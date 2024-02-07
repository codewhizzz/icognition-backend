# tests/conftest.py
import os
import pytest

@pytest.fixture(scope='session', autouse=True)
def set_env_variables():
    # Assuming these are your desired test environment settings
    os.environ['ENVIRONMENT'] = 'staging'  # Or 'production', as needed
    os.environ['DATABASE_URL'] = 'your_test_database_url_here'

    yield  # Allows tests to run with these environment settings

    # Optional: Clear or reset environment variables after tests complete
    # os.environ.pop('ENVIRONMENT')
    # os.environ.pop('DATABASE_URL')

