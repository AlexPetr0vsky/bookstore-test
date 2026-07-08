from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class ApiResponse:
    status_code: int
    headers: Dict[str, str]
    data: Any


@dataclass
class BookResponse:
    id: int
    book: str
    description: str
    icon_book: str
    author_id: int
