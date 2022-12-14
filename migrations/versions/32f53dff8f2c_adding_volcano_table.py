"""Adding volcano table

Revision ID: 32f53dff8f2c
Revises: 
Create Date: 2022-09-25 15:41:49.889980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f53dff8f2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('volcano',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('height', sa.String(length=30), nullable=True),
    sa.Column('last_eruption', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_volcano_name'), 'volcano', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_volcano_name'), table_name='volcano')
    op.drop_table('volcano')
    # ### end Alembic commands ###
