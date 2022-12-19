from functools import cached_property

from django.db import transaction
from rest_framework.exceptions import NotAcceptable

from core.app.repositories.attachment_repository import AttachmentRepository
from core.app.repositories.teachers_questionnaire_repository import (
    QuestionnaireTeacherRepository,
)
from core.app.repositories.user_repository import UserRepository
from core.app.services.types import QuestionnaireTeacherData
from core.models import (
    User,
    QuestionnaireTeacher,
    UserRoles,
    Attachment,
)


class QuestionnaireTeacherRegister:
    questionnaire_repository = QuestionnaireTeacherRepository()
    user_repository = UserRepository()

    def __init__(self, user: User, data: QuestionnaireTeacherData):
        self.data = data
        self.user = user

    @cached_property
    def questionnaire(self) -> QuestionnaireTeacher:
        questionnaire = QuestionnaireTeacher()
        questionnaire.name = self.data["name"]
        questionnaire.surname = self.data["surname"]
        questionnaire.date_of_birth = self.data["date_of_birth"]
        questionnaire.gender = self.data["gender"]
        questionnaire.about_me = self.data["about_me"]
        questionnaire.work_experience = self.data["work_experience"]
        questionnaire.vk_link = self.data["vk_link"]
        questionnaire.telegram_link = self.data["telegram_link"]
        questionnaire.passport_photo = self.data["passport_photo"]
        questionnaire.user_photo = self.data["user_photo"]
        questionnaire.user_with_passport_photo = self.data["user_with_passport_photo"]
        questionnaire.user = self.user
        return questionnaire

    def create_questionnaire_certificate_photos(
        self, questionnaire: QuestionnaireTeacher
    ) -> None:
        photos = []
        for item in self.data["certificate_photos"]:
            attachment = Attachment()
            attachment.image = item
            photos.append(attachment)
        AttachmentRepository(model=Attachment).bulk_create(models=photos)
        questionnaire.setup_certificate_photos(photos=photos)

    def create(self) -> QuestionnaireTeacher:
        if self.user.has_role(role=UserRoles.TEACHER):
            raise NotAcceptable("User already has teacher role")
        if self.questionnaire_repository.has_moderate_questionnaires(user=self.user):
            raise NotAcceptable("User has moderate questionnaires")
        with transaction.atomic():
            self.questionnaire_repository.store(questionnaire=self.questionnaire)
            self.create_questionnaire_certificate_photos(self.questionnaire)
        return self.questionnaire
