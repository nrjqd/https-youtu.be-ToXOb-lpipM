"""create posts table

Revision ID: 6e11c9e5b434
Revises: 
Create Date: 2022-11-25 12:58:42.038042

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e11c9e5b434'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Colum('id', sa.Integer(),nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
