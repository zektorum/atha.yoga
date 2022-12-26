import hashlib
import logging
from datetime import timedelta
from typing import Tuple, Any, List, cast

import furl
import requests
from django.utils.timezone import now

from core.app.services.types import InitPaymentResponse, PaymentStatuses
from core.app.utils.exceptions import ServerError
from server import settings

logger = logging.getLogger("daily_log")


class TinkoffPaymentService:
    BASE_URL = "https://securepay.tinkoff.ru/v2"

    def init_pay(
        self, amount: int, transaction_id: str, description: str, success_url: str
    ) -> InitPaymentResponse:
        url = furl.furl(url=self.BASE_URL).join("Init")
        params = {
            "TerminalKey": settings.TERMINAL_KEY,
            "Amount": amount,
            "Description": description,
            "OrderId": transaction_id,
            "RedirectDueDate": (now() + timedelta(hours=1))
            .replace(microsecond=0)
            .isoformat(),
            "SuccessURL": success_url,
        }
        res = requests.post(url=url.url, data=params).json()
        if not res.get("Success"):
            logger.error(res)
            raise ServerError(detail="Payment not success")
        return InitPaymentResponse.from_dict(data=res)

    def payment_status(self, payment_id: str) -> PaymentStatuses:
        url = furl.furl(url=self.BASE_URL).join("GetState")
        params = {
            "TerminalKey": settings.TERMINAL_KEY,
            "PaymentId": payment_id,
            "Password": settings.TERMINAL_PASSWORD,
        }
        sorted_params = dict(
            cast(List[Tuple[str, Any]], sorted(params.items(), key=lambda x: x[0]))
        )
        token = "".join(map(str, sorted_params.values()))
        token_hash = hashlib.new("sha256")
        token_hash.update(token.encode())
        params["Token"] = token_hash.hexdigest()
        res = requests.post(url, data=params).json()
        if not res.get("Success"):
            logger.error(res)
            raise ServerError(detail="Payment not success")
        return PaymentStatuses(res.get("Status"))
