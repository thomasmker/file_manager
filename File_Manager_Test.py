import unittest
import os
import shutil
from File_Manager import FileManager


class MyTestCase(unittest.TestCase):
    def test_should_remove_prefix_and_suffix_from_all_files_in_the_directory(self):
        prefix = "prefix_"
        suffix = "_suffix"
        path = "test_prefix_suffix"

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = []
        for file in desired_file_names:
            filename, extension = FileManager.get_filename_and_extension(file)
            files.append(f"{prefix}{filename}{suffix}{extension}")

        file_paths = [os.path.join(path, file) for file in files]
        [open(file, "a").close() for file in file_paths]

        # Renaming the files
        file_manager = FileManager(path, prefix, suffix)
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        shutil.rmtree(path)

    def test_should_remove_prefix_from_all_files_in_the_directory(self):
        path = "test_prefix"
        prefix = "prefix_"

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = []
        for file in desired_file_names:
            filename, extension = FileManager.get_filename_and_extension(file)
            files.append(f"{prefix}{filename}{extension}")

        file_paths = [os.path.join(path, file) for file in files]
        [open(file, "a").close() for file in file_paths]

        # Renaming the files
        file_manager = FileManager(path, prefix)
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        shutil.rmtree(path)

    def test_should_remove_suffix_from_all_files_in_the_directory(self):
        path = "test_suffix"
        suffix = "_suffix"

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)

        # Creating the files
        desired_file_names = {"01.txt", "02.txt"}
        files = []
        for file in desired_file_names:
            filename, extension = FileManager.get_filename_and_extension(file)
            files.append(f"{filename}{suffix}{extension}")

        file_paths = [os.path.join(path, file) for file in files]
        [open(file, "a").close() for file in file_paths]

        # Renaming the files
        file_manager = FileManager(path, "",suffix)
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        shutil.rmtree(path)

    def test_should_remove_prefix_and_suffix_from_all_files_without_extension_in_the_directory(self):
        prefix = "prefix_"
        suffix = "_suffix"
        path = "test_prefix_suffix_extension"

        if not os.path.exists(path):
            os.makedirs(path)
        else:
            shutil.rmtree(path)

        # Creating the files
        desired_file_names = {"01", "02"}
        files = []
        for file in desired_file_names:
            filename, extension = FileManager.get_filename_and_extension(file)
            files.append(f"{prefix}{filename}{suffix}{extension}")

        file_paths = [os.path.join(path, file) for file in files]
        [open(file, "a").close() for file in file_paths]

        # Renaming the files
        file_manager = FileManager(path, prefix, suffix)
        file_manager.remove_prefix_suffix()

        # Checking the result
        renamed_files = file_manager.get_directory_files()

        self.assertEqual(desired_file_names == set(renamed_files), True)

        # Removing the directory and its content
        shutil.rmtree(path)

    def test_do_not_allow_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            file_manager = FileManager("an invalid path name")


if __name__ == '__main__':
    unittest.main()
