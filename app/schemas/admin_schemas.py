from pydantic import BaseModel, EmailStr


class AdminSchema(BaseModel):
    email: EmailStr
    username: str
    surname: str

    class Config:
        orm_mode = True


class AdminSignInSchema(BaseModel):
    email: EmailStr
    password: str


class AdminSignUpSchema(BaseModel):
    email: EmailStr
    password: str
    username: str
    surname: str
