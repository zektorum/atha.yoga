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
    QuestionnaireTeacherCertificatePhoto,
    QuestionnaireTeacherPassportPhoto,
    QuestionnaireTeacherUserPhoto,
)


class QuestionnaireTeacherRegister:
    questionnaire_repository = QuestionnaireTeacherRepository()
    user_repository = UserRepository()

    def __init__(self, user: User, data: QuestionnaireTeacherData):
        self.data = data
        self.user = user

    def certificates_photos_create(self, questionnaire: QuestionnaireTeacher) -> None:
        certificates_to_create = []
        for item in self.data["certificate_photos"]:
            certificate = QuestionnaireTeacherCertificatePhoto()
            certificate.image = item
            certificate.questionnaire = questionnaire
            certificates_to_create.append(certificate)
        AttachmentRepository(model=QuestionnaireTeacherCertificatePhoto).bulk_create(
            models=certificates_to_create
        )

    def passport_photos_create(self, questionnaire: QuestionnaireTeacher) -> None:
        passports_to_create = []
        for item in self.data["passport_photos"]:
            passport_photo = QuestionnaireTeacherPassportPhoto()
            passport_photo.image = item
            passport_photo.questionnaire = questionnaire
            passports_to_create.append(passport_photo)
        AttachmentRepository(model=QuestionnaireTeacherPassportPhoto).bulk_create(
            models=passports_to_create
        )

    def user_photos_create(self, questionnaire: QuestionnaireTeacher) -> None:
        user_photos_to_create = []
        for item in self.data["user_photos"]:
            user_photo = QuestionnaireTeacherUserPhoto()
            user_photo.image = item
            user_photo.questionnaire = questionnaire
            user_photos_to_create.append(user_photo)
        AttachmentRepository(model=QuestionnaireTeacherPassportPhoto).bulk_create(
            models=user_photos_to_create
        )

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
        questionnaire.user = self.user

        with transaction.atomic():
            self.questionnaire_repository.store(questionnaire=questionnaire)
            self.certificates_photos_create(questionnaire=questionnaire)
            self.passport_photos_create(questionnaire=questionnaire)
            self.user_photos_create(questionnaire=questionnaire)
        return questionnaire

    def create(self) -> QuestionnaireTeacher:
        if self.user.has_role(role=UserRoles.TEACHER):
            raise NotAcceptable("User already has teacher role")
        if self.questionnaire_repository.has_moderate_questionnaires(user=self.user):
            raise NotAcceptable("User has moderate questionnaires")

        return self.questionnaire
