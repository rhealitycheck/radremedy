"""Adding Review.ip column

Revision ID: b511e51f3a0
Revises: 15ba1cfb5eef
Create Date: 2015-06-06 23:52:39.478000

"""

# revision identifiers, used by Alembic.
revision = 'b511e51f3a0'
down_revision = '15ba1cfb5eef'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('ip', sa.Unicode(length=45), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'ip')
    ### end Alembic commands ###
