"""empty message

Revision ID: 82a835d4bc53
Revises: 2663d1c0dfe0
Create Date: 2024-04-10 19:39:31.138720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82a835d4bc53'
down_revision = '2663d1c0dfe0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voters_turnout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fk_polling_station_code', sa.String(length=12), nullable=True),
    sa.Column('turnout_male_1', sa.Integer(), nullable=True),
    sa.Column('turnout_female_1', sa.Integer(), nullable=True),
    sa.Column('turnout_other_1', sa.Integer(), nullable=True),
    sa.Column('turnout_male_2', sa.Integer(), nullable=True),
    sa.Column('turnout_female_2', sa.Integer(), nullable=True),
    sa.Column('turnout_other_2', sa.Integer(), nullable=True),
    sa.Column('turnout_male_3', sa.Integer(), nullable=True),
    sa.Column('turnout_female_3', sa.Integer(), nullable=True),
    sa.Column('turnout_other_3', sa.Integer(), nullable=True),
    sa.Column('turnout_male_4', sa.Integer(), nullable=True),
    sa.Column('turnout_female_4', sa.Integer(), nullable=True),
    sa.Column('turnout_other_4', sa.Integer(), nullable=True),
    sa.Column('turnout_male_5', sa.Integer(), nullable=True),
    sa.Column('turnout_female_5', sa.Integer(), nullable=True),
    sa.Column('turnout_other_5', sa.Integer(), nullable=True),
    sa.Column('turnout_male_6', sa.Integer(), nullable=True),
    sa.Column('turnout_female_6', sa.Integer(), nullable=True),
    sa.Column('turnout_other_6', sa.Integer(), nullable=True),
    sa.Column('turnout_male_sangha', sa.Integer(), nullable=True),
    sa.Column('turnout_female_sangha', sa.Integer(), nullable=True),
    sa.Column('turnout_other_sangha', sa.Integer(), nullable=True),
    sa.Column('remarks', sa.String(length=150), nullable=True),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.ForeignKeyConstraint(['fk_polling_station_code'], ['polling_station.ps_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voters_turnout')
    # ### end Alembic commands ###