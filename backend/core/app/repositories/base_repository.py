from abc import ABC
from typing import Type

from django.db.models import Model


class BaseRepository(ABC):
    model: Type[Model]
