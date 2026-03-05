"""Integration tests simulating user interactions (student-style descriptions).

These tests exercise the interaction between the input layer (button presses)
and the calculation logic.
"""
from ui import CalculatorEngine


def test_full_add_sequence():
    # Student: I press 5, then +, then 3, then =, I expect 8.
    e = CalculatorEngine()
    e.press_digit('5')
    e.press_op('+')
    e.press_digit('3')
    e.press_equals()
    assert float(e.get_display()) == 8.0


def test_clear_after_calculation():
    # Student: After doing a calculation, pressing Clear resets display to 0.
    e = CalculatorEngine()
    e.press_digit('5')
    e.press_op('+')
    e.press_digit('3')
    e.press_equals()
    e.press_clear()
    assert e.get_display() == '0'
