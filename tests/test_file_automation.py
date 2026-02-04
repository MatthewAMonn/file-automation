import pytest
from pathlib import Path
from src import file_automation


source_directory = Path("C:/Users/13605/Downloads/")
destination_directory_docs = Path("C:/Users/13605/Downloads/DL_Docs/")
destination_directory_images = Path("C:/Users/13605/Downloads/DL_Images/")
destination_directory_apps = Path("C:/Users/13605/Downloads/DL_Apps")
destination_directory_videos = Path("C:/Users/13605/Downloads/DL_Videos/")
destination_directory_spreadsheets = Path(
    "C:/Users/13605/Downloads/DL_Spreadsheets/")
destination_directory_misc = Path("C:/Users/13605/Downloads/DL_Misc/")


@pytest.mark.parametrize(
    "directory, expected_result",
    [
        (source_directory, True),
        (destination_directory_docs, True),
        (destination_directory_images, True),
        (destination_directory_apps, True),
        (destination_directory_videos, True),
        (destination_directory_spreadsheets, True),
        (destination_directory_misc, True),
        (Path("C:/Fake/Path/"), False),
        (Path(""), False),
        (Path(), False)
    ]
)
def test_directory_exists(directory, expected_result):
    """Simple test to make sure the hard coded directories to be used in the main program exist

    Args:
        directory (Path): Path of the directory to be tested
        expected_result (bool): Expected result from calling check_directory_is_valid
    """
    result = file_automation.check_directory_is_valid(directory)
    assert result == expected_result
