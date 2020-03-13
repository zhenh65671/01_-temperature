from tkinter import *
from functools import partial   # To prevent unwanted windows

import random





class Converter:
    def __init__(self):

        # Formatting variables...
        background_color = "light blue"

        # In actual program this blank and is populated with user calculations
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C is 104 degrees F',
                              '40 degrees C is 4.4 degrees F',
                              '12 degrees C is 53.6 degrees F', ]

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=400,height=400, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Set up history Heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                          font="Arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label,row 1)
        self.history_text = Label(self.converter_frame, text="",
                                justify=LEFT, width=40, bg=background, wrap=250)
        self.history_text.grid(row=1)


    def history(self):
        get_history = history(self)
        get_history.history_text.configure(text="History text goes here")




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Converter(root)
    root.mainloop()
