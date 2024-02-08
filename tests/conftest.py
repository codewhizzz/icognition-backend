# conftest.py
import pytest
import os

def pytest_configure(config):
    if not os.getenv('DATABASE_URL'):
        setattr(config.option, 'markexpr', 'not requires_database')

# test_app.py
import pytest

@pytest.mark.requires_database
def test_function_that_requires_database():
    # Your test code that requires DATABASE_URL

