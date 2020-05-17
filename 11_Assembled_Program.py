from tkinter import *
from functools import partial   # To prevent unwanted windows
import random


class Converter:
    def __init__(self):

        # Formatting variables
        background_color = "light blue"

        # Converter Frame
        self.converter_frame = Frame(bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Converter Heading (row 0)
        self.temp_heading_label = Label(self.converter_frame,
                                        text="Temperature Converter",
                                        font="Arial 19 bold", bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        # User instructions (row 1)
        self.temp_instructions_label = Label(self.converter_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the button below...",
                                             font="Arial 10 italic", wrap=290,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        # Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.converter_frame, width=20,
                                      font="Arial 14 bold")
        self.to_convert_entry.grid(row=2)

        # Converter button frame (row 3),orchid3 | khaki1
        self.conversion_button_frame = Frame(self.converter_frame)
        self.conversion_button_frame.grid(row=3,pady=10)

        self.to_c_button = Button(self.conversion_button_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  bg="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_button_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  bg="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        # Answer label (row 4)
        self.converter_label = Label(self.converter_frame,font="Arial 14 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converter_label.grid(row=4)

        # History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                       text="Calculation History", width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5, command=self.help)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"   # Pale pink background for when entry box has errors

        # Retrieve amount entered into Entry field
        to_convert = self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # Check and convert to Fahrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            # Check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees C is {} degrees F".format(to_convert, celsius)

            else:
                # Input is invalid (too cold)!!
                answer = "Too Cold!"
                has_errors = "Yes"

            # Display answer
            if has_errors == "no":
                self.converter_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converter_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

            # Add Answer to list for history
                if answer != "Too Cold":
                    self.all_calculations.append(answer)
                    print(self.all_calculations)

        except ValueError:
            self.converter_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)

        return rounded

    def help(self):
        print("you asked for help")
        get_help = Help(self)
        help = "Help text goes here"
        get_help.help_text.configure(text=help)


class Help:
        def __init__(self, partner):

             background = "orange"

             #disable help button
             partner.help_button.config(state=DISABLED)

             # Sets up child window  (ie: help box)
             self.help_box = Toplevel()

             # If users press cross at top, closes help and 'releases' help button
             self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

             # Set up GUI Frame
             self.help_frame = Frame(self.help_box, bg=background)
             self.help_frame.grid()

             # Set up Help heading (row 0)
             self.how_heading = Label(self.help_frame, text="Help / Instruction",
                                      font="arial 10 bold", bg=background)

             # Help text (label, row 1)
             self.help_text =Label(self.help_frame, text="",
                                   justify=LEFT, width=40, bg=background,wrap=250)
             self.help_text.grid(row=1)

            # Dismiss button (row 2)
             self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                       width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
             self.dismiss_btn.grid(row=2, pady=10)

        def close_help(self, partner):
            # Put help button back to normal...
            partner.help_button.config(state=NORMAL)
            self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()