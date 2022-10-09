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
