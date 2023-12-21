from pydantic import BaseModel


class UsersItem(BaseModel):
    created_at: str
    description: str
