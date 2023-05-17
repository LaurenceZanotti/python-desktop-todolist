from tkinter import *
from tkinter import ttk

from .counter_style import *

class CounterPage():
    def __init__(self, root: Tk):
        self.root = root
        self.frame = ttk.Frame()
        self.__counter = 0
        self.__setup()

    def __setup(self):
        frame = ttk.Frame(self.root, padding=10)
        self.label_counter = ttk.Label(frame, text=f"Contador: {self.__counter}", **label_style)
        button = ttk.Button(frame, text="+1", command=self.__handleClick, **button_style)

        # Insert them into the main frame
        self.label_counter.pack()
        button.pack()
        frame.pack(padx=100, pady=100)

    def __handleClick(self):
        self.__counter += 1
        self.label_counter.config(text=f"Contador: {self.__counter}")

if __name__ == "__main__":
    pass