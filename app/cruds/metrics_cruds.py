from app.models.metric_models import Registration
from sqlalchemy.orm import Session
from fastapi import HTTPException
import datetime


def add_registration(reg_mehtod: str, db: Session):
    db_reg = Registration(
        method=reg_mehtod
    )
    try:
        db.add(db_reg)
        db.commit()
        db.refresh(db_reg)
        return 0
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


def count_registrations(method: str, date_from: datetime.date, db: Session):
    return db.query(Registration).filter(Registration.method.like(method), Registration.date_registered >= date_from).count()
