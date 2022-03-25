from dataclasses import dataclass


@dataclass
class User:
    name: str
    password: str
    email: str


def create_user(name, email, password) -> User:
    print(f"CREATE USER {name}")
    return User(name=name, email=email, password=password)
