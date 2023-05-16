from tkinter import *
from tkinter import ttk

class UI:
    def __init__(self):
        self.__counter = 0
        self.root = Tk()
        self.__setup()

    def __setup(self):
        self.root.title("Counter App v0.0.0")

        # Setup widgets
        frame = ttk.Frame(self.root, padding=10)
        self.label_counter = ttk.Label(frame, text=f"Contador: {self.__counter}")
        button = ttk.Button(frame, text="+1", command=self.__handleClick)

        # Insert them into the main frame
        self.label_counter.grid()
        frame.grid()
        button.grid()

    def __handleClick(self):
        self.__counter += 1
        self.label_counter.config(text=f"Contador: {self.__counter}")

if __name__ == "__main__":
    pass