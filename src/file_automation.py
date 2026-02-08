from pathlib import Path
import constants


def check_directory_is_valid(directory: Path):
    """Checks if a directory exists or not

    Args:
        directory (string): Path of a directory

    Returns:
        boolean: Provides True or False if directory exists
    """
    if str(directory) == '.':
        print("Error: An empty directory was provided")
        return False
    elif directory.is_dir():
        return True
    else:
        print(f"Error: Directory {directory} does not exist.")
        return False


def get_file_extension(file_path: Path):
    """Given a file's path, returns the extension of the file.

    Args:
        file_path (Path): Path of the file that has been requested to have its extension returned

    Returns:
        str: File's extension
    """
    char_to_find = "."
    path_as_string = file_path.as_posix()
    last_index = path_as_string.rfind(char_to_find)
    file_extension = path_as_string[last_index+1:]
    return file_extension.lower()


def get_file_name_from_path(file_path: Path):
    """Given a file's path, returns the file name

    Args:
        file_path (Path): Path of the file that has been requested to have its extension returned

    Returns:
        _type_: File's name
    """
    char_to_find = "/"
    path_as_string = file_path.as_posix()
    last_index = path_as_string.rfind(char_to_find)
    file_name = path_as_string[last_index+1:]
    return file_name


def get_source_directory():
    """Returns hard coded source directory from the constants.py file

    Returns:
        Path: Source directory from the constants.py file
    """
    return constants.source_directory


def get_destination_directory(file_extension: str):
    """Based on the file extension given, returns directory's path from constants.py

    Args:
        file_extension (str): Extension of a file, helped to determine which folder the file will be moved to

    Returns:
        Path: Path from the constants.py file
    """
    if file_extension in constants.list_apps:
        return constants.destination_directory_apps
    elif file_extension in constants.list_docs:
        return constants.destination_directory_docs
    elif file_extension in constants.list_images:
        return constants.destination_directory_images
    elif file_extension in constants.list_spreadsheets:
        return constants.destination_directory_spreadsheets
    elif file_extension in constants.list_videos:
        return constants.destination_directory_videos
    else:
        return constants.destination_directory_misc


def move_file(file_name: str, start_directory: Path, end_directory: Path):
    """Given a file path, moves that file from a source directory to a destination directory

    Args:
        file_name (str): File to be moved
        start_directory (Path): Source directory of the file
        end_directory (Path): Destination directory of the file

    Returns:
        str: Console message that could be used for testing purposes.
    """
    start_directory_full_path = start_directory / file_name
    end_directory_full_path = end_directory / file_name
    console_message = ""

    try:
        start_directory_full_path.rename(end_directory_full_path)
        console_message = f"Moved file '{file_name}' successfully to '{end_directory}'"
        print(console_message)
        return console_message
    except FileNotFoundError:
        console_message = f"Error: Source file '{file_name}' does not exist in directory '{start_directory}'"
        print(console_message)
        return console_message
    except PermissionError as e:
        console_message = "Permission error has occurred. Please adjust permission settings for file/destination and that the file is closed"
        print(console_message)
        return console_message
    except Exception as e:
        console_message = f"Unkown error has occured: {e}"
        print(console_message)
        return console_message


def move_files():
    """Function moves files from a source folder to another folder based on their file extension

    """
    source_directory = get_source_directory()
    if check_directory_is_valid(source_directory) == True:
        for file_path in source_directory.iterdir():
            if file_path.is_file():
                file_name = get_file_name_from_path(file_path)
                file_extension = get_file_extension(file_path)
                destination_directory = get_destination_directory(
                    file_extension)
                move_file(file_name, source_directory,
                          destination_directory)
    else:
        console_message = f"Error: Source directory '{source_directory}' does not exist."
        print(console_message)


move_files()
