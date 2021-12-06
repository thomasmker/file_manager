import pytest
from File_Manager import FileManager


@pytest.fixture
def prefix():
    return "prefix_"


@pytest.fixture
def suffix():
    return "_suffix"


def test_should_remove_prefix_and_suffix_from_all_files_in_the_directory(prefix, suffix):
    path = "test_prefix_suffix"

    file_manager = FileManager(path)
    file_manager.prefix = prefix
    file_manager.suffix = suffix

    file_manager.clean_directory()

    # Creating the files
    desired_file_names = {"01.txt", "02.txt"}
    files = file_manager.add_prefix_to_files(desired_file_names)
    files = file_manager.add_suffix_to_files(files)
    file_manager.create_empty_files(files)

    # Renaming the files
    file_manager.remove_prefix_suffix()

    # Checking the result
    renamed_files = file_manager.get_directory_files()

    assert desired_file_names == set(renamed_files)

    # Removing the directory and its content
    file_manager.remove_directory_and_contents()


def test_should_remove_prefix_from_all_files_in_the_directory(prefix):
    path = "test_prefix"

    file_manager = FileManager(path)
    file_manager.prefix = prefix

    file_manager.clean_directory()

    # Creating the files
    desired_file_names = {"01.txt", "02.txt"}
    files = file_manager.add_prefix_to_files(desired_file_names)
    file_manager.create_empty_files(files)

    # Renaming the files
    file_manager.remove_prefix_suffix()

    # Checking the result
    renamed_files = file_manager.get_directory_files()

    assert desired_file_names == set(renamed_files)

    # Removing the directory and its content
    file_manager.remove_directory_and_contents()


def test_should_remove_suffix_from_all_files_in_the_directory(suffix):
    path = "test_suffix"

    file_manager = FileManager(path)
    file_manager.suffix = suffix

    file_manager.clean_directory()

    # Creating the files
    desired_file_names = {"01.txt", "02.txt"}
    files = file_manager.add_suffix_to_files(desired_file_names)
    file_manager.create_empty_files(files)

    # Renaming the files
    file_manager.remove_prefix_suffix()

    # Checking the result
    renamed_files = file_manager.get_directory_files()

    assert desired_file_names == set(renamed_files)

    # Removing the directory and its content
    file_manager.remove_directory_and_contents()


def test_do_not_allow_invalid_path():
    with pytest.raises(FileNotFoundError):
        file_manager = FileManager("an invalid path name")
        file_manager.remove_prefix_suffix()
