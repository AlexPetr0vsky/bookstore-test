import requests
from typing import Any, Dict, Optional
from src.models.response_models import BookResponse, ApiResponse, BookListResponse, AuthorListResponse, AuthorResponse


class HTTPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        return self.session.request(method, url, **kwargs)

    def get_books(self) -> ApiResponse:
        response = self._request("GET", "books")
        data = response.json()
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=BookListResponse(books=[BookResponse(**item) for item in data])
        )

    def get_book(self, book_id: int) -> ApiResponse:
        response = self._request("GET", f"books/{book_id}")
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=BookResponse(**response.json())
        )

    def post_book(self, data: Dict[str, Any]) -> ApiResponse:
        response = self._request("POST", "books", json=data)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=BookResponse(**response.json())
        )


    def patch_book(self, book_id: int, data: Dict[str, Any]) -> ApiResponse:
        response = self._request("PATCH", f"books/{book_id}", json=data)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=BookResponse(**response.json())
        )


    def put_book(self, book_id: int, data: Dict[str, Any]) -> ApiResponse:
        response = self._request("PUT", f"books/{book_id}", json=data)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=BookResponse(**response.json())
        )


    def delete_book(self, book_id: int) -> ApiResponse:
        response = self._request("DELETE", f"books/{book_id}")
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=None
        )


    def get_authors(self) -> ApiResponse:
        response = self._request("GET", "authors")
        data = response.json()
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=AuthorListResponse(authors=[AuthorResponse(**item) for item in data])
        )

    def get_author(self, author_id: int) -> ApiResponse:
        response = self._request("GET", f"authors/{author_id}")
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=AuthorResponse(**response.json())
        )

    def delete_author(self, author_id: int) -> ApiResponse:
        response = self._request("DELETE", f"authors/{author_id}")
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=None
        )
