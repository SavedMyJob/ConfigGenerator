""" main.py """
import tkinter as tk
from rotation_config_generator import RotationConfigGenerator

if __name__ == "__main__":
    root = tk.Tk()
    app = RotationConfigGenerator(root)
    root.mainloop()