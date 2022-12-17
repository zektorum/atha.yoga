import uuid
from typing import Any

from django.core.management import BaseCommand

from core.app.services.payment_service import TinkoffPaymentService


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        uid = uuid.uuid4()
        print(
            TinkoffPaymentService().init_pay(
                amount=1000, transaction_id=str(uid), description="Купи купи"
            )
        )
        # print(TinkoffPaymentService().payment_status(
        #     payment_id="2087087239"
        # ))
