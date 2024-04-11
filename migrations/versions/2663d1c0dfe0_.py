"""empty message

Revision ID: 2663d1c0dfe0
Revises: 9ce55567e93e
Create Date: 2024-04-10 10:19:47.229126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2663d1c0dfe0'
down_revision = '9ce55567e93e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ps_election_officer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_polling_station_code', sa.String(length=12), nullable=True),
    sa.Column('presiding_officer', sa.String(length=150), nullable=True),
    sa.Column('polling_officer_1', sa.String(length=150), nullable=True),
    sa.Column('micro_observers', sa.String(length=150), nullable=True),
    sa.Column('block_level_officer', sa.String(length=150), nullable=True),
    sa.Column('remarks', sa.String(length=150), nullable=True),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['fk_polling_station_code'], ['polling_station.ps_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ps_election_officer')
    # ### end Alembic commands ###
