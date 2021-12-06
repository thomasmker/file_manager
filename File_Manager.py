from os import listdir, rename, makedirs
from os.path import isdir, isfile, join, splitext, exists
import shutil


class FileManager:
    def __init__(self, path):
        self.path = path
        self._prefix = ""
        self._suffix = ""

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        self._prefix = prefix

    @property
    def suffix(self):
        return self.suffix

    @suffix.setter
    def suffix(self, suffix):
        self._suffix = suffix

    def remove_prefix_suffix(self):
        self.validate_path()

        files = self.get_directory_files()

        for file in files:
            filename, extension = self.get_filename_and_extension(file)

            filename = self.remove_prefix(filename)
            filename = self.remove_suffix(filename)

            old_file = join(self.path, file)
            new_file = join(self.path, filename + extension)

            rename(old_file, new_file)

        print("Success")

    def remove_prefix(self, filename):
        return filename.removeprefix(self._prefix) if self._prefix else filename

    def remove_suffix(self, filename):
        return filename.removesuffix(self._suffix) if self._suffix else filename

    def validate_path(self):
        if not isdir(self.path):
            raise FileNotFoundError(f'The path {self.path} is not a valid directory')

    @staticmethod
    def get_filename_and_extension(file):
        split_filename = splitext(file)
        filename_args_size = len(split_filename)
        filename = split_filename[0] if filename_args_size > 0 else file
        extension = split_filename[1] if filename_args_size > 1 else ""
        return filename, extension

    def get_directory_files(self):
        return [f for f in listdir(self.path) if isfile(join(self.path, f))]

    def directory_exists(self):
        return exists(self.path)

    def create_directory(self):
        if not self.directory_exists():
            makedirs(self.path)

    def remove_directory_and_contents(self):
        if self.directory_exists():
            shutil.rmtree(self.path)

    def clean_directory(self):
        self.remove_directory_and_contents()
        self.create_directory()

    def add_prefix_to_files(self, filenames):
        return [f"{self._prefix}{file}" for file in filenames]

    def add_suffix_to_files(self, filenames):
        renamed_files = []
        for file in filenames:
            filename, extension = FileManager.get_filename_and_extension(file)
            renamed_files.append(f"{filename}{self._suffix}{extension}")
        return renamed_files

    def create_empty_files(self, files):
        file_paths = [join(self.path, file) for file in files]
        [open(file, "a").close() for file in file_paths]