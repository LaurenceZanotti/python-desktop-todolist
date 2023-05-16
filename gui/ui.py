from tkinter import *

from .pages.counter_page import CounterPage

class UI:
    def __init__(self):
        self.root = Tk()
        self.__setup()

    def __setup(self):
        self.root.title("Counter App v0.0.0")
        page = CounterPage(self.root)

if __name__ == "__main__":
    pass