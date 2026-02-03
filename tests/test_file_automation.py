import pytest
from pathlib import Path
from src import file_automation


@pytest.mark.parametrize(
    "directory, expected_result",
    [
        (Path("C:/Users/13605/Downloads/"), True),
        (Path("C:/Users/13605/Downloads/DL_Docs/"), True),
        (Path("C:/Users/13605/Downloads/DL_Images/"), True),
        (Path("C:/Users/13605/Downloads/DL_Apps"), True),
        (Path("C:/Users/13605/Downloads/DL_Videos/"), True),
        (Path("C:/Users/13605/Downloads/DL_Misc/"), True),
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
