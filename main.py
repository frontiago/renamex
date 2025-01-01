import os 
from tkinter import *
from tkinter import filedialog, messagebox 

def rename_files(folder_path, base_name):
    try:
        # List all files in the directory
        files = os.listdir(folder_path)

        # Sort files to ensure consistent ordering
        files.sort()

        # Loop through each file and rename it
        for index, filename in enumerate(files):
            # Create a name with the base name and increment number
            new_name = f"{base_name}{index + 1}{os.path.splitext(filename)[1]}"

            # Get the full paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_name)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed {filename} to {new_name}")

        messagebox.showinfo("Success", "Files renamed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, END)
    folder_path_entry.insert(0, folder_path)

def on_rename_click():
    folder_path = folder_path_entry.get()
    base_name = base_name_entry.get()

    if not folder_path or not base_name:
        messagebox.showerror("Error, please fill all the fields")
        return 

    rename_files(folder_path, base_name)

# Create the main window
root = Tk()
root.title("Renamex - File Renamer")

# Folder path input
Label(root, text="Folder Path").grid(row=0, column=0, padx=10, pady=10)
folder_path_entry = Entry(root, width=50)
folder_path_entry.grid(row=0, column=1, padx=10, pady=10)
Button(root, text="Browse", command=browse_folder).grid(row=0, column=2, padx=10, pady=10)

# Base name input
Label(root, text="Base Name").grid(row=1, column=0, padx=10,pady=10)
base_name_entry = Entry(root, width=50)
base_name_entry.grid(row=1, column=1, padx=10, pady=10)

# Rename button
Button(root, text="Rename Files", command=on_rename_click).grid(row=2, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
