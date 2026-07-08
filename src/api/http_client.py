import requests
import logging
from typing import Optional, Dict, Any, List
from urllib.parse import urljoin

from src.models.response_models import BookResponse, ApiResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HTTPClient:
    """
    Базовый HTTP-клиент для работы с API.
    Инкапсулирует requests.Session, добавляет логирование и обработку ошибок.
    """

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get(self, endpoint: str) -> ApiResponse:
        """GET-запрос к эндпоинту. Возвращает статус, заголовки и JSON."""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=response.json()
        )

    def post(self, endpoint: str, data: dict = None) -> ApiResponse:
        """POST-запрос к эндпоинту."""

        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=response.json() if response.text else {}
        )

    def get_books(self) -> ApiResponse:
        """GET /books. Возвращает список книг в виде BookResponse."""

        url = f"{self.base_url}/books"
        response = self.session.get(url)
        data = response.json()
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=[BookResponse(**item) for item in data]
        )

    def delete_book(self, book_id: int) -> ApiResponse:
        """DELETE /books/{id}"""

        url = f"{self.base_url}/books/{book_id}"
        response = self.session.delete(url)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=response.json() if response.text else {}
        )