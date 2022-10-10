import app.models.admin_models as admin_models
import app.schemas.admin_schemas as admin_schemas
from pydantic import EmailStr
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.helpers.admin_helpers import hash_password


def get_admins_from_db(db: Session):
    return db.query(admin_models.Admin).all()


def get_admin_by_email(admin_email: EmailStr, db: Session):
    return db.query(admin_models.Admin).filter(admin_models.Admin.email == admin_email).first()


def register_admin(admin: admin_schemas.AdminSignUpSchema, db: Session):
    db_admin = admin_models.Admin(
        email=admin.email,
        password=hash_password(admin.password),
        username=admin.username,
        surname=admin.surname,
    )
    try:
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return admin_schemas.AdminSchema.from_orm(db_admin)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
