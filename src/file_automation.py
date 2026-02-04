# Provides a way for file and directory operations, such as copying and moving.
from pathlib import Path

download_directory = Path("C:/Users/13605/Downloads/")
destination_directory_docs = Path("C:/Users/13605/Downloads/DL_Docs/")
destination_directory_images = Path("C:/Users/13605/Downloads/DL_Images/")
destination_directory_apps = Path("C:/Users/13605/Downloads/DL_Apps")
destination_directory_videos = Path("C:/Users/13605/Downloads/DL_Videos/")
destination_directory_misc = Path("C:/Users/13605/Downloads/DL_Misc/")


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

# first iteration will use only file extensions to check what type of file is being looked at


def move_files():
    for item in download_directory.iterdir():
        if item.is_file():
            print(item.name)
            print(get_file_extension(item.name))
            # if file name is a document, like .PDF and .txt, move file to destination_directory_docs

            # if file name is an image, like .jpg and .png, move file to destination_directory_images
            # code
            # if file name is a program, like .exe, move file to destination_directory_apps
            # code
            # if file name is a video, like PDF and .txt, move file to destination_directory_videos
            # code


def get_file_extension(file_name: str):
    char_to_find = "."
    last_index = file_name.rfind(char_to_find)
    file_extension = file_name[last_index:]
    return file_extension.lower()


move_files()


"""
format for moving a file

if file extension exists in a list, all other than misc will have a list
    then 


"""
