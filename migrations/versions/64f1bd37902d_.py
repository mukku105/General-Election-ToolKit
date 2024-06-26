"""empty message

Revision ID: 64f1bd37902d
Revises: 6330cdd7519d
Create Date: 2024-04-08 16:17:46.656370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64f1bd37902d'
down_revision = '6330cdd7519d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('polling_station', schema=None) as batch_op:
        batch_op.add_column(sa.Column('part_no', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('polling_station', schema=None) as batch_op:
        batch_op.drop_column('part_no')

    # ### end Alembic commands ###
