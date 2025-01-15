"""empty message

Revision ID: d3784a8b54e4
Revises: 
Create Date: 2024-12-10 13:37:20.667439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3784a8b54e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Verificar se a coluna já existe
    from sqlalchemy import inspect
    inspector = inspect(op.get_bind())
    columns = [column['name'] for column in inspector.get_columns('items')]

    if 'description' not in columns:
        with op.batch_alter_table('items', schema=None) as batch_op:
            batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

def downgrade():
    # Remover a coluna 'description' durante o downgrade
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')