import app.models.metric_models as metric_models
from sqlalchemy.orm import Session
from fastapi import HTTPException


def add_registration(reg_mehtod: str, db: Session):
    db_reg = metric_models.Registration(
        method=reg_mehtod
    )
    try:
        db.add(db_reg)
        db.commit()
        db.refresh(db_reg)
        return 0
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
