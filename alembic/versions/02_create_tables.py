# alembic/versions/0002_create_tables.py
"""create tables

Revision ID: 0002_create_tables
Revises: 0001_create_db
Create Date: 2025-09-02 00:01:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0002_create_tables'
down_revision = '0001_create_db'
branch_labels = None
depends_on = None

def upgrade():
    # users
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('role', sa.String(length=20), nullable=False),
    )

    # menu_items
    op.create_table(
        'menu_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
    )

    # inventory
    op.create_table(
        'inventory',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('menu_item_id', sa.Integer(), sa.ForeignKey('menu_items.id'), nullable=False, unique=True),
        sa.Column('initial_qty', sa.Integer(), nullable=False, server_default="70"),
        sa.Column('qty_sold', sa.Integer(), nullable=False, server_default="0"),
    )

    # orders
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('menu_item_id', sa.Integer(), sa.ForeignKey('menu_items.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('orders')
    op.drop_table('inventory')
    op.drop_table('menu_items')
    op.drop_table('users')
