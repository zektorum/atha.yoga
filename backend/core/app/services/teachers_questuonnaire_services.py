from functools import cached_property

from rest_framework.exceptions import NotAcceptable

from core.app.repositories.user_repository import UserRepository
from core.app.repositories.teachers_questionnaire_repository import QuestionnaireTeacherRepository
from core.app.services.types import QuestionnaireTeacherData
from core.models import User, QuestionnaireTeacher


class QuestionnaireTeacherRegister:
    teachers_repository = QuestionnaireTeacherRepository()
    user_repository = UserRepository()

    def __init__(self, user: User, data: QuestionnaireTeacherData):
        self.questionnaire = None
        self.data = data
        self.user = user

    @cached_property
    def check_user(self) -> QuestionnaireTeacher:
        user_role = self.teachers_repository.check_user_by_roles(roles=self.data["roles"])
        if user_role.roles != 'STUDENT':
            raise NotAcceptable(f"This field must be an STUDENT, not be a {self.data['roles']}")

        questionnaire = QuestionnaireTeacher()
        questionnaire.name = self.data['name']
        questionnaire.surname = self.data['surname']
        questionnaire.date_of_birth = self.data['date_of_birth']
        questionnaire.gender = self.data['gender']
        questionnaire.about_me = self.data['about_me']
        questionnaire.work_experience = self.data['work_experience']
        questionnaire.vk_link = self.data['vk_link']
        questionnaire.telegram_link = self.data['telegram_link']
        questionnaire.certificate_photos = self.data['certificate_photos']
        questionnaire.passport_photo = self.data['passport_photo']
        questionnaire.user_photo = self.data['user_photo']

        self.teachers_repository.store(questionnaire=questionnaire)
        return questionnaire

    def create_questionnaire(self) -> QuestionnaireTeacher:
        return self.questionnaire
