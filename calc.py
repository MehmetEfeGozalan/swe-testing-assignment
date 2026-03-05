#!/usr/bin/env python3
import sys

def compute(a, op, b):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ValueError('Division by zero')
        return a / b
    raise ValueError(f'Unsupported operator: {op}')

def parse_number(token):
    try:
        if '.' in token:
            return float(token)
        return int(token)
    except Exception:
        raise ValueError(f'Invalid number: {token}')

def repl():
    result = 0
    print('Simple Calculator — enter expressions like "5 + 3" or "+ 4" to apply to result.')
    print('Commands: C or clear to reset, q or quit to exit.')
    while True:
        try:
            s = input(f'[result={result}] calc> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nGoodbye')
            break
        if not s:
            continue
        low = s.lower()
        if low in ('q', 'quit', 'exit'):
            print('Goodbye')
            break
        if low in ('c', 'clear'):
            result = 0
            print('Cleared. result = 0')
            continue
        tokens = s.split()
        try:
            if len(tokens) == 3:
                a = parse_number(tokens[0])
                op = tokens[1]
                b = parse_number(tokens[2])
                result = compute(a, op, b)
            elif len(tokens) == 2 and tokens[0] in ('+', '-', '*', '/'):
                op = tokens[0]
                b = parse_number(tokens[1])
                result = compute(result, op, b)
            elif len(tokens) == 1:
                # single number -> set result
                result = parse_number(tokens[0])
            else:
                print('Invalid input. Use: "a + b" or "+ b" or "C"')
                continue
            print('= {}'.format(result))
        except ValueError as e:
            print('Error:', e)

def run_once_from_argv(argv):
    # usage: calc.py "5 + 3"
    if len(argv) < 2:
        repl()
        return
    expr = ' '.join(argv[1:]).strip()
    if expr.lower() in ('c', 'clear'):
        print('Cleared. result = 0')
        return
    tokens = expr.split()
    try:
        if len(tokens) != 3:
            raise SystemExit('Provide an expression like: "5 + 3"')
        a = parse_number(tokens[0])
        op = tokens[1]
        b = parse_number(tokens[2])
        res = compute(a, op, b)
        print(res)
    except ValueError as e:
        print('Error:', e)

if __name__ == '__main__':
    run_once_from_argv(sys.argv)
