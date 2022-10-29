"""registrations table created

Revision ID: 183a4c05dec3
Revises: a1386c99d7a9
Create Date: 2022-10-28 03:51:46.591424

"""
from alembic import op
import sqlalchemy as sa
from app.models.metric_models import Registration
from datetime import datetime, timedelta

# revision identifiers, used by Alembic.
revision = '183a4c05dec3'
down_revision = 'a1386c99d7a9'
branch_labels = None
depends_on = None

today = datetime.today()
one_week_ago = today - timedelta(days=7)
one_month_ago = today - timedelta(days=30)
three_months_ago = today - timedelta(days=90)


def upgrade() -> None:
    op.create_table('registrations',
                    sa.Column('reg_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('method', sa.String(length=50), nullable=False),
                    sa.Column('date_registered', sa.Date(),
                              server_default=sa.text('CURRENT_DATE'), nullable=True),
                    sa.PrimaryKeyConstraint('reg_id')
                    )

    op.bulk_insert(Registration.__table__,
                   [
                       {'method': 'federatedidentity',
                           'date_registered': today},
                       {'method': 'mailpassword',
                           'date_registered': today},
                       {'method': 'mailpassword', 'date_registered': one_month_ago},
                       {'method': 'mailpassword',
                           'date_registered': three_months_ago},
                       {'method': 'federatedidentity',
                           'date_registered': three_months_ago}
                   ])


def downgrade() -> None:
    op.drop_table('registrations')
