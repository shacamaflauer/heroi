"""empty message

Revision ID: 0a65571c1019
Revises: 
Create Date: 2020-04-06 23:01:36.417544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a65571c1019'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_pessoa', sa.String(), nullable=True),
    sa.Column('cpf_pessoa', sa.String(length=11), nullable=True),
    sa.Column('endereco', sa.String(), nullable=True),
    sa.Column('numero', sa.String(), nullable=True),
    sa.Column('bairro', sa.String(), nullable=True),
    sa.Column('cidade', sa.String(), nullable=True),
    sa.Column('celular', sa.String(), nullable=True),
    sa.Column('senha', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf_pessoa')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
