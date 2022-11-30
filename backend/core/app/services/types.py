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


class TextMailData(TypedDict):
    subject: str
    message: str
    receivers: list


class HtmlMailData(TypedDict):
    subject: str
    message: str
    receivers: list
    template_path: str