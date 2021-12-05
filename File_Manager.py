from os import listdir, rename
from os.path import isdir, isfile, join, splitext


class FileManager:
    def __init__(self, path, prefix="", suffix=""):
        self.path = path
        self.prefix = prefix
        self.suffix = suffix
        self.validate_path()

    def remove_prefix_suffix(self):
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
        return filename.removeprefix(self.prefix) if self.prefix else filename

    def remove_suffix(self, filename):
        return filename.removesuffix(self.suffix) if self.suffix else filename

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
