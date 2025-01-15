import tkinter as tk

def create_window(x, y):
    """Create a window with specified x and y resolution."""
    window = tk.Tk()
    window.geometry(f"{x}x{y}")
    window.title("My Window")
    window.mainloop()

def on_ready():
    """This function is called when the system is ready."""
    create_window(800, 600)

def process():
    """This function processes the main logic of the program."""
    pass


on_ready()
while True:
    process()