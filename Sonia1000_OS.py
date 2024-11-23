import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser
import os
import subprocess

# Function to open a web browser
def browse_web():
    url = url_entry.get()
    if url:
        webbrowser.open(url)
    else:
        messagebox.showwarning("Input Error", "Please enter a URL.")

# Function to list files in a directory
def list_files():
    directory = filedialog.askdirectory()
    if directory:
        files = os.listdir(directory)
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)

# Function to read a selected file
def read_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                messagebox.showinfo("File Content", content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Function to list processes
def list_processes():
    process_list.delete(0, tk.END)
    try:
        # For Windows, use 'tasklist'. For Linux, use 'ps -e'.
        for proc in subprocess.check_output(['tasklist']).decode().splitlines()[3:]:
            process_list.insert(tk.END, proc.split()[0])
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to kill a selected process
def kill_process():
    selected_process = process_list.get(process_list.curselection())
    if selected_process:
        try:
            subprocess.run(['taskkill', '/F', '/IM', selected_process])
            messagebox.showinfo("Success", f"Killed process: {selected_process}")
            list_processes()  # Refresh the process list
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showwarning("Selection Error", "Please select a process to kill.")

# Main GUI
root = tk.Tk()
root.title("Mini OS")

# URL Entry
tk.Label(root, text="Enter URL:").pack()
url_entry = tk.Entry(root)
url_entry.pack()
tk.Button(root, text="Browse Web", command=browse_web).pack()

# File Operations
tk.Button(root, text="List Files", command=list_files).pack()
file_list = tk.Listbox(root, width=50)
file_list.pack()

tk.Button(root, text="Read File", command=read_file).pack()

# Process Operations
tk.Button(root, text="List Processes", command=list_processes).pack()
process_list = tk.Listbox(root, width=50)
process_list.pack()

tk.Button(root, text="Kill Process", command=kill_process).pack()

root.mainloop()
