# Kevin Sim
# Resourced used: Geeksforgeeks.org, Stackoverflow.com
# Code skeletal structure based on linked below:
# https://www.geeksforgeeks.org/python-simple
# -calculator-using-tkinter/?ref=rp
# Project code author: AyanBanerjee3
# My changes: color scheme, names, code comments, pep8 format
# https://stackoverflow.com/questions/7591294/how-to-create-
# a-self-resizing-grid-of-buttons-in-tkinter by 'Vaughn Cato'

# Load everything from tkinter library
from tkinter import *
# Imports the math functions
import math


# Class is 'number cruncher', aka another name for calculator
class numCrunch:

    # Function that makes sure '/' means 'divide
    # and that '*' means 'multiply'
    def replaceSymbol(self):
        self.expression = self.e.get()
        # backslash is now 'divide by'
        self.newtext = self.expression.replace('/', '/')
        # asterisk is now 'multiply by'
        self.newtext = self.newtext.replace('x', '*')

    # Function that means "equals to"
    def answer(self):
        self.replaceSymbol()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Error!')
        else:
            self.e.delete(0, END)
            self.e.insert(0, self.value)

    # Function that means "square root of"
    def sqrt(self):
        self.replaceSymbol()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Error!')
        else:
            self.sqrtval = math.sqrt(self.value)
            self.e.delete(0, END)
            self.e.insert(0, self.sqrtval)

    # Function that means "square of"
    def timesItself(self):
        self.replaceSymbol()
        try:
            self.value = eval(self.newtext)
        except SyntaxError or NameError:
            self.e.delete(0, END)
            self.e.insert(0, 'Error!')
        else:
            self.sqval = math.pow(self.value, 2)
            self.e.delete(0, END)
            self.e.insert(0, self.sqval)

    # Function that clears the input window
    def totalWipe(self):
            self.e.delete(0, END)

    # Function that clears the input window one character at a time
    def wipe(self):
            self.txt = self.e.get()[:-1]
            self.e.delete(0, END)
            self.e.insert(0, self.txt)

    # Function that registers the user's button press
    def press(self, argi):
            self.e.insert(END, argi)

    # Function that is the default GUI constructor
    # 'fg' is foreground, 'bg' is background,
    # 'width' and 'height' is button dimensions
    def __init__(self, master):
            # Title of GUI
            master.title('Basic Calculator')
            # Determines shape
            master.geometry()
            self.e = Entry(master)
            # Grid size
            # configure your buttons so that they
            # will expand to fill the cell using 'sticky=NSEW' (Vaughn Cato)
            self.e.grid(row=0, column=0, columnspan=6, pady=3, sticky=NSEW)
            # Focus
            self.e.focus_set()
            # "=" button
            Button(master, text="=", width=13, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.answer()).grid(
                   row=4, column=4, columnspan=2, sticky=NSEW)
            # configure the rows and columns to have a non-zero
            # weight so that they will take up the extra space (Vaughn Cato)
            Grid.rowconfigure(master, 4, weight=1)
            Grid.columnconfigure(master, 4, weight=1)
            # "AC" button to execute 'totalWipe' function
            Button(master, text='AC', width=6, height=3,
                   fg="black", bg="white",
                   command=lambda: self.totalWipe()).grid(
                   row=1, column=4, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 4, weight=1)
            # "C" button to execute 'wipe' function
            Button(master, text='C', width=6, height=3,
                   fg="black", bg="white",
                   command=lambda: self.wipe()).grid(
                   row=1, column=5, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 5, weight=1)
            # addition button
            Button(master, text="+", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press('+')).grid(
                   row=4, column=3, sticky=NSEW)
            Grid.rowconfigure(master, 4, weight=1)
            Grid.columnconfigure(master, 3, weight=1)
            # multiplication button
            Button(master, text="x", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press('x')).grid(
                   row=2, column=3, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 3, weight=1)
            # subtraction button
            Button(master, text="-", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press('-')).grid(
                   row=3, column=3, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 3, weight=1)
            # division button
            Button(master, text="÷", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press('/')).grid(
                   row=1, column=3, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 3, weight=1)
            # Percentage symbol
            Button(master, text="%", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press('%')).grid(
                   row=4, column=2, sticky=NSEW)
            Grid.rowconfigure(master, 4, weight=1)
            Grid.columnconfigure(master, 2, weight=1)
            # Seven
            Button(master, text="7", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press('7')).grid(
                   row=1, column=0, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 0, weight=1)
            # Eight
            Button(master, text="8", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(8)).grid(
                   row=1, column=1, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 1, weight=1)
            # Nine
            Button(master, text="9", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(9)).grid(
                   row=1, column=2, sticky=NSEW)
            Grid.rowconfigure(master, 1, weight=1)
            Grid.columnconfigure(master, 2, weight=1)
            # Four
            Button(master, text="4", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(4)).grid(
                   row=2, column=0, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 0, weight=1)
            # Five
            Button(master, text="5", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(5)).grid(
                   row=2, column=1, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 1, weight=1)
            # Six
            Button(master, text="6", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(6)).grid(
                   row=2, column=2, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 2, weight=1)
            # One
            Button(master, text="1", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(1)).grid(
                   row=3, column=0, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 0, weight=1)
            # Two
            Button(master, text="2", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(2)).grid(
                   row=3, column=1, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 1, weight=1)
            # Three
            Button(master, text="3", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(3)).grid(
                   row=3, column=2, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 2, weight=1)
            # Zero
            Button(master, text="0", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press(0)).grid(
                   row=4, column=0, sticky=NSEW)
            Grid.rowconfigure(master, 4, weight=1)
            Grid.columnconfigure(master, 0, weight=1)
            # Add decmial to text window
            Button(master, text=".", width=6, height=3,
                   fg="black", bg="grey",
                   command=lambda: self.press('.')).grid(
                   row=4, column=1, sticky=NSEW)
            Grid.rowconfigure(master, 4, weight=1)
            Grid.columnconfigure(master, 1, weight=1)
            # Open parenthesis
            Button(master, text="(", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press('(')).grid(
                   row=2, column=4, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 4, weight=1)
            # Close parenthesis
            Button(master, text=")", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.press(')')).grid(
                   row=2, column=5, sticky=NSEW)
            Grid.rowconfigure(master, 2, weight=1)
            Grid.columnconfigure(master, 5, weight=1)
            # Square root button
            Button(master, text="?", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.sqrt()).grid(
                   row=3, column=4, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 4, weight=1)
            # executes square function
            Button(master, text="x²", width=6, height=3,
                   fg="black", bg="light grey",
                   command=lambda: self.timesItself()).grid(
                   row=3, column=5, sticky=NSEW)
            Grid.rowconfigure(master, 3, weight=1)
            Grid.columnconfigure(master, 5, weight=1)


# Simple Calculator Program (SCP)
def simpCalc():
    # Program driver
    base = Tk()
    # Instantiate object
    obj = numCrunch(base)
    # Execute GUI
    base.mainloop()

# Execute SCP
if __name__ == "__main__":
    # Call function
    simpCalc()
