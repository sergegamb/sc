from pydantic import BaseModel


class Technician(BaseModel):
    name: str
    username: str
    email: str
    id: int
