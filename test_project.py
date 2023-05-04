import pytest
import unittest.mock as mock
from project import read_csv, begin_quiz, quiz, get_user_choice, get_level_list, shuffle_all_level_list

quiz_data_file = "ScienceQuizData.csv"
pytest.level_list_dict = {"easy": [], "medium": [], "hard": []}  # global variable.
read_csv(quiz_data_file, pytest.level_list_dict)


@mock.patch('builtins.input', lambda *args: "A")
def test_get_user_choice():
    assert (get_user_choice()) == "A"


def test_shuffle_all_level_list():
    before = pytest.level_list_dict["easy"]
    shuffle_all_level_list(pytest.level_list_dict)
    assert len(before) == len(pytest.level_list_dict["easy"])


def test_get_level_list():
    assert (get_level_list(10)) == "medium"
    assert (get_level_list(5)) == "easy"
    assert (get_level_list(2)) == "easy"
    assert (get_level_list(25)) == "hard"


def test_read_csv():
    assert len(pytest.level_list_dict) >= 1
    with pytest.raises(SystemExit):
        read_csv("junkFile.csv", pytest.level_list_dict)
