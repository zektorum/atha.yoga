from typing import Type, List

from core.app.repositories.base_repository import BaseRepository
from core.models import Attachment


class AttachmentRepository(BaseRepository):
    model = Attachment

    def __init__(self, model: Type[Attachment]) -> None:
        self.model = model

    def bulk_create(self, models: List[Attachment]) -> List[Attachment]:
        for model in models:
            model.save()
        return models
