import os

import pytest
import requests

BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT_SEGUNDOS = 10


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, path, **kwargs):
        kwargs.setdefault("timeout", TIMEOUT_SEGUNDOS)
        return self.session.request(method, self.base_url + path, **kwargs)

    def get(self, path, **kwargs):
        return self.request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self.request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self.request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self.request("DELETE", path, **kwargs)


@pytest.fixture(scope="session")
def api():
    client = ApiClient(BASE_URL)
    yield client
    client.session.close()
