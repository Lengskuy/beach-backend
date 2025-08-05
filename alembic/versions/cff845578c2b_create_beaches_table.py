"""Create beaches table with updated schema

Revision ID: cff845578c2b
Revises: 
Create Date: 2025-08-04 20:02:49.388395
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cff845578c2b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'beaches',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), index=True),
        sa.Column('temperature', sa.Float(), nullable=True),
        sa.Column('wave_height', sa.Float(), nullable=True),
        sa.Column('crowd_level', sa.String(), nullable=True),
        sa.Column('safety_flag', sa.String(), nullable=True),
        sa.Column('timestamp', sa.String(), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('beaches')
