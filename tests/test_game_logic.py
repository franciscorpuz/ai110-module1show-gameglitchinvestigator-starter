import pytest

from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_high_hint_says_go_lower():
    # Regression: hints used to be reversed ("Too High" said "Go HIGHER!")
    _, message = check_guess(60, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_hint_says_go_higher():
    # Regression: hints used to be reversed ("Too Low" said "Go LOWER!")
    _, message = check_guess(40, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_comparison_is_numeric_not_lexicographic():
    # Regression: the secret was sometimes a string, so "9" > "10" was True.
    # 9 is lower than 10, so this must be "Too Low".
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"

    # 100 is higher than 20 (as strings, "100" < "20").
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"


def test_string_secret_is_not_silently_coerced():
    # Regression: the string fallback in check_guess is gone, so a mismatched
    # type now raises instead of giving an inconsistent answer.
    with pytest.raises(TypeError):
        check_guess(5, "10")
