from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str


class PassengerSelfProfile(BaseModel):
    email: str
    username: str
    surname: str
    ratings: float
