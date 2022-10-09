from fastapi import APIRouter, Depends, HTTPException
from app.schemas import admin_schemas
from app.helpers.admin_helpers import hash_password
from app.cruds import admin_cruds
from app.database import SessionLocal, get_db
from typing import List
from starlette import status


router = APIRouter()


@router.get("/", response_model=List[admin_schemas.AdminSchema], status_code=status.HTTP_200_OK)
def get_admins(db: SessionLocal = Depends(get_db)):
    return admin_cruds.get_admins_from_db(db)


@router.post("/grantaccess", response_model=admin_schemas.AdminSchema, status_code=status.HTTP_200_OK)
def grant_access(admin: admin_schemas.AdminSignInSchema, db: SessionLocal = Depends(get_db)):
    admin_from_db = admin_cruds.get_admin_by_email(admin.email, db)
    if not admin_from_db or (admin_from_db.password != hash_password(admin.password)):
        raise HTTPException(
            status_code=403, detail="Incorrect mail or password")

    return admin_schemas.AdminSchema.from_orm(admin_from_db)
