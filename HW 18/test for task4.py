import pytest
from homework6_assignment import create_and_write_files, change_file_content

@pytest.fixture
def temporary_binary_files(tmp_path):
    file1_path = tmp_path / 'file1.bin'
    file2_path = tmp_path / 'file2.bin'
    return file1_path, file2_path

def test_create_and_write_files(temporary_binary_files):
    file1_path, file2_path = temporary_binary_files

    create_and_write_files()

    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        data1 = file1.read()
        data2 = file2.read()

    assert len(data1) == 10
    assert len(data2) == 10

def test_change_file_content(temporary_binary_files):
    file1_path, file2_path = temporary_binary_files

    create_and_write_files()

    data1_before_change, data2_before_change = None, None

    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        data1_before_change = file1.read()
        data2_before_change = file2.read()

    change_file_content()

    data1_after_change, data2_after_change = None, None

    with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
        data1_after_change = file1.read()
        data2_after_change = file2.read()

    assert data1_after_change == data2_before_change
    assert data2_after_change == data1_before_change