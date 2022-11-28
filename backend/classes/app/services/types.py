from typing import TypedDict


class CommentCreateData(TypedDict):
    email: str
    text: str
    class_id: int
