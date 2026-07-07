import requests
import logging
from typing import Optional, Dict, Any
from urllib.parse import urljoin

from src.models.response_models import BookResponse, AuthorResponse, ApiResponse

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

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        json: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        timeout: Optional[int] = None,
        **kwargs
    ) -> requests.Response:
        """
        Универсальный метод для всех HTTP-запросов.
        """
        url = urljoin(self.base_url + '/', endpoint.lstrip('/'))
        timeout = timeout or self.timeout

        logger.info(f"{method} {url}")

        if json:
            logger.debug(f"JSON: {json}")
        if params:
            logger.debug(f"Params: {params}")

        if headers:
            request_headers = {**self.session.headers, **headers}
        else:
            request_headers = self.session.headers

        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=json,
                data=data,
                headers=request_headers,
                timeout=timeout,
                **kwargs
            )

            logger.info(f"Response: {response.status_code} {response.reason}")
            if response.text and len(response.text) < 1000:
                logger.debug(f"Body: {response.text[:200]}...")

            return response

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout: {url}")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error: {url}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise

    def get(
        self,
        endpoint: str,
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """GET-запрос"""
        return self._request("GET", endpoint, params=params, headers=headers, **kwargs)

    def post(
        self,
        endpoint: str,
        json: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """POST-запрос"""
        return self._request("POST", endpoint, json=json, data=data, headers=headers, **kwargs)

    def put(
        self,
        endpoint: str,
        json: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """PUT-запрос"""
        return self._request("PUT", endpoint, json=json, data=data, headers=headers, **kwargs)

    def patch(
        self,
        endpoint: str,
        json: Optional[Dict] = None,
        data: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """PATCH-запрос"""
        return self._request("PATCH", endpoint, json=json, data=data, headers=headers, **kwargs)

    def delete(
        self,
        endpoint: str,
        headers: Optional[Dict] = None,
        **kwargs
    ) -> requests.Response:
        """DELETE-запрос"""
        return self._request("DELETE", endpoint, headers=headers, **kwargs)

    def set_header(self, key: str, value: str):
        """Добавить заголовок для всех последующих запросов"""
        self.session.headers[key] = value

    def set_auth_token(self, token: str):
        """Установить Bearer-токен для всех запросов"""
        self.session.headers["Authorization"] = f"Bearer {token}"

    def clear_headers(self):
        """Сбросить все кастомные заголовки (оставить только базовые)"""
        self.session.headers.clear()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def get_books(self) -> ApiResponse:
        url = f"{self.base_url}/books"
        response = self.session.get(url)
        return ApiResponse(
            status_code=response.status_code,
            headers=dict(response.headers),
            data=response.json()
        )

    def get_authors(self) -> list[AuthorResponse]:
        response = self.get("authors")
        response.raise_for_status()
        data = response.json()
        return [AuthorResponse(**item) for item in data]
