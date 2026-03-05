#!/usr/bin/env python3
import tkinter as tk
from calc import compute


class CalculatorEngine:
    """Simple calculator input layer that talks to `compute()`.

    This class is intentionally UI-agnostic so tests can simulate button presses
    without requiring a window.
    """
    def __init__(self):
        self.clear()

    def clear(self):
        self.display = '0'
        self.stored = None
        self.pending_op = None
        self.reset_next = False

    def _current_value(self):
        try:
            if '.' in self.display:
                return float(self.display)
            return int(self.display)
        except Exception:
            return 0

    def _format_number(self, n):
        if isinstance(n, float) and n.is_integer():
            return int(n)
        return n

    def press_digit(self, d):
        if self.reset_next or self.display == '0':
            self.display = d
            self.reset_next = False
        else:
            self.display += d

    def press_dot(self):
        if self.reset_next:
            self.display = '0.'
            self.reset_next = False
        elif '.' not in self.display:
            self.display += '.'

    def press_op(self, op):
        cur = self._current_value()
        if self.stored is None:
            self.stored = cur
        else:
            self.stored = compute(self.stored, self.pending_op, cur)
        self.pending_op = op
        self.reset_next = True
        self.display = str(self._format_number(self.stored))

    def press_equals(self):
        if self.pending_op is None:
            return
        cur = self._current_value()
        res = compute(self.stored if self.stored is not None else 0, self.pending_op, cur)
        self.display = str(self._format_number(res))
        self.stored = None
        self.pending_op = None
        self.reset_next = True

    def press_clear(self):
        self.clear()

    def get_display(self):
        return str(self.display)


class CalculatorGUI:
    def __init__(self, master=None):
        self.master = master or tk.Tk()
        self.master.title('Student Calculator')
        self.engine = CalculatorEngine()
        self._build_ui()

    def _build_ui(self):
        self.display_var = tk.StringVar(value=self.engine.get_display())
        entry = tk.Entry(self.master, textvariable=self.display_var, justify='right', font=('Arial', 18), bd=10)
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Note: swapped positions so Clear ('C') is where '=' used to be,
        # and '=' is now the full-width bottom button for clarity.
        btns = [
            ('7', self._on_digit), ('8', self._on_digit), ('9', self._on_digit), ('/', self._on_op),
            ('4', self._on_digit), ('5', self._on_digit), ('6', self._on_digit), ('*', self._on_op),
            ('1', self._on_digit), ('2', self._on_digit), ('3', self._on_digit), ('-', self._on_op),
            ('0', self._on_digit), ('.', self._on_dot), ('C', self._on_clear), ('+', self._on_op),
        ]

        r = 1
        c = 0
        for (txt, handler) in btns:
            b = tk.Button(self.master, text=txt, command=lambda t=txt, h=handler: h(t), width=5, height=2, font=('Arial', 14))
            b.grid(row=r, column=c, sticky='nsew')
            c += 1
            if c > 3:
                c = 0
                r += 1

        equals = tk.Button(self.master, text='=', command=lambda: self._on_equals('='), width=5, height=2, font=('Arial', 14))
        equals.grid(row=r, column=0, columnspan=4, sticky='nsew')

        for i in range(5):
            self.master.rowconfigure(i, weight=1)
        for i in range(4):
            self.master.columnconfigure(i, weight=1)

    def _sync_display(self):
        self.display_var.set(self.engine.get_display())

    def _on_digit(self, key):
        self.engine.press_digit(key)
        self._sync_display()

    def _on_dot(self, _):
        self.engine.press_dot()
        self._sync_display()

    def _on_op(self, key):
        self.engine.press_op(key)
        self._sync_display()

    def _on_equals(self, _):
        self.engine.press_equals()
        self._sync_display()

    def _on_clear(self):
        self.engine.press_clear()
        self._sync_display()

    def run(self):
        self.master.mainloop()


if __name__ == '__main__':
    app = CalculatorGUI()
    app.run()
