from pydantic import BaseModel, EmailStr


class AdminSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str

    class Config:
        orm_mode = True
