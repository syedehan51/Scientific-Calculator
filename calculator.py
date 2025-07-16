import math
import tkinter as tk
from tkinter import messagebox

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)
        self.configure(bg="#222")

        self.expression = ""
        self.display = tk.Entry(self, font=("Arial", 20), bg="#333", fg="white", justify="right", bd=0, insertbackground='white')
        self.display.grid(row=0, column=0, columnspan=5, sticky="nsew", pady=(10,20), ipady=10)

        buttons = [
            ('7', '8', '9', '/', 'sqrt'),
            ('4', '5', '6', '*', 'pow'),
            ('1', '2', '3', '-', 'log'),
            ('0', '.', '^', '+', 'ln'),
            ('sin', 'cos', 'tan', '(', ')'),
            ('asin', 'acos', 'atan', 'factorial', 'C'),
            ('pi', 'e', 'abs', 'round', '='),
        ]

        for r, row in enumerate(buttons, 1):
            for c, btn_text in enumerate(row):
                btn = tk.Button(self, text=btn_text, font=("Arial", 14), fg="white", bg="#444",
                                activebackground="#666", activeforeground="white",
                                bd=0, highlightthickness=0,
                                command=lambda text=btn_text: self.on_button_click(text))
                btn.grid(row=r, column=c, sticky="nsew", padx=3, pady=3)

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        for i in range(len(buttons) + 1):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':

            self.expression = ""
            self.update_display()
        elif char == '=':
            self.calculate()
        elif char in ('pi', 'e'):

            self.expression += f" {char} "
            self.update_display()
        elif char == 'pow':
            self.expression += "^"
            self.update_display()
        elif char == 'sqrt':
            self.expression += "sqrt("
            self.update_display()
        elif char in ('log', 'ln', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'factorial', 'abs', 'round'):
            self.expression += f"{char}("
            self.update_display()
        else:
            self.expression += char
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def safe_factorial(self, n):
        if not n.is_integer() or n < 0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        return math.factorial(int(n))

    def calculate(self):
        expr = self.expression.replace('^', '**').replace('ln', 'log')
        try:
            allowed_names = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan,
                'log': math.log10,
                'log10': math.log10,
                'ln': math.log,
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e,
                'factorial': self.safe_factorial,
                'abs': abs,
                'round': round,
                'pow': pow,
            }
            result = eval(expr, {"__builtins__": None}, allowed_names)
            self.expression = str(result)
            self.update_display()
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression:\n{e}")
            self.expression = ""
            self.update_display()

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()
