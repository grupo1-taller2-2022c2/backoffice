from app.models.metric_models import Registration, Login
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


def add_login(login_mehtod: str, db: Session):
    db_login = Login(
        method=login_mehtod
    )
    try:
        db.add(db_login)
        db.commit()
        db.refresh(db_login)
        return 0
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


def count_logins(method: str, date_from: datetime.date, db: Session):
    return db.query(Login).filter(Login.method.like(method), Login.login_date >= date_from).count()
