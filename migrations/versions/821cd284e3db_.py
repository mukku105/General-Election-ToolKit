"""empty message

Revision ID: 821cd284e3db
Revises: d9f91a35a1e8
Create Date: 2024-04-08 14:28:17.502030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '821cd284e3db'
down_revision = 'd9f91a35a1e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('polling_station', schema=None) as batch_op:
        batch_op.add_column(sa.Column('ac_no', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('polling_station', schema=None) as batch_op:
        batch_op.drop_column('ac_no')

    # ### end Alembic commands ###
