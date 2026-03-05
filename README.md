# Simple Calculator

# Simple Calculator 

Features
- Addition, subtraction, multiplication, division
- Raises an error on division by zero
- Simple GUI available with buttons and display

Run the graphical app (Windows):

```bash
python ui.py
```

Run the tests (unit + integration) with a single command using pytest:

```bash
pytest -q
```

If you prefer the built-in unittest runner you can also run:

```bash
python -m unittest -q
```

What I implemented
- Unit tests: at least 8 tests covering +, -, *, / and edge cases (division by
	zero, negative numbers, decimals).
- Integration tests: 2 tests that simulate button presses and verify the UI
	input layer interacts correctly with the calculation logic.

Files
- `calc.py`: core calculation functions used by the app.
- `ui.py`: calculator input engine and a Tkinter GUI wrapper.
- `test_calc.py`: unit tests for the core logic.
- `test_integration.py`: integration tests that simulate user interaction.

If you want me to also add a requirements file or package this as an
executable, tell me and I will prepare it.
