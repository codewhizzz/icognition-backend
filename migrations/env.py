import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlmodel import SQLModel
from alembic import context

# Import your models here so Alembic can find them
from app.models import Bookmark, Document, Entity

# Automatically load .env file if present
from dotenv import load_dotenv
load_dotenv()

# Use DATABASE_URL from environment variable if available, otherwise fall back to LOCAL_PSQL from .env
connection_string = os.getenv('DATABASE_URL', os.getenv('LOCAL_PSQL'))

config = context.config

# Override the sqlalchemy.url in alembic.ini with the connection string from the environment
config.set_main_option('sqlalchemy.url', connection_string)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option('sqlalchemy.url')
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={'paramstyle': 'named'},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Here, instead of using the config file's settings directly,
    # we ensure the connection string from the environment is used.
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=connection_string  # Ensure this uses the dynamic connection string
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

