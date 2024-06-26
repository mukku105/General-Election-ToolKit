"""empty message

Revision ID: 6b6313731d2f
Revises: 48560d4c0afc
Create Date: 2024-04-12 15:06:27.828406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6313731d2f'
down_revision = '48560d4c0afc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voters_turnout', schema=None) as batch_op:
        batch_op.add_column(sa.Column('turnout_male_1_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_1_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_1_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_2_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_2_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_2_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_3_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_3_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_3_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_4_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_4_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_4_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_5_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_5_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_5_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_6_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_6_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_6_sangha', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_pc', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_female_pc', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_pc', sa.Integer(), nullable=True))
        batch_op.drop_column('turnout_male_sangha')
        batch_op.drop_column('turnout_other_sangha')
        batch_op.drop_column('turnout_female_sangha')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('voters_turnout', schema=None) as batch_op:
        batch_op.add_column(sa.Column('turnout_female_sangha', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('turnout_other_sangha', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('turnout_male_sangha', sa.INTEGER(), nullable=True))
        batch_op.drop_column('turnout_other_pc')
        batch_op.drop_column('turnout_female_pc')
        batch_op.drop_column('turnout_male_pc')
        batch_op.drop_column('turnout_other_6_sangha')
        batch_op.drop_column('turnout_female_6_sangha')
        batch_op.drop_column('turnout_male_6_sangha')
        batch_op.drop_column('turnout_other_5_sangha')
        batch_op.drop_column('turnout_female_5_sangha')
        batch_op.drop_column('turnout_male_5_sangha')
        batch_op.drop_column('turnout_other_4_sangha')
        batch_op.drop_column('turnout_female_4_sangha')
        batch_op.drop_column('turnout_male_4_sangha')
        batch_op.drop_column('turnout_other_3_sangha')
        batch_op.drop_column('turnout_female_3_sangha')
        batch_op.drop_column('turnout_male_3_sangha')
        batch_op.drop_column('turnout_other_2_sangha')
        batch_op.drop_column('turnout_female_2_sangha')
        batch_op.drop_column('turnout_male_2_sangha')
        batch_op.drop_column('turnout_other_1_sangha')
        batch_op.drop_column('turnout_female_1_sangha')
        batch_op.drop_column('turnout_male_1_sangha')

    # ### end Alembic commands ###
