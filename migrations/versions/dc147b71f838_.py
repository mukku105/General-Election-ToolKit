"""empty message

Revision ID: dc147b71f838
Revises: 64f1bd37902d
Create Date: 2024-04-08 17:52:45.574642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc147b71f838'
down_revision = '64f1bd37902d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assembly_const',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ac_no', sa.Integer(), nullable=False),
    sa.Column('ac_name', sa.String(length=150), nullable=True),
    sa.Column('ac_category', sa.String(length=150), nullable=True),
    sa.Column('remarks', sa.String(length=150), nullable=True),
    sa.Column('state', sa.String(length=150), nullable=True),
    sa.Column('district', sa.String(length=150), nullable=True),
    sa.Column('last_updated', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ac_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assembly_const')
    # ### end Alembic commands ###
