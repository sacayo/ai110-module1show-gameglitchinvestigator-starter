from logic_utils import check_guess

# --- Original tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: hint direction ---
# Bug: check_guess used to say "Go HIGHER!" when guess > secret (backwards).
# Fix: guess > secret → "Go LOWER!", guess < secret → "Go HIGHER!"

def test_hint_says_go_lower_when_guess_too_high():
    # Positive: guess is above secret, message must direct player DOWN
    _, message = check_guess(80, 50)
    assert "LOWER" in message

def test_hint_says_go_higher_when_guess_too_low():
    # Positive: guess is below secret, message must direct player UP
    _, message = check_guess(20, 50)
    assert "HIGHER" in message

def test_hint_does_not_say_go_higher_when_too_high():
    # Negative: should NOT tell player to go higher when guess is already too high
    _, message = check_guess(80, 50)
    assert "HIGHER" not in message

def test_hint_does_not_say_go_lower_when_too_low():
    # Negative: should NOT tell player to go lower when guess is already too low
    _, message = check_guess(20, 50)
    assert "LOWER" not in message

def test_win_message_not_directional():
    # Negative: a correct guess should not tell the player to go higher or lower
    _, message = check_guess(50, 50)
    assert "HIGHER" not in message
    assert "LOWER" not in message


# --- Bug fix: check_guess returns a tuple ---
# Bug: tests compared check_guess() directly to a string; it actually returns (outcome, message).

def test_check_guess_returns_tuple():
    # Positive: result must be a 2-tuple
    result = check_guess(50, 50)
    assert isinstance(result, tuple)
    assert len(result) == 2

def test_check_guess_outcome_is_string():
    # Positive: first element must be a string outcome
    outcome, message = check_guess(60, 50)
    assert isinstance(outcome, str)
    assert isinstance(message, str)

def test_check_guess_outcome_not_just_message():
    # Negative: the full tuple must not equal a bare string
    result = check_guess(50, 50)
    assert result != "Win"
