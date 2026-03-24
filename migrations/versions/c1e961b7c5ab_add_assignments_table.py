"""add assignments table

Revision ID: c1e961b7c5ab
Revises: 
Create Date: 2026-03-23 21:50:16.734694

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1e961b7c5ab'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('assignments')
