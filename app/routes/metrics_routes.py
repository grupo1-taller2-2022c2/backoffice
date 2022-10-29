import datetime
import os
from fastapi import APIRouter, Depends, HTTPException, status, Query
from starlette import status
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


# ------------Endpoints for frontend (to display metrics)-----------------

# e.g. /registrations?method=mailpassword
@router.get("/registrations", status_code=status.HTTP_200_OK)
def get_registrations_count(method: str = Query(default="mailpassword", description="Should be mailpassword or federatedidentity"),
                            from_date: datetime.date = datetime.date.today(),  db: SessionLocal = Depends(get_db)):
    check_correct_method(method)

    return metrics_cruds.count_registrations(method, from_date, db)
