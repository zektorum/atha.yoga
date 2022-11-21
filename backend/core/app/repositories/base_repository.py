from abc import ABC

from django.db.models import Model


class BaseRepository(ABC):
    model: Model
