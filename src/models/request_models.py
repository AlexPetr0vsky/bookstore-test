from dataclasses import dataclass


@dataclass
class RegisterUserRequest:
    username: str
    email: str
    password: str
