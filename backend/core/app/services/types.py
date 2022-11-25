from typing import TypedDict


class UserRegisterData(TypedDict):
    email: str
    password: str


class UserLoginData(TypedDict):
    email: str
    password: str

class UserChangePassData(TypedDict):
    email: str
    password: str
    new_password: str