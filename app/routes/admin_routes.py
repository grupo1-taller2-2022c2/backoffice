from fastapi import APIRouter, Depends
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
