"""fill out fix table

Revision ID: c95c4545491e
Revises: 06ea8c057d9f
Create Date: 2021-03-10 11:52:24.711555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c95c4545491e'
down_revision = '06ea8c057d9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fix', sa.Column('Accuracy', sa.Float(), nullable=True))
    op.add_column('fix', sa.Column('Altitude', sa.Float(), nullable=True))
    op.add_column('fix', sa.Column('Latitude', sa.Float(), nullable=True))
    op.add_column('fix', sa.Column('Longitude', sa.Float(), nullable=True))
    op.add_column('fix', sa.Column('MeasurementDateTime', sa.DateTime(), nullable=True))
    op.add_column('fix', sa.Column('Provider', sa.String(length=80), nullable=True))
    op.add_column('fix', sa.Column('Speed', sa.Float(), nullable=True))
    op.add_column('fix', sa.Column('UTCTimeInMs', sa.BigInteger(), nullable=True))
    op.add_column('fix', sa.Column('UploadDateTime', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_fix_Latitude'), 'fix', ['Latitude'], unique=False)
    op.create_index(op.f('ix_fix_Longitude'), 'fix', ['Longitude'], unique=False)
    op.create_index(op.f('ix_fix_MeasurementDateTime'), 'fix', ['MeasurementDateTime'], unique=False)
    op.create_index(op.f('ix_fix_UTCTimeInMs'), 'fix', ['UTCTimeInMs'], unique=False)
    op.create_index(op.f('ix_fix_UploadDateTime'), 'fix', ['UploadDateTime'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_fix_UploadDateTime'), table_name='fix')
    op.drop_index(op.f('ix_fix_UTCTimeInMs'), table_name='fix')
    op.drop_index(op.f('ix_fix_MeasurementDateTime'), table_name='fix')
    op.drop_index(op.f('ix_fix_Longitude'), table_name='fix')
    op.drop_index(op.f('ix_fix_Latitude'), table_name='fix')
    op.drop_column('fix', 'UploadDateTime')
    op.drop_column('fix', 'UTCTimeInMs')
    op.drop_column('fix', 'Speed')
    op.drop_column('fix', 'Provider')
    op.drop_column('fix', 'MeasurementDateTime')
    op.drop_column('fix', 'Longitude')
    op.drop_column('fix', 'Latitude')
    op.drop_column('fix', 'Altitude')
    op.drop_column('fix', 'Accuracy')
    # ### end Alembic commands ###