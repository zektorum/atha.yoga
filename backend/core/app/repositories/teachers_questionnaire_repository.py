from core.app.repositories.base_repository import BaseRepository
from core.models import QuestionnaireTeacher, User, QuestionnaireTeacherStatuses


class QuestionnaireTeacherRepository(BaseRepository):
    model = QuestionnaireTeacher

    def store(self, questionnaire: QuestionnaireTeacher) -> None:
        questionnaire.save()

    def has_moderate_questionnaires(self, user: User) -> bool:
        return self.model.objects.filter(
            user_id=user.id,
            status__in=[
                QuestionnaireTeacherStatuses.MODERATION,
                QuestionnaireTeacherStatuses.ACCEPTED,
            ],
        )
