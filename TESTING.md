### Testing Strategy
I tested the core arithmetic logic in `calc.py` with unit tests that cover addition, subtraction, multiplication, division, decimals, negative numbers and division-by-zero. I added two integration tests that operate on `CalculatorEngine` in `ui.py` to simulate user flows (e.g., 5 + 3 → 8, and Clear resets display). I did not automate GUI clicks or run performance/stress tests because the assignment focuses on correctness and reliable, fast tests.

### Lecture Concepts
- Testing Pyramid: I kept many fast unit tests at the base and a small number of integration tests above them; I avoided slow end-to-end GUI automation to keep the suite quick and maintainable.
- Black-box vs White-box: unit tests follow a white-box style (directly calling `compute()` and checking error behavior); integration tests are more black-box, simulating user actions and asserting visible outputs.
- Functional vs Non-Functional: I focused on functional testing (correct arithmetic and input handling). I intentionally did not test non-functional properties like performance, accessibility or rendering differences.


### Test Results Summary

| Test File | Type | Purpose | Status | Pass/Fail Criteria |
|---|---:|---|---:|---|
| `test_calc.py` | Unit | Core arithmetic and edge cases | PASS | PASS because `compute()` returns correct results for + - * /, handles decimals and negatives, and raises ValueError on division by zero.
| `test_integration.py` | Integration | Simulated user flows via `CalculatorEngine` | PASS | PASS because sequences like 5 + 3 → display `8` and Clear resets display to `0`. 
