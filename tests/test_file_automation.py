import pytest
from pathlib import Path
from src import file_automation


@pytest.mark.parametrize(
    "directory, expected_result",
    [
        (file_automation.source_directory, True),
        (file_automation.destination_directory_docs, True),
        (file_automation.destination_directory_images, True),
        (file_automation.destination_directory_apps, True),
        (file_automation.destination_directory_videos, True),
        (file_automation.destination_directory_spreadsheets, True),
        (file_automation.destination_directory_misc, True),
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
