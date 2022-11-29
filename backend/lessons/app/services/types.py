from typing import TypedDict


class CommentCreateData(TypedDict):
    email: str
    text: str
    lesson_id: int
