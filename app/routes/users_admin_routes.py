import json
import os
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import requests
from starlette import status
from app.schemas import admin_schemas, user_schemas
from pydantic import EmailStr

router = APIRouter()
url_base = os.getenv('USERS_BASE_URL')


@router.get("/", response_model=List[user_schemas.UserSchema], status_code=status.HTTP_200_OK)
def get_users():
    url = url_base + "/users/"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.get("/passengers/{user_email}", response_model=user_schemas.PassengerSelfProfile, status_code=status.HTTP_200_OK)
def get_passenger_profile(user_email: EmailStr):
    # We use the /me to get the complete profile and not just the public fields
    url = url_base + "/passengers/me/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
