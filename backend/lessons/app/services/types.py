from typing import TypedDict


class CommentCreateData(TypedDict):
    text: str
    lesson_id: int
