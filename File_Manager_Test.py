import unittest
from File_Manager import FileManager


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.prefix = "prefix_"
        self.suffix = "_suffix"

    def test_should_remove_prefix_and_suffix_from_all_files_in_the_directory(self):
        path = "test_prefix_suffix"

        file_manager = FileManager(path)
        file_manager.prefix = self.prefix
        file_manager.suffix = self.suffix

        file_manager.create_directory()

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = file_manager.add_prefix_to_files(desired_file_names)
        files = file_manager.add_suffix_to_files(files)
        file_manager.create_empty_files(files)

        # Renaming the files
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        file_manager.remove_directory_and_contents()

    def test_should_remove_prefix_from_all_files_in_the_directory(self):
        path = "test_prefix"

        file_manager = FileManager(path)
        file_manager.prefix = self.prefix

        file_manager.create_directory()

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = file_manager.add_prefix_to_files(desired_file_names)
        file_manager.create_empty_files(files)

        # Renaming the files
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        file_manager.remove_directory_and_contents()

    def test_should_remove_suffix_from_all_files_in_the_directory(self):
        path = "test_suffix"

        file_manager = FileManager(path)
        file_manager.suffix = self.suffix
        file_manager.create_directory()

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = file_manager.add_suffix_to_files(desired_file_names)
        file_manager.create_empty_files(files)

        # Renaming the files
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        file_manager.remove_directory_and_contents()

    def test_should_remove_prefix_and_suffix_from_all_files_without_extension_in_the_directory(self):
        path = "test_prefix_suffix_extension"

        file_manager = FileManager(path)
        file_manager.prefix = self.prefix
        file_manager.suffix = self.suffix

        file_manager.create_directory()

        # Creating the files
        desired_file_names = {"01", "02"}
        files = file_manager.add_prefix_to_files(desired_file_names)
        files = file_manager.add_suffix_to_files(files)
        file_manager.create_empty_files(files)

        # Renaming the files
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        file_manager.remove_directory_and_contents()

    def test_do_not_allow_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            file_manager = FileManager("an invalid path name")
            file_manager.remove_prefix_suffix()


if __name__ == '__main__':
    unittest.main()
