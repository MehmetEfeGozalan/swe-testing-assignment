# Simple Calculator

This small command-line calculator is prepared for your assignment.

Features:
- Addition, subtraction, multiplication, division
- Graceful handling of division by zero (raises an error message)
- Reset result with `C` or `clear`

Usage:

Interactive REPL:

```
python calc.py
```

Example inputs (REPL):
- `5 + 3`   -> provide Calctwo numbers
- `+ 4`     -> add 4 to the current `result`
- `C`       -> reset the result to zero
- `quit`    -> exit

Single-expression run:

```
python calc.py "5 + 3"
```

Run tests:

```
python -m unittest -q
```
