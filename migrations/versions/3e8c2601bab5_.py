"""empty message

Revision ID: 3e8c2601bab5
Revises: 405641286f00
Create Date: 2022-04-11 00:43:16.574517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e8c2601bab5'
down_revision = '405641286f00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('menu',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itemtype', sa.String(length=80), nullable=True),
    sa.Column('itemtitle1', sa.String(length=200), nullable=True),
    sa.Column('itemtitle2', sa.String(length=200), nullable=True),
    sa.Column('itemprice1', sa.Integer(), nullable=True),
    sa.Column('itemprice2', sa.Integer(), nullable=True),
    sa.Column('itemdiscription', sa.String(length=1000), nullable=True),
    sa.Column('itemadditionaldetails', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('menu')
    # ### end Alembic commands ###
