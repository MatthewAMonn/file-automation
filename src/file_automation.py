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
