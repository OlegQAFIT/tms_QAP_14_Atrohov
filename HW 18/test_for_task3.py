import pytest
from homework6_assignment import generate_and_process_numbers


@pytest.fixture
def temporary_file_edit(tmp_path):
    file_path = tmp_path / 'temporary_file.txt'
    return file_path


def test_generate_and_process_numbers(temporary_file_edit, tmp_path):
    generate_and_process_numbers(temporary_file_edit)

    with open(temporary_file_edit, 'r') as file:
        result = list(map(float, file.readlines()))

    assert len(result) == 10


def test_generate_and_process_numbers_with_no_numbers(temporary_file_edit, tmp_path):
    with pytest.raises(ValueError):
        generate_and_process_numbers(temporary_file_edit)
