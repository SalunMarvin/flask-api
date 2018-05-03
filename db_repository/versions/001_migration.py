from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
person = Table('person', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('reference_code', String(length=100), nullable=False),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime),
    Column('name', String(length=255)),
    Column('document_number', String(length=100)),
    Column('kind', String(length=100)),
    Column('avatar', String(length=255)),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('reference_code', String(length=100), nullable=False),
    Column('created_at', DateTime),
    Column('updated_at', DateTime),
    Column('deleted_at', DateTime),
    Column('email', String(length=100), nullable=False),
    Column('username', String(length=100)),
    Column('token', String(length=150)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['person'].drop()
    post_meta.tables['user'].drop()
