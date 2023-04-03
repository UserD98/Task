import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title("Task")

# Stvaranje oznaka i ulaznih polja
task_name_label = tk.Label(root, text="Task Name")
task_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

task_name_entry = tk.Entry(root)
task_name_entry.grid(row=0, column=1, padx=5, pady=5)

due_date_label = tk.Label(root, text="Due Date")
due_date_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

due_date_entry = tk.Entry(root)
due_date_entry.grid(row=1, column=1, padx=5, pady=5)

priority_label = tk.Label(root, text="Priority")
priority_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Stvaranje padajućeg izbornika
priority_var = tk.StringVar()
priority_combobox = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"])
priority_combobox.grid(row=2, column=1, padx=5, pady=5)
priority_combobox.current(0)

# Stvaranje tablice
tree_columns = ("Task Name", "Due Date", "Priority")
tree = ttk.Treeview(root, columns=tree_columns, show="headings")
tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

for col in tree_columns:
    tree.heading(col, text=col)

# Funkcije za dodavanje, brisanje i spremanje zadataka
def add_task():
    task_name = task_name_entry.get()
    due_date = due_date_entry.get()
    priority = priority_var.get()

    if not task_name or not due_date:
        messagebox.showerror("Error", "Please enter task name and due date.")
        return

    tree.insert("", tk.END, values=(task_name, due_date, priority))
    clear_fields()

def clear_fields():
    task_name_entry.delete(0, tk.END)
    due_date_entry.delete(0, tk.END)
    priority_combobox.current(0)

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tree.get_children():
            values = tree.item(task)["values"]
            f.write(",".join(values) + "\n")

def delete_task():
    selection = tree.selection()
    if not selection:
        messagebox.showerror("Error", "Please select a task to delete.")
        return

    result = messagebox.askquestion("Delete Task", "Are you sure you want to delete the selected task?")
    if result == "yes":
        for task in selection:
            tree.delete(task)

def exit_task():
    result = messagebox.askquestion("Exit", "Are you sure you want to exit?")
    if result == "yes":
        save_tasks()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", exit_task)

# Stvaranje gumba
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=4, column=0, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_task)
delete_button.grid(row=4, column=1, padx=5, pady=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks)
save_button.grid(row=5, column=0, padx=5, pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_task)
exit_button.grid(row=5, column=1, padx=5, pady=5)
root.mainloop()
