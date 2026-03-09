# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the game
python -m streamlit run app.py

# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run a single test
pytest tests/test_game_logic.py::test_winning_guess
```

## Project Overview

This is an educational debugging challenge: a deliberately broken Streamlit number-guessing game. The goal is to find and fix intentional bugs, refactor logic into `logic_utils.py`, and update the test suite.

## Architecture

```
app.py              → Streamlit UI + broken game logic (main entry point)
logic_utils.py      → Stub module — students refactor functions here from app.py
tests/
  test_game_logic.py → pytest tests importing from logic_utils
```

**Game state** lives in `st.session_state`: `secret`, `attempts`, `score`, `status`, `history`.

**Game logic functions** (currently in `app.py`, meant to move to `logic_utils.py`):
- `get_range_for_difficulty(difficulty)` → `(low, high)`
- `parse_guess(raw)` → `(ok, int_or_None, error_msg)`
- `check_guess(guess, secret)` → `(outcome, message)` where outcome is `"Win"`, `"Too High"`, or `"Too Low"`
- `update_score(current_score, outcome, attempt_number)` → `int`

## Known Intentional Bugs

1. **Secret changes on submit** (lines ~158-161): Converts `secret` to string on even attempts, causing type mismatch in `check_guess()`.
2. **Backwards hints**: Hint logic is inverted.
3. **No range validation**: `parse_guess()` accepts negative numbers.
4. **New Game reset**: Button doesn't fully reset game state.

## Test/Logic Contract

Tests import from `logic_utils`, not `app.py`. After refactoring, `check_guess()` returns a tuple `(outcome, message)` — tests currently expect only the outcome string and need updating to unpack tuples.
