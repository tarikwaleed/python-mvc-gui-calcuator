import tkinter as tk
class View(tk.Tk):
    """docstring for View."""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def main(self):
      self.mainloop()
