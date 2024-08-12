"""Add triggers to vote

Revision ID: 25fb5109f156
Revises: e8363dc440c5
Create Date: 2024-08-12 10:30:01.438531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25fb5109f156'
down_revision: Union[str, None] = 'e8363dc440c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the trigger function
    op.execute("""
    CREATE OR REPLACE FUNCTION increment_vote_count()
    RETURNS TRIGGER AS $$
    BEGIN
        UPDATE comments
        SET vote_count = vote_count + 1
        WHERE comment_id = NEW.comment_id;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """)

    # Create the trigger
    op.execute("""
    CREATE TRIGGER increment_vote_count_trigger
    AFTER INSERT ON votes
    FOR EACH ROW
    EXECUTE FUNCTION increment_vote_count();
    """)


def downgrade() -> None:
     # Drop the trigger
    op.execute("""
    DROP TRIGGER IF EXISTS increment_vote_count_trigger ON votes;
    """)

    # Drop the trigger function
    op.execute("""
    DROP FUNCTION IF EXISTS increment_vote_count();
    """)
