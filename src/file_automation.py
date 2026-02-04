# Provides a way for file and directory operations, such as copying and moving.
from pathlib import Path

# Global variables for folder to be organized and the locations for all folders that will have files moved into them
source_directory = Path("C:/Users/13605/Downloads/")
destination_directory_docs = Path("C:/Users/13605/Downloads/DL_Docs/")
destination_directory_images = Path("C:/Users/13605/Downloads/DL_Images/")
destination_directory_apps = Path("C:/Users/13605/Downloads/DL_Apps")
destination_directory_videos = Path("C:/Users/13605/Downloads/DL_Videos/")
destination_directory_spreadsheets = Path(
    "C:/Users/13605/Downloads/DL_Spreadsheets/")
destination_directory_misc = Path("C:/Users/13605/Downloads/DL_Misc/")

# Global lists for file extensions that fall under a set type, like txt and pdf for documents.
docs_list = ["pdf", "txt", "doc", "docx", "odt", "rtf", ]
images_list = ["png", "jpg", "jpeg", "gif",
               "tiff", "webp", "svg", "raw", "heif"]
apps_list = ["exe", "app", "msi", "pkg", "bat", "sh", "ps1"]
videos_list = ["mp4", "mov", "mkv", "avi", "wmv"]
spreadsheets_list = ["xlsx", "xls", "csv"]


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


# def move_files():
    # for item in source_directory.iterdir():
        # if item.is_file():

        # print(item.name)
        # print(get_file_extension(item.name))
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
    file_extension = file_name[last_index+1:]
    return file_extension.lower()


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


"""
format for moving a file

if file extension exists in a list, all other than misc will have a list
    then 


"""
