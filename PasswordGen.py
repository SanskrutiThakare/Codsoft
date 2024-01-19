import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import string

def generate_password(length=12, include_lowercase=True, include_uppercase=True,
                      include_digits=True, include_symbols=True):
    lowercase_letters = string.ascii_lowercase if include_lowercase else ''
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    symbols = string.punctuation if include_symbols else ''

    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    if not all_characters:
        return None

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate_password_button_clicked():
    length = int(length_var.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    password = generate_password(length, include_lowercase, include_uppercase,
                                  include_digits, include_symbols)

    if password:
        result_var.set(password)
    else:
        messagebox.showerror("Error", "Please include at least one character set.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure frames
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Create and configure widgets
length_var = tk.StringVar(value="12")
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

length_label = ttk.Label(main_frame, text="Password Length:")
length_entry = ttk.Entry(main_frame, textvariable=length_var, width=5)

lowercase_checkbox = ttk.Checkbutton(main_frame, text="Lowercase", variable=lowercase_var)
uppercase_checkbox = ttk.Checkbutton(main_frame, text="Uppercase", variable=uppercase_var)
digits_checkbox = ttk.Checkbutton(main_frame, text="Digits", variable=digits_var)
symbols_checkbox = ttk.Checkbutton(main_frame, text="Symbols", variable=symbols_var)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password_button_clicked)

result_label = ttk.Label(main_frame, text="Generated Password:")
result_entry = ttk.Entry(main_frame, textvariable=result_var, state="readonly")

# Arrange widgets in the grid
length_label.grid(column=0, row=0, sticky=tk.W, pady=5)
length_entry.grid(column=1, row=0, pady=5)
lowercase_checkbox.grid(column=0, row=1, sticky=tk.W, pady=5)
uppercase_checkbox.grid(column=1, row=1, sticky=tk.W, pady=5)
digits_checkbox.grid(column=0, row=2, sticky=tk.W, pady=5)
symbols_checkbox.grid(column=1, row=2, sticky=tk.W, pady=5)
generate_button.grid(column=0, row=3, columnspan=2, pady=10)
result_label.grid(column=0, row=4, sticky=tk.W, pady=5)
result_entry.grid(column=1, row=4, sticky=(tk.W, tk.E), pady=5)

# Start the GUI event loop
root.mainloop()
