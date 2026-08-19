import requests


class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get(self, endpoint, **kwargs):
        return requests.get(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def post(self, endpoint, **kwargs):
        return requests.post(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def put(self, endpoint, **kwargs):
        return requests.put(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        return requests.delete(
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )