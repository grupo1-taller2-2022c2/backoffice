import datetime
import os
from fastapi import APIRouter, Depends, HTTPException, status, Query
from starlette import status
import requests
from app.database import SessionLocal, get_db
from app.cruds import metrics_cruds

router = APIRouter()
url_base = os.getenv('USERS_BASE_URL')


def check_correct_method(method):
    if method not in ["mailpassword", "federatedidentity"]:
        raise HTTPException(
            status_code=409, detail="method must be mailpassword or federatedidentity")


# ------------Endpoints for Users microservice (to update counters))-----------------

@router.post("/registrations", status_code=status.HTTP_200_OK)
def add_one_to_registration_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                                  db: SessionLocal = Depends(get_db)):
    check_correct_method(method)

    return metrics_cruds.add_registration(method, db)


@router.post("/logins", status_code=status.HTTP_200_OK)
def add_one_to_login_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                           db: SessionLocal = Depends(get_db)):
    check_correct_method(method)

    return metrics_cruds.add_login(method, db)


# ------------Endpoints for frontend (to display metrics)-----------------

# e.g. /registrations?method=mailpassword
@router.get("/registrations", status_code=status.HTTP_200_OK)
def get_registrations_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                            from_date: datetime.date = datetime.date.today(),  db: SessionLocal = Depends(get_db)):
    check_correct_method(method)

    return metrics_cruds.count_registrations(method, from_date, db)


@router.get("/logins", status_code=status.HTTP_200_OK)
def get_logins_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                     from_date: datetime.date = datetime.date.today(),  db: SessionLocal = Depends(get_db)):
    check_correct_method(method)

    return metrics_cruds.count_logins(method, from_date, db)


@router.get("/blocked_users", status_code=status.HTTP_200_OK)
def get_current_blocked_users_count():
    url = url_base + "/users/blocked"
    response = requests.get(url=url)
    if response.ok:
        return response.json()
    raise HTTPException(status_code=response.status_code,
                        detail=response.json()['detail'])
