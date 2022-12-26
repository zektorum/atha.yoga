from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet

from core.app.repositories.teachers_questionnaire_repository import (
    QuestionnaireTeacherRepository,
)
from core.app.services.teachers_questionnaire_services import QuestionnaireTeacherAccept
from core.models import QuestionnaireTeacher, QuestionnaireTeacherStatuses


@admin.action(description="Accept selected questionnaires")
def accept_questionnaires(
    modeladmin: ModelAdmin,
    request: WSGIRequest,
    queryset: QuerySet[QuestionnaireTeacher],
) -> None:
    for item in queryset:
        QuestionnaireTeacherAccept(questionnaire=item).accept()


@admin.action(description="Decline selected questionnaires")
def decline_questionnaires(
    modeladmin: ModelAdmin,
    request: WSGIRequest,
    queryset: QuerySet[QuestionnaireTeacher],
) -> None:
    repo = QuestionnaireTeacherRepository()
    for item in queryset:
        item.status = QuestionnaireTeacherStatuses.DECLINED
        repo.store(item)
