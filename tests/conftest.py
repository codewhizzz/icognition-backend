# conftest.py
import pytest
import os

def pytest_configure(config):
    if not os.getenv('DATABASE_URL'):
        setattr(config.option, 'markexpr', 'not requires_database')

