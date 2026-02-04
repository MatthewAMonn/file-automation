# Provides a way for file and directory operations, such as copying and moving.
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


def move_files():
    source_directory = get_source_directory()
    for file in source_directory.iterdir():
        if file.is_file():
            file_extension = get_file_extension(file)
            destination_directory = get_destination_directory(file_extension)
            move_file(file, source_directory, destination_directory)


def get_file_extension(file_name: str):
    char_to_find = "."
    last_index = file_name.rfind(char_to_find)
    file_extension = file_name[last_index+1:]
    return file_extension.lower()


def get_source_directory():
    return constants.source_directory


def get_destination_directory(file_type: str):
    if file_type in constants.list_apps:
        return constants.destination_directory_apps
    elif file_type in constants.list_docs:
        return constants.destination_directory_docs
    elif file_type in constants.list_images:
        return constants.list_images
    elif file_type in constants.list_spreadsheets:
        return constants.destination_directory_spreadsheets
    elif file_type in constants.list_videos:
        return constants.destination_directory_videos
    else:
        return constants.destination_directory_misc


def move_file(file_name: str, start_directory: Path, end_directory: Path):
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


# move_files()
