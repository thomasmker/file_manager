import argparse
from File_Manager import FileManager


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-path', help="the path folder", type=str)
    parser.add_argument('--prefix', '-p', help="the prefix to be removed", type=str, default="")
    parser.add_argument('--suffix', '-s', help="the suffix to be removed", type=str, default="")
    args = parser.parse_args()
    return args.path, args.prefix, args.suffix


def main():
    path, prefix, suffix = get_args()
    file_manager = FileManager(path)
    file_manager.prefix = prefix
    file_manager.suffix = suffix
    file_manager.remove_prefix_suffix()
    return


if __name__ == '__main__':
    FileManager.get_directory_files("1")

    # main()
