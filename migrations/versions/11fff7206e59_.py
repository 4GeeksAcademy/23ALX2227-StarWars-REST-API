"""empty message

Revision ID: 11fff7206e59
Revises: a5cffa318ac2
Create Date: 2023-11-25 01:50:57.810049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11fff7206e59'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('eye_color', sa.String(length=80), nullable=False),
    sa.Column('hair_color', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('created', sa.String(length=80), nullable=False),
    sa.Column('edited', sa.String(length=80), nullable=False),
    sa.Column('producer', sa.String(length=80), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('director', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gravity', sa.String(length=80), nullable=False),
    sa.Column('clima', sa.String(length=80), nullable=False),
    sa.Column('poblation', sa.String(length=80), nullable=False),
    sa.Column('rotation_period', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('films_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['films_id'], ['films.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('planet')
    op.drop_table('films')
    op.drop_table('character')
    # ### end Alembic commands ###