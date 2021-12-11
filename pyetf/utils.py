import inspect
import json
import functools
import logging
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def dump_json(data, name):
    with open(name, "w") as f:
        json.dump(data, f)


def _try(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.info(e)

    return inner


def retry_session(retries=5, backoff_factor=0.5, session=None, *mounts):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    if mounts:
        for m in mounts:
            session.mount(m, adapter)
    return session


def get_class_property_methods(cls):
    props = []
    for x in inspect.getmembers(cls):
        if isinstance(x[1], property):
            props.append(x[0])
    return props
