import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def create_test_data_dir():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    # Optionally, populate the directory with needed files
    # Example: Create a dummy file
    with open(os.path.join(data_dir, 'dummy_file.txt'), 'w') as file:
        file.write('Dummy content')

