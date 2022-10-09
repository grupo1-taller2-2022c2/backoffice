"""create admins table

Revision ID: cfb6d702dbd4
Revises: 
Create Date: 2022-10-09 14:35:58.109470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfb6d702dbd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('admins',
                    sa.Column('admin_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(length=50), nullable=False),
                    sa.Column('password', sa.String(
                        length=100), nullable=False),
                    sa.Column('username', sa.String(
                        length=50), nullable=False),
                    sa.Column('surname', sa.String(length=50), nullable=False),
                    sa.PrimaryKeyConstraint('admin_id')
                    )


def downgrade() -> None:
    op.drop_table('admins')
