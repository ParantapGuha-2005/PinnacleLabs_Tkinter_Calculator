import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.equation = ""

        # Display Screen
        self.display = tk.Entry(
            root, font=("Helvetica", 24), bg="#252538", fg="#cdd6f4",
            bd=0, justify="right", insertbackground="white"
        )
        self.display.pack(pady=20, fill="x", padx=15, ipady=15)

        # Button Layout
        button_frame = tk.Frame(root, bg="#1e1e2e")
        button_frame.pack(fill="both", expand=True, padx=15, pady=10)

        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]

        row, col = 0, 0
        for btn_text in buttons:
            if not btn_text:
                continue
                
            # Styling specific buttons
            if btn_text == 'C':
                bg_color, fg_color = "#f38ba8", "#11111b"
            elif btn_text in ['/', '*', '-', '+', '=']:
                bg_color, fg_color = "#cba6f7", "#11111b"
            else:
                bg_color, fg_color = "#313244", "#cdd6f4"

            btn = tk.Button(
                button_frame, text=btn_text, font=("Helvetica", 14, "bold"),
                bg=bg_color, fg=fg_color, activebackground="#45475a",
                activeforeground="white", bd=0, cursor="hand2"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            
            # Bind click events
            if btn_text == '=':
                btn.config(command=self.evaluate)
            elif btn_text == 'C':
                btn.config(command=self.clear)
            else:
                btn.config(command=lambda val=btn_text: self.press(val))

            col += 1
            if col > 3:
                col = 0
                row += 1

        # Make buttons resize evenly
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def press(self, num):
        self.equation += str(num)
        self.update_display()

    def clear(self):
        self.equation = ""
        self.update_display()

    def evaluate(self):
        try:
            # Safely evaluate the math string
            result = str(eval(self.equation))
            self.equation = result
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()