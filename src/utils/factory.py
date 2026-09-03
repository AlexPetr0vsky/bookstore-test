from random import randint
from typing import Dict, Any
from faker import Faker

from src.models.request_models import RegisterUserRequest

fake = Faker()


class BookFactory:
    @staticmethod
    def create_payload(**kwargs) -> Dict[str, Any]:
        return {
            "book": kwargs.get('book') or fake.word() + " " + fake.word(),
            "name": kwargs.get('name') or fake.name(),
            "photo": kwargs.get('photo', "http://example.com/photo.jpg"),
            "wiki": kwargs.get('wiki', "http://example.com/wiki"),
            "description": kwargs.get('description', fake.sentence()),
            "icon_book": kwargs.get('icon_book', "http://example.com/icon.jpg")
        }


class UserFactory:
    @staticmethod
    def create_payload(**kwargs) -> RegisterUserRequest:
        request = {
            "username": kwargs.get('username') or fake.name(),
            "password": kwargs.get('password', fake.word() + "".join([str(randint(1, 10)) for _ in range(3)]) + "!"),
            "email": kwargs.get('email', fake.word() + "@" + fake.word() + ".com")
        }

        return RegisterUserRequest(**request)
