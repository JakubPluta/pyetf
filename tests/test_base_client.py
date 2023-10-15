from unittest import mock

import pandas as pd
import pytest
import requests

from etfpy.client._base_client import BaseClient
from tests.utils import get_quotes


@pytest.fixture
def client():
    return BaseClient()


def test_can_init_base_client(client):
    assert client._base_url == "https://etfdb.com"
    assert client._api_url == "https://etfdb.com/api/screener/"
    assert isinstance(client, BaseClient)


def test_init_base_client_with_kwargs():
    client = BaseClient(a=1, something="nothing")
    assert client.a == 1 and client.something == "nothing"


def test_has_session(client):
    assert isinstance(client._session, requests.Session)
    assert isinstance(client._requests_session, requests.Session)


def test_can_prepare_request_body(client):
    assert client._prepare_request_body() == {
        "page": 1,
        "per_page": 250,
        "only": ["meta", "data", None],
    }
    assert client._prepare_request_body(5, 1000) == {
        "page": 5,
        "per_page": 1000,
        "only": ["meta", "data", None],
    }

    with pytest.raises(ValueError) as ve:
        client._prepare_request_body(-1, 1000)
    assert str(ve.value) == "page param needs to be positive number"


@mock.patch("etfpy.client._base_client.BaseClient.post_request")
def test_can_get_metadata(m, client):
    m.return_value = {}
    assert client.get_metadata() == {}

    m.return_value = 5
    assert client.get_metadata() == {}

    class FakeResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return self.data

    m.return_value = FakeResponse({"some": "data"})
    assert client.get_metadata() == {"some": "data"}


@mock.patch.object(requests, "get")
def test_service_get(mock_request_get, client):
    def res():
        r = requests.Response()
        r.status_code = 200
        type(r).text = mock.PropertyMock(return_value=get_quotes())  # property mock
        return r

    mock_request_get.return_value = res()
    quotes = client._get_quotes("SPY")
    assert isinstance(quotes, pd.DataFrame) and quotes["symbol"].unique()[0] == "SPY"
