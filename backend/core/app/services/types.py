from dataclasses import dataclass
from enum import Enum
from typing import TypedDict, NamedTuple, List

from django.core.files.uploadedfile import InMemoryUploadedFile

from dacite import from_dict, Config


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


class PaymentStatuses(Enum):
    NEW = "NEW"
    FORM_SHOWED = "FORM_SHOWED"
    DEADLINE_EXPIRED = "DEADLINE_EXPIRED"
    CANCELED = "CANCELED"
    PREAUTHORIZING = "PREAUTHORIZING"
    AUTHORIZING = "AUTHORIZING"
    AUTH_FAIL = "AUTH_FAIL"
    REJECTED = "REJECTED"
    PAY_CHECKING = "PAY_CHECKING"
    AUTHORIZED = "AUTHORIZED"
    REVERSING = "REVERSING"
    PARTIAL_REVERSED = "PARTIAL_REVERSED"
    REVERSED = "REVERSED"
    CONFIRMING = "CONFIRMING"
    CONFIRM_CHECKING = "CONFIRM_CHECKING"
    CONFIRMED = "CONFIRMED"
    REFUNDING = "REFUNDING"
    PARTIAL_REFUNDED = "PARTIAL_REFUNDED"
    REFUNDED = "REFUNDED"


@dataclass
class InitPaymentResponse:
    Success: bool
    Status: PaymentStatuses
    PaymentId: str
    PaymentURL: str

    @classmethod
    def from_dict(cls, data: dict) -> "InitPaymentResponse":
        return from_dict(
            data_class=InitPaymentResponse,
            data=data,
            config=Config(type_hooks={PaymentStatuses: PaymentStatuses}),
        )


class QuestionnaireTeacherData(TypedDict):
    name: str
    surname: str
    date_of_birth: str
    gender: str
    about_me: str
    work_experience: str
    vk_link: str
    telegram_link: str
    certificate_photos: List[InMemoryUploadedFile]
    passport_photos: List[InMemoryUploadedFile]
    user_photos: List[InMemoryUploadedFile]
