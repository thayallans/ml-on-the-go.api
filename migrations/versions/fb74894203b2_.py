"""empty message

Revision ID: fb74894203b2
Revises: 5e2bf06e2fcc
Create Date: 2019-07-06 11:28:29.353668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb74894203b2'
down_revision = '5e2bf06e2fcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accountinfo', sa.Column('spreadsheet_target', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accountinfo', 'spreadsheet_target')
    # ### end Alembic commands ###