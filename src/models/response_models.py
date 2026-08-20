from dataclasses import dataclass
from typing import Dict, Any, List, Optional


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


@dataclass
class BookListResponse:
    books: List[BookResponse]


@dataclass
class AuthorResponse:
    id: int
    name: str
    photo: Optional[str] = None
    wiki: Optional[str] = None


@dataclass
class AuthorListResponse:
    authors: List[AuthorResponse]


@dataclass
class GeneralErrorResponse:
    error: str
    message: Optional[str] = None
    