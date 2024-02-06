# conftest.py in your tests directory

import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def create_test_data_dir():
    os.makedirs("tests/data/", exist_ok=True)
    # You can also populate the directory with necessary files here

