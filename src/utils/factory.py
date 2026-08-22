from typing import Dict, Any
from faker import Faker

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
