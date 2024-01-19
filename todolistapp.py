import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # GUI Elements
        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(root, textvariable=self.task_var, font=("Arial", 12), width=30)
        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(root, selectbackground="lightblue", font=("Arial", 12), height=10)
        self.delete_button = ttk.Button(root, text="Delete Task", command=self.delete_task)

        # Layout
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, columnspan=3)
        self.delete_button.grid(row=2, column=0, columnspan=3, pady=(0, 10))

        # Bind Double Click Event to Listbox
        self.task_listbox.bind("<Double-1>", self.delete_task)

    def add_task(self):
        new_task = self.task_var.get()
        if new_task:
            self.tasks.append(new_task)
            self.update_task_list()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_task_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    app = TodoListApp(root)
    root.mainloop()
