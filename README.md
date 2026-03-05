# Quick-Calc

Quick-Calc is a simple desktop calculator designed for teaching and
demonstration. It supports addition, subtraction, multiplication and
division, provides a small Tkinter-based graphical interface, and includes
unit and integration tests so instructors can validate functionality easily.

## Project Requirements (what the professor should have)
- Python 3.8+ installed (Windows users: `py` launcher is recommended).
- `pytest` (only required to run the full test suite including integration tests).
- Tkinter (bundled with standard Windows Python installers; if missing,
	install the OS-specific tkinter package).

## Setup Instructions
1. Clone the repository and change into the project folder:

```powershell
git clone <repo-url>
cd Calc
```

2. Verify Python is available (prefer the launcher):

```powershell
py -3 --version
```

3. Install `pytest` (optional but recommended to run all tests):

```powershell
py -3 -m pip install --user pytest
```

## How to Run the Application
- Run the GUI (recommended on Windows with the launcher):

```powershell
py -3 ui.py
```

You can also run `python ui.py` if your `python` command points to the
correct Python installation.

## How to Run Tests
- Recommended (runs unit + integration tests):

```powershell
py -3 -m pytest -q
```

- Alternatively run only the unit tests with the standard library runner:

```powershell
py -3 -m unittest -q
```

Note: `test_integration.py` uses plain test functions and assertions; pytest
is the simplest runner for those tests.

## Testing Framework Research
Pytest and Unittest are two common testing frameworks in Python with
different philosophies. Unittest is part of the standard library and follows
a class-based, xUnit-style approach. It is stable, well-documented and
works out-of-the-box without additional dependencies, which can be an
advantage in constrained or highly regulated environments. However, it can
require more boilerplate (test classes, setup/teardown methods) and its
assertion methods are sometimes less convenient than native Python asserts.

Pytest is a widely-used third-party framework that emphasizes simplicity and
concise tests. It supports plain test functions, powerful fixtures, rich
assertion introspection (native `assert` statements), and a large plugin
ecosystem. Pytest often leads to shorter, more readable tests and makes it
easy to parametrize and organize cases.

Why Pytest for Quick-Calc: pytest was chosen because it minimizes
boilerplate and makes integration tests straightforward to write and run
(plain functions and asserts). Its fixture system and plugin ecosystem also
make it a practical choice for small educational projects where clarity and
conciseness are priorities.

## Files
- `calc.py`: core calculation functions used by the app.
- `ui.py`: calculator input engine and a Tkinter GUI wrapper (buttons:
	digits, operations, and Clear/Equals).
- `test_calc.py`: unit tests for the core logic.
- `test_integration.py`: integration tests that simulate user interaction.

If you want, I can add a `requirements.txt` that lists `pytest` and a
Windows `run_tests.bat` / `run_ui.bat` to make running the project even
easier for your professor. Would you like me to add those files and commit them?
