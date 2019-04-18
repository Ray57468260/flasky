"""empty message

Revision ID: 1069a3759b65
Revises: 2619d2a89e2a
Create Date: 2019-04-17 19:17:15.840128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1069a3759b65'
down_revision = '2619d2a89e2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('tiemstamp', sa.DateTime(), nullable=True),
    sa.Column('disabled', sa.Boolean(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_tiemstamp'), 'comments', ['tiemstamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_tiemstamp'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###