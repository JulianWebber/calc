import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""
        
        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()
        
        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, borderwidth=4)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 0
        col = 0
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=10, height=3, command=button_command).grid(row=row, column=col, padx=1, pady=1)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set("")
        elif button == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("error")
                self.expression = ""
        else:
            self.expression += button
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()