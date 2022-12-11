import logging

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from furl import furl
from rest_framework.request import Request
from rest_framework.views import APIView

from core.app.repositories.payment_repository import PaymentRepository
from core.app.services.payment_service import TinkoffPaymentService
from core.app.services.types import PaymentStatuses


class SuccessPaymentHandler(APIView):
    def get(self, request: Request, transaction_id: str) -> HttpResponseRedirect:
        transaction = PaymentRepository().find_by_id(id_=transaction_id)
        if not transaction:
            logging.getLogger("daily_log").error(
                f"Undefined transaction with pk {transaction_id}"
            )
            return redirect(furl(settings.SITE_URL).join("fail-payment").url)
        payment_status = TinkoffPaymentService().payment_status(
            payment_id=transaction.payment_id
        )
        if payment_status != PaymentStatuses.CONFIRMED:
            return redirect(furl(settings.SITE_URL).join("fail-payment").url)
        return redirect(furl(settings.SITE_URL).join("success-payment").url)
