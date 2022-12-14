"""insert values to tables

Revision ID: a1386c99d7a9
Revises: cfb6d702dbd4
Create Date: 2022-10-09 14:57:17.234791

"""
from app.models.admin_models import Admin
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a1386c99d7a9"
down_revision = "cfb6d702dbd4"
branch_labels = None
depends_on = "cfb6d702dbd4"


def upgrade() -> None:
    op.bulk_insert(
        Admin.__table__,
        [
            {
                "email": "admin1@gmail.com",
                "password": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                "username": "admin1",
                "surname": "pepe",
            },
            {
                "email": "admin2@gmail.com",
                "password": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
                "username": "admin2",
                "surname": "pancracio",
            },
        ],
    )


def downgrade() -> None:
    pass
