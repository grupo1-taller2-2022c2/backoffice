import datetime
import os
from app.helpers.metric_helpers import RegistrationCounterFactory
from fastapi import APIRouter, Depends, HTTPException, status
from starlette import status
from app.database import SessionLocal, get_db
from app.cruds import metrics_cruds

router = APIRouter()
url_base = os.getenv('USERS_BASE_URL')

# Endpoints for Users microservice (to update counters)


@router.post("/registrations", status_code=status.HTTP_200_OK)
def add_one_to_registration_count(method: str = "mailpassword",  db: SessionLocal = Depends(get_db)):
    if method not in ["mailpassword", "federatedidentity"]:
        raise HTTPException(
            status_code=409, detail="method must be mailpassword or federatedidentity")

    return metrics_cruds.add_registration(method, db)


# Endpoints for frontend (to display metrics)

# e.g. /registrations?method=mailpassword
# response_model=List[metric_schemas.MetricSchema],
@router.get("/registrations", status_code=status.HTTP_200_OK)
def get_registrations_count(method: str = "mailpassword", from_date: datetime.date = datetime.date.today(),  db: SessionLocal = Depends(get_db)):
    try:
        return RegistrationCounterFactory.create_counter_for_method(
            method).count(db, from_date)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
