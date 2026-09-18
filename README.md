# 🧮 Scientific Calculator with Tkinter

A sleek, dark-themed scientific calculator built in Python using the Tkinter GUI framework. This project features robust expression evaluation and includes safe mathematical function parsing.

## ✨ Features
* **Core Math Operations:** Standard addition, subtraction, multiplication, division, and exponents (`^`).
* **Advanced Scientific Functions:** Trigonometry (`sin`, `cos`, `tan`), inverse trig (`asin`, `acos`, `atan`), logarithms (`log`, `ln`), and square roots.
* **Special Constants & Built-ins:** Easy access to `pi` and `e`, absolute values (`abs`), rounding, and custom `factorial` operations.
* **Modern Dark Theme:** A visually comfortable `#222` dark-mode interface with responsive, clean grid-aligned buttons.
* **Error Handling:** Built-in validation that alerts users of invalid math expressions instead of crashing the program.

## 🛠️ Tech Stack
* **Language:** Python 3
* **GUI Framework:** Tkinter (Python's standard built-in GUI library)
* **Math Logic:** Python's native `math` module

## 🧠 Technical Highlights
* **Object-Oriented Design:** Structured entirely inside a clean `ScientificCalculator` class inheriting from `tk.Tk`.
* **Safe Evaluation:** Uses custom name maps to strictly evaluate expressions safely without exposing full system built-ins.
* **Input Validation:** Features specialized exception handling for factorials, ensuring they only run on non-negative integers.

## 🚀 How To Run
Make sure you have Python installed on your computer, then run the script via your terminal or command prompt:

```bash
python calculator.py
```
