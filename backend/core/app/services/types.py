from typing import TypedDict, NamedTuple

import PIL.JpegImagePlugin


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


class TextMailData(NamedTuple):
    subject: str
    message: str
    receivers: list


class HtmlMailData(NamedTuple):
    subject: str
    message: str
    receivers: list
    template_path: str


class QuestionnaireTeacherData(TypedDict):
    name: str
    surname: str
    date_of_birth: str
    gender: str
    about_me: str
    work_experience: str
    vk_link: str
    telegram_link: str
    certificate_photos: PIL.JpegImagePlugin.JpegImageFile
    passport_photo: PIL.JpegImagePlugin.JpegImageFile
    user_photo: PIL.JpegImagePlugin.JpegImageFile
    roles: str
