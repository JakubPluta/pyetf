import inspect
from typing import Dict, Any, Optional, Tuple
import bs4
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from etfpy.log import get_logger


logger = get_logger(__name__)

software_names = [SoftwareName.CHROME.value]
operating_systems = [
    OperatingSystem.WINDOWS.value,
    OperatingSystem.LINUX.value,
    OperatingSystem.MAC.value,
]
user_agent_rotator = UserAgent(
    software_names=software_names, operating_systems=operating_systems, limit=50
)


def get_headers() -> Dict:
    return {
        "User-Agent": user_agent_rotator.get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }


def get_retry_session(retries=6, backoff_factor=0.1):
    session = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504, 406],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("https://etfdb.com", adapter)
    session.headers.update(get_headers())
    return session


def _handle_spans(spans) -> Optional[Tuple[Any]]:
    """Parses a list of spans into a record.

    Args:
        spans: A list of spans.

    Returns:
        A record, or None if the record could not be parsed.
    """
    try:
        record = tuple(span.text.strip() for span in spans)
        return record[:2] if len(record) > 2 else record
    except Exception as e:
        logger.debug("couldn't parse profile container %s", str(e))
    return None


def _handle_nth_child(x: bs4.element.Tag, child_num: int):
    try:
        return x.select_one(f":nth-child({child_num})").text.strip()
    except Exception as e:
        logger.warning(str(e))
        return None


def handle_find_all_rows(rows: bs4.element.ResultSet):
    results = {}
    for row in rows:
        key = _handle_nth_child(row, 1)
        value = _handle_nth_child(row, 2)
        if key:
            results[key] = value
    return results


def chunkify(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def _get_tbody_thead(soup, table_id: str, tag="table"):
    rows = [
        x.text.strip()
        for x in soup.find(tag, {"id": table_id}).find("tbody").find_all("td")
    ]
    thead = [
        x.text.strip()
        for x in soup.find(tag, {"id": table_id}).find("thead").find_all("th")
    ]
    return rows, thead[1:]


def handle_tbody_thead(soup, table_id: str, tag="table"):
    rows, header = _get_tbody_thead(soup, table_id, tag)
    results = {}
    for row in list(chunkify(rows, 4)):
        size_key = row.pop(0)
        results[size_key] = dict(zip(header, row))
    return results


def get_class_property_methods(cls):
    props = []
    for x in inspect.getmembers(cls):
        if isinstance(x[1], property):
            props.append(x[0])
    return props
