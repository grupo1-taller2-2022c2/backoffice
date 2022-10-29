"""logins table created

Revision ID: b1ee83b3c611
Revises: 183a4c05dec3
Create Date: 2022-10-29 20:22:10.337604

"""
from alembic import op
import sqlalchemy as sa
from app.models.metric_models import Login
from datetime import datetime, timedelta


# revision identifiers, used by Alembic.
revision = 'b1ee83b3c611'
down_revision = '183a4c05dec3'
branch_labels = None
depends_on = None

today = datetime.today()
yesterday = today - timedelta(days=1)
one_week_ago = today - timedelta(days=7)
one_month_ago = today - timedelta(days=30)
three_months_ago = today - timedelta(days=90)


def upgrade() -> None:
    op.create_table('logins',
                    sa.Column('login_id', sa.Integer(),
                              autoincrement=True, nullable=False),
                    sa.Column('method', sa.String(length=50), nullable=False),
                    sa.Column('login_date', sa.Date(), server_default=sa.text(
                        'CURRENT_DATE'), nullable=True),
                    sa.PrimaryKeyConstraint('login_id')
                    )

    op.bulk_insert(Login.__table__,
                   [
                       {'method': 'federatedidentity',
                           'login_date': yesterday},
                       {'method': 'mailpassword',
                           'login_date': yesterday},
                       {'method': 'mailpassword', 'login_date': one_week_ago},
                       {'method': 'mailpassword',
                           'login_date': one_week_ago},
                       {'method': 'federatedidentity',
                           'login_date': one_month_ago}
                   ])


def downgrade() -> None:
    op.drop_table('logins')
