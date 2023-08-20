import tkinter as tk

def on_button_click(event):
    current_text = result_label.cget("text")
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current_text)
            result_label.config(text=result)
        except Exception as e:
            result_label.config(text="Error")

    elif button_text == "C":
        result_label.config(text="")
    else:
        result_label.config(text=current_text + button_text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

result_label = tk.Label(root, text="", anchor="e", font=("Helvetica", 24))
result_label.pack(fill="both", padx=10, pady=10, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

button_text = [
    ("7", 1, 0, 1, 1), ("8", 1, 1, 1, 1), ("9", 1, 2, 1, 1), ("/", 1, 3, 1, 1),
    ("4", 2, 0, 1, 1), ("5", 2, 1, 1, 1), ("6", 2, 2, 1, 1), ("*", 2, 3, 1, 1),
    ("1", 3, 0, 1, 1), ("2", 3, 1, 1, 1), ("3", 3, 2, 1, 1), ("-", 3, 3, 1, 1),
    ("0", 4, 0, 1, 1), (".", 4, 1, 1, 1), ("C", 4, 2, 1, 1), ("+", 4, 3, 1, 1),
    ("=", 5, 0, 1, 4)  # Spanning 4 columns
]


for (btn_text, row, col, rowspan, colspan) in button_text:
    button = tk.Button(button_frame, text=btn_text, font=("Helvetica", 24), height=2, width=5)
    button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan)
    button.bind("<Button-1>", on_button_click)

root.mainloop()
