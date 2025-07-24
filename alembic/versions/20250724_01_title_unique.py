"""add unique constraint to book title+author

Revision ID: 20250724_01
Revises: 20250723_01
Create Date: 2025-07-24
"""
revision = '20250724_01'
down_revision = '20250723_01'
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_unique_constraint('uq_books_title_author', 'books', ['title', 'author'])

def downgrade():
    op.drop_constraint('uq_books_title_author', 'books', type_='unique')
