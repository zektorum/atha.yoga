from typing import Optional


from core.app.repositories.base_repository import BaseRepository
from core.models import QuestionnaireTeacher, User


class QuestionnaireTeacherRepository(BaseRepository):
    model = QuestionnaireTeacher()

    def store(self, questionnaire: QuestionnaireTeacher) -> None:
        questionnaire.save()

    def check_user_by_roles(self, roles: str) -> Optional[User]:
        user = User.objects.filter(roles=roles)
        return user
