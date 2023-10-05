import itertools
from typing import Any, Dict, Generator, List

from requests.exceptions import ConnectionError, Timeout

from etfpy.client._base_client import BaseClient
from etfpy.log import get_logger

logger = get_logger(__name__)


class ETFListScraper(BaseClient):
    """Scrapes ETF data from the ETFDB.
    It"S a list of all available etfs in ETFDB
    """

    def _parse_etf_record(self, obj: dict) -> Dict[str, Any]:
        """Parses an ETF record into a dictionary.

        Parameters
        ----------
        obj: dict
            The ETF record.

        Returns
        -------
        Dict[str, Any]
            The parsed ETF record.

        """

        return {
            "symbol": obj.get("symbol", {}).get("text"),
            "asset_class": obj.get("asset_class"),
            "price": obj.get("price"),
            "average_volume": obj.get("average_volume"),
            "name": obj.get("name", {}).get("text"),
            "url": self._base_url + obj.get("symbol", {}).get("url"),
            "one_year_return": obj.get("ytd"),
        }

    def _prepare_etfs_list(
        self, etfs: List[dict]
    ) -> Generator[Dict[str, Any], None, None]:
        """Prepares a list of ETFs for parsing.

        Parameters
        ----------
        etfs: List[dict]
            The list of ETFs.

        Yields
        ------
        Dict[str, Any]
            A parsed ETF record.

        """
        for etf in etfs:
            yield self._parse_etf_record(etf)

    def _scrape_page(self, page: int, page_size=250) -> List[Dict[Any, Any]]:
        """Scrapes a page of ETFs from the ETFDB API.

        Parameters
        ----------
        page: int
            The page number to scrape.
        page_size: int, default=250
            The number of ETFs to scrape per page.

        Returns
        -------
        List[dict]
            A list of ETF records.

        Raises
        ------
        ConnectionError
            If there is a connection error.
        Timeout
            If the request times out.

        """
        logger.debug("getting data for page: %s with page_size: %s", page, page_size)
        request_body = self._prepare_request_body(page=page, page_size=page_size)
        try:
            return self.post_request(request_body).json()["data"]
        except (ConnectionError, Timeout) as e:
            logger.error("connection timeout: %s", str(e))
        except (AttributeError, KeyError) as e:
            logger.error("another exception happened: %s", str(e))
        return []

    def get_etfs(
        self, page_size: int = 250
    ) -> Generator[List[Dict[str, Any]], None, None]:
        """Scrapes all ETFs from the ETFDB API.

        Parameters
        ----------
        page_size: int, default=250
            The number of ETFs to scrape per page.

        Yields
        ------
        List[Dict[str, Any]]
            A list of parsed ETF records.

        """
        page = 1
        while True:
            etfs = self._scrape_page(page, page_size)
            if not etfs:
                break
            yield list(self._prepare_etfs_list(etfs))
            page += 1


def get_all_etfs(page_size: int = 250) -> List[Dict[str, Any]]:
    """Scrapes all ETFs from the ETFDB API and returns them as a list.

    Parameters
    ----------
    page_size: int, default=250
        The number of ETFs to scrape per page.

    Returns
    -------
    List[Dict[str, Any]]
        A list of parsed ETF records.

    """

    etfs_gen = ETFListScraper().get_etfs(page_size)
    return list(itertools.chain(*etfs_gen))
