"""create db

evision ID: 284f22749a0b
Revises: 67f5d67aea55
Create Date: 2024-01-12 13:05:38.527277
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284f22749a0b'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')