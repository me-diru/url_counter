"""empty message

Revision ID: 6792a13ab299
Revises: 
Create Date: 2020-09-25 18:46:28.625868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6792a13ab299'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('url',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=64), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_url_count'), 'url', ['count'], unique=True)
    op.create_index(op.f('ix_url_url'), 'url', ['url'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_url_url'), table_name='url')
    op.drop_index(op.f('ix_url_count'), table_name='url')
    op.drop_table('url')
    # ### end Alembic commands ###
