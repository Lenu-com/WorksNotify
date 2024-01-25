import requests
from app.infrastructure.interfaces.i_http_client import IHttpClient


class HttpClient(IHttpClient):
    def post(self, url, headers, data) -> None:
        requests.post(url=url, headers=headers, data=data)
