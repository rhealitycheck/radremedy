"""Adding model for news posts.

Revision ID: 1726eb3f34a5
Revises: 58620e8a20f9
Create Date: 2016-02-29 23:06:23.028000

"""

# revision identifiers, used by Alembic.
revision = '1726eb3f34a5'
down_revision = '58620e8a20f9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.Unicode(length=500), nullable=False),
    sa.Column('author', sa.Unicode(length=500), nullable=False),
    sa.Column('summary', sa.UnicodeText(), nullable=False),
    sa.Column('body', sa.UnicodeText(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('visible', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    ### end Alembic commands ###
