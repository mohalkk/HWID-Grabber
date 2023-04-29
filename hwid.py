import wmi
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import pyperclip

def get_hwid():
    w = wmi.WMI()
    hwids = [component.UUID for component in w.Win32_ComputerSystemProduct()]
    hwid = str(hwids[0])
    return hwid

def copy_hwid():
    hwid = get_hwid()
    pyperclip.copy(hwid)
    messagebox.showinfo("HWID Copied", f"Your HWID ({hwid}) has been copied to the clipboard.")

root = tk.Tk()
root.geometry("275x75") 
root.title("Get HWID")

hwid_label = ttk.Label(root, text="")
hwid_label.grid(column=0, row=0, padx=5, pady=5)
hwid_value = ttk.Label(root, text=get_hwid())
hwid_value.grid(column=1, row=0, padx=5, pady=5)

copy_button = ttk.Button(root, text="Copy HWID", command=copy_hwid)
copy_button.grid(column=1, row=1, padx=5, pady=5)

root.mainloop()
