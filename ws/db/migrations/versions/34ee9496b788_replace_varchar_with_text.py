"""replace VARCHAR with TEXT

Revision ID: 34ee9496b788
Revises: fa9c488d44e4
Create Date: 2018-08-15 11:00:18.647411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34ee9496b788'
down_revision = 'fa9c488d44e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('interwiki', 'iw_prefix',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.UnicodeText())
    op.alter_column('namespace_canonical', 'nsc_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.UnicodeText(),
               existing_nullable=False)
    op.alter_column('namespace_name', 'nsn_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.UnicodeText(),
               existing_nullable=False)
    op.alter_column('namespace_starname', 'nss_name',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.UnicodeText(),
               existing_nullable=False)
    op.alter_column('tag', 'tag_displayname',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.UnicodeText(),
               existing_nullable=False)
    op.alter_column('tag', 'tag_name',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.UnicodeText(),
               existing_nullable=False)
    op.alter_column('ws_sync', 'wss_key',
               existing_type=sa.VARCHAR(length=32),
               type_=sa.UnicodeText())
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ws_sync', 'wss_key',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=32))
    op.alter_column('tag', 'tag_name',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
    op.alter_column('tag', 'tag_displayname',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
    op.alter_column('namespace_starname', 'nss_name',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=32),
               existing_nullable=False)
    op.alter_column('namespace_name', 'nsn_name',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=32),
               existing_nullable=False)
    op.alter_column('namespace_canonical', 'nsc_name',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=32),
               existing_nullable=False)
    op.alter_column('interwiki', 'iw_prefix',
               existing_type=sa.UnicodeText(),
               type_=sa.VARCHAR(length=32))
    # ### end Alembic commands ###