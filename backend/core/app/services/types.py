from dataclasses import dataclass
from enum import Enum
from typing import TypedDict, NamedTuple


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
class InitPaymentResponse(TypedDict):
    Success: bool
    Status: PaymentStatuses
    PaymentId: int
    PaymentURL: str
