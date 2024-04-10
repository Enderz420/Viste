import tkinter as tk
from tkinter import filedialog

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("VisTE")

menu = tk.Menu(root)
root.config(menu=menu)

menu.add_command(label="New", command=new_file)
menu.add_command(label="Save", command=save_file)
menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill="both")

root.mainloop()