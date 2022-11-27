from typing import TypedDict


class CommentAddData(TypedDict):
    email: str
    text: str
    class_id: int


class CommentsGetData(TypedDict):
    class_id: int
