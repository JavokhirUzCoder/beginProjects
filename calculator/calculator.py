import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display = tk.Entry(self.master, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for digits 0-9
        self.digit_buttons = []
        for i in range(10):
            button = tk.Button(self.master, text=str(i), font=("Arial", 16), width=3, height=1,
                               command=lambda digit=i: self.add_digit(digit))
            self.digit_buttons.append(button)

        # Add digit buttons to the grid
        for i in range(1, 10):
            self.digit_buttons[i].grid(row=3 - (i-1)//3, column=(i-1)%3)
        self.digit_buttons[0].grid(row=4, column=1)

        # Create buttons for operations
        self.operation_buttons = []
        for op in ["+", "-", "*", "/"]:
            button = tk.Button(self.master, text=op, font=("Arial", 16), width=3, height=1,
                               command=lambda operation=op: self.set_operation(operation))
            self.operation_buttons.append(button)

        # Add operation buttons to the grid
        for i in range(4):
            self.operation_buttons[i].grid(row=i+1, column=3)

        # Create equals button
        self.equals_button = tk.Button(self.master, text="=", font=("Arial", 16), width=3, height=1,
                                        command=self.calculate)
        self.equals_button.grid(row=4, column=2)

        # Create clear button
        self.clear_button = tk.Button(self.master, text="C", font=("Arial", 16), width=3, height=1,
                                       command=self.clear_display)
        self.clear_button.grid(row=4, column=0)

        self.reset()

    def reset(self):
        self.current_value = 0
        self.current_operation = None
        self.clear_display()

    def clear_display(self):
        self.display.delete(0, tk.END)

    def add_digit(self, digit):
        self.display.insert(tk.END, str(digit))

    def set_operation(self, operation):
        self.current_operation = operation
        self.current_value = float(self.display.get())
        self.clear_display()

    def calculate(self):
        new_value = float(self.display.get())
        if self.current_operation == "+":
            self.current_value += new_value
        elif self.current_operation == "-":
            self.current_value -= new_value
        elif self.current_operation == "*":
            self.current_value *= new_value
        elif self.current_operation == "/":
            self.current_value /= new_value
        self.clear_display()
        self.display.insert(tk.END, str(self.current_value))

root = tk.Tk()
app = Calculator(root)
root.mainloop()
