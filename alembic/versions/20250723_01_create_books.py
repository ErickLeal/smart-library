"""create books table

Revision ID: 20250723_01
Revises: 
Create Date: 2025-07-23
"""
revision = '20250723_01'
down_revision = None
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'books',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('author', sa.String, nullable=False),
        sa.Column('year', sa.Integer, nullable=False),
        sa.Column('pages', sa.Integer, nullable=False, server_default='0'),
        sa.Column('is_old', sa.Boolean, nullable=False, server_default=sa.text('false')),
        sa.Column('is_big', sa.Boolean, nullable=False, server_default=sa.text('false')),
    )

def downgrade():
    op.drop_table('books')
