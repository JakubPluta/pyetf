from typing import Any, Dict
import requests
from requests import HTTPError

from etfpy.utils import get_retry_session, get_headers
from etfpy.log import get_logger


logger = get_logger(__name__)


class BaseClient:
    """Base client for interacting with the etfdb API.

    Parameters
    ----------
    kwargs: Any
        Additional keyword arguments to pass to the client.

    Attributes
    ----------
    _base_url: str
        The base URL for the etfdb API.
    _api_url: str
        The URL for the etfdb screener API.
    _session: requests.Session
        A session object used to make all requests.
    """

    def __init__(self, **kwargs: Any):
        self._base_url = "https://etfdb.com"
        self._api_url = f"{self._base_url}/api/screener/"

        self._session = get_retry_session()

        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def session(self) -> requests.Session:
        """Returns the request session object."""
        return self._session

    @staticmethod
    def _prepare_request_body(
        page: int = 1, per_page: int = 250, **kwargs: Any
    ) -> Dict:
        """Prepares the request body for a screener request.

        Parameters
        ----------
        page: int, default=1
            The page number to request.
        per_page: int, default=250
            The number of results per page to request.
        kwargs: Any
            Additional keyword arguments to pass to the request.

        Returns
        -------
        Dict
            The request body.

        Raises
        ------
        ValueError
            If the page number is less than 1.
        """

        if page < 1:
            raise ValueError("page param needs to be positive number")
        body = {
            "tab": "returns",
            "page": page,
            "per_page": per_page,
            "only": ["meta", "data", None],
        }
        body.update(**kwargs)
        return body

    def post_request(self, request_body: Dict) -> requests.Response:
        """Posts a request to the ETFDB screener API.

        Parameters
        ----------
        request_body: Dict
            The request body.

        Returns
        -------
        requests.Response
            The response object.
        """
        return self.session.post(
            self._api_url, json=request_body, headers=get_headers()
        )

    def get_metadata(self) -> Dict:
        """Gets the metadata for the ETFDB screener API.

        Returns
        -------
        Dict
            The metadata dictionary.
        """

        try:
            return self.post_request(self._prepare_request_body()).json()
        except HTTPError as he:
            logger.error(str(he))
        except AttributeError as ae:
            logger.error(str(ae))
        return {}
