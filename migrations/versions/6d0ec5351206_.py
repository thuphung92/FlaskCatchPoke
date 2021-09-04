"""empty message

Revision ID: 6d0ec5351206
Revises: 6b81b8c14f07
Create Date: 2021-09-03 19:55:05.007916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d0ec5351206'
down_revision = '6b81b8c14f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catched', sa.Column('catched_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('catched', 'catched_on')
    # ### end Alembic commands ###