import requests
from dataclasses import dataclass
from typing import Any, Dict, Optional
from src.models.response_models import BookResponse


@dataclass
class ApiResponse:
    status_code: int
    headers: Dict[str, str]
    data: Any


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> ApiResponse:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)

        # Пытаемся спарсить JSON только если есть тело и это JSON
        data = None
        if response.text:
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                try:
                    data = response.json()
                except requests.exceptions.JSONDecodeError:
                    data = response.text
            else:
                data = response.text
        else:
            data = {}

        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=data
        )

    def get(self, endpoint: str) -> ApiResponse:
        return self._request("GET", endpoint)

    def post(self, endpoint: str, data: Optional[Dict] = None) -> ApiResponse:
        return self._request("POST", endpoint, json=data)

    def delete(self, endpoint: str) -> ApiResponse:
        return self._request("DELETE", endpoint)

    def get_books(self) -> ApiResponse:
        response = self._request("GET", "books")
        if isinstance(response.data, list):
            return ApiResponse(
                status_code=response.status_code,
                headers=response.headers,
                data=[BookResponse(**item) for item in response.data]
            )
        return response

    def delete_book(self, book_id: int) -> ApiResponse:
        return self._request("DELETE", f"books/{book_id}")

    def get_authors(self) -> ApiResponse:
        return self._request("GET", "authors")

    def delete_author(self, author_id: int) -> ApiResponse:
        return self._request("DELETE", f"authors/{author_id}")