import inspect
from typing import Any, Dict, Iterator, List, Optional, Tuple

import bs4
import requests
from random_user_agent.params import OperatingSystem, SoftwareName
from random_user_agent.user_agent import UserAgent
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from etfpy.log import get_logger

logger = get_logger("utils")

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
    """Get headers for HTTP requests.

    Returns:
        A dictionary of headers.
    """

    return {
        "User-Agent": user_agent_rotator.get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }


def get_retry_session(retries=6, backoff_factor=0.1) -> requests.Session:
    """Get a Session object with retry capabilities.

    Args:
        retries: The number of retries to attempt before giving up.
        backoff_factor: The factor by which to increase the wait time between retries.

    Returns:
        A Session object with retry capabilities.
    """
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
    session.mount("http://", adapter)
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


def _handle_nth_child(x: bs4.element.Tag, child_num: int) -> Optional[str]:
    """Extract from beautiful soup tag a nth-child(1) stripped text
    It's utility function to handle repeated pattern in etf data scraping code
    :nth-child() selector selects child elements according to
    their position among all the sibling elements within a parent

    Parameters
    ----------
    x : bs4.element.Tag
        beautiful soup tag
    child_num : int
        child to extract

    Returns
    -------
    str
        stripped text from nth-child
    """
    try:
        return x.select_one(f":nth-child({child_num})").text.strip()
    except Exception as e:
        logger.warning(str(e))
        return None


def handle_find_all_rows(rows: bs4.element.ResultSet) -> Dict[str, str]:
    """
    Extract data from a ResultSet of BeautifulSoup elements representing
    table rows and return a dictionary of key-value pairs.

    Parameters
    ----------
    rows : bs4.element.ResultSet
        A ResultSet of BeautifulSoup elements representing table rows.

    Returns
    -------
    typing.Dict[str, str]
        A dictionary of key-value pairs, where the keys are the values of the first child element of
        each row and the values are the values of the second child element of each row.

    Examples
    --------
    >>> soup = BeautifulSoup("<table id='my_table'><tr><td>1</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>", "html.parser")

    >>> rows = soup.find_all("tr")

    >>> results = handle_find_all_rows(rows)

    >>> print(results)
    {'1': '2', '3': '4'}
    """

    results = {}
    for row in rows:
        key = _handle_nth_child(row, 1)
        value = _handle_nth_child(row, 2)
        if key:
            results[key] = value
    return results


def chunkify(lst: list, n: int) -> Iterator[list]:
    """
    Yield successive n-sized chunks from lst.

    Parameters
    ----------
    lst : list
        The list to chunk.
    n : int
        The size of each chunk.

    Returns
    -------
    Iterator[list]
        An iterator over the chunks.

    Examples
    --------
    >>> list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> chunks = chunkify(list1, 3)

    >>> for chunk in chunks:
    ...     print(chunk)
    ...
    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]
    [10]
    """
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def _get_tbody_thead(
    soup: bs4.BeautifulSoup, table_id: str, tag="table"
) -> Tuple[List[str], List[str]]:
    """
    Get the table body and header rows for a given table ID.

    Parameters
    ----------
    soup : BeautifulSoup
        The BeautifulSoup object representing the HTML document.
    table_id : str
        The ID of the table.
    tag : str, optional
        The HTML tag of the html element. Defaults to `table`.

    Returns
    -------
    typing.Tuple[typing.List[str], typing.List[str]]
        A tuple containing two lists: the first list contains the table body rows
        and the second list contains the table header rows.

    Examples
    --------
    >>> soup = BeautifulSoup(
    "<table id='my_table'><thead><tr><th>Header 1</th>
    <th>Header 2</th></tr></thead><tbody><tr><td>Data 1</td><td>Data 2</td>
    </tr><tr><td>Data 3</td><td>Data 4</td></tr></tbody></table>",
    "html.parser")

    >>> rows, thead = _get_tbody_thead(soup, table_id="my_table")

    >>> print(rows)
    ['Data 1', 'Data 3']

    >>> print(thead)
    ['Header 2']
    """
    rows = [
        x.text.strip()
        for x in soup.find(tag, {"id": table_id}).find("tbody").find_all("td")
    ]
    thead = [
        x.text.strip()
        for x in soup.find(tag, {"id": table_id}).find("thead").find_all("th")
    ]
    return rows, thead[1:]


def handle_tbody_thead(soup, table_id: str, tag="table") -> Dict:
    """Extract data from a table body and header, and return a dictionary of key-value pairs.

    Parameters
    ----------
    soup : BeautifulSoup
        The BeautifulSoup object representing the HTML document.
    table_id : str
        The ID of the table.
    tag : str, optional
        The HTML tag of the table element. Defaults to `table`.

    Returns
    -------
    typing.Dict[str, typing.Dict[str, str]]
        A dictionary of key-value pairs, where the keys are the values of
        the first column in the table body and the values are dictionaries mapping
        the table header values to the corresponding values in the table body row.

    Examples
    --------
    >>> soup = BeautifulSoup(
    "<table id='my_table'><thead><tr><th>Size</th><th>Value</th></tr></thead><tbody>
    <tr><td>Small</td><td>10</td></tr><tr><td>Medium</td><td>20</td></tr><tr><td>Large</td>
    <td>30</td></tr></tbody></table>",
    "html.parser"
    )

    >>> results = handle_tbody_thead(soup, table_id="my_table")

    >>> print(results)
    {'Small': {'Value': '10'}, 'Medium': {'Value': '20'}, 'Large': {'Value': '30'}}
    """

    rows, header = _get_tbody_thead(soup, table_id, tag)
    results = {}
    for row in list(chunkify(rows, 4)):
        size_key = row.pop(0)
        results[size_key] = dict(zip(header, row))
    return results


def get_class_property_methods(cls):
    """
    Get a list of all the property methods defined in a class.

    Parameters
    ----------
    cls : class
        The class to get the property methods of.

    Returns
    -------
    list of str
        A list of the names of all the property methods defined in the class.

    Examples
    --------
    >>> class MyClass:
    ...     @property
    ...     def prop1(self):
    ...         return 1
    ...
    ...     @property
    ...     def prop2(self):
    ...         return 2
    ...
    >>> prop_methods = get_class_property_methods(MyClass)
    >>> prop_methods
    ['prop1', 'prop2']
    """
    props = []
    for x in inspect.getmembers(cls):
        if isinstance(x[1], property):
            props.append(x[0])
    return props


def convert_spaces_to_underscore_and_lowercase(data: dict):
    """Converts spaces to underscores in all keys in a nested dictionary.

    Args:
        data: A nested dictionary.

    Returns:
        A nested dictionary with all spaces in keys converted to underscores.
    """

    def recurse(data):
        if isinstance(data, dict):
            return {k.replace(" ", "_").lower(): recurse(v) for k, v in data.items()}
        return data

    return recurse(data)


def remove_nested_benchmarks(data: dict, ticker: str):
    results = {}
    for k, v in data.items():
        results[k] = v.get(ticker) if isinstance(v, dict) else v
    return results
