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
wallets_url_base = os.getenv('WALLETS_BASE_URL')


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


@router.get("/drivers/{user_email}", response_model=user_schemas.DriverSelfProfile, status_code=status.HTTP_200_OK)
def get_driver_profile(user_email: EmailStr):
    # We use the /me to get the complete profile and not just the public fields
    url = url_base + "/drivers/me/" + user_email
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.post("/blocked/{user_email}", status_code=status.HTTP_200_OK)
def block_user(user_email: EmailStr):
    url = url_base + "/users/blocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.post("/unblocked/{user_email}", status_code=status.HTTP_200_OK)
def unblock_user(user_email: EmailStr):
    url = url_base + "/users/unblocked/" + user_email
    response = requests.post(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


@router.post("/{user_email}/wallet/deposit", status_code=status.HTTP_200_OK)
def deposit_funds_in_user_wallet(user_email: EmailStr, deposit_funds: user_schemas.DepositFundsSchema):
    user_id = get_user_id_from_email(user_email)
    url = wallets_url_base + "/transfers/system"
    body = {
        'receiver_user_id': user_id,
        'amount_in_ethers': deposit_funds.amount_in_ethers
    }
    response = requests.post(url=url, json=body)

    if response.ok:
        return response.json()

    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])


############## AUX ##############
def get_user_id_from_email(email):
    url = url_base + "/users/" + email + "/id"
    response = requests.get(url=url)
    if response.ok:
        print(response.text)
        return int(response.text)

    raise HTTPException(status_code=response.status_code,
                        detail=response.json())
