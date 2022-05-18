"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150286761
Name:       Vili Ikäheimo
Email:      vili.ikaheimo@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    """
    Luokka jolla muodosteaan kappaletavaralaskin
    """
    def __init__(self):
        """
        Init metodi luokalle
        """
        self.__mainwindow = Tk()

        self.__number_value = 0

        self.__current_value_label = Label(self.__mainwindow, text=self.__number_value)
        self.__reset_button = Button(self.__mainwindow, text="Reset", command=self.reset_value)
        self.__increase_button = Button(self.__mainwindow, text="Increase", command=self.increase_value)
        self.__decrease_button = Button(self.__mainwindow, text="Decrease", command=self.decrease_value)
        self.__quit_button = Button(self.__mainwindow, text="Quit", command=self.quit)

        self.__current_value_label.grid(row=0, column=1, columnspan=2)
        self.__reset_button.grid(row=1, column=0)
        self.__increase_button.grid(row=1, column=1)
        self.__decrease_button.grid(row=1, column=2)
        self.__quit_button.grid(row=1, column=3)

        self.__mainwindow.mainloop()

    def increase_value(self):
        """
        metodi lukujen lisäämiselle
        :return:
        """
        self.__number_value += 1
        self.__current_value_label.configure(text=self.__number_value)

    def decrease_value(self):
        """
         metodi lukujen vähentämiselle
        :return:
        """
        self.__number_value -= 1
        self.__current_value_label.configure(text=self.__number_value)

    def reset_value(self):
        """
        metodi arvon nollaamiselle
        :return:
        """
        self.__number_value = 0
        self.__current_value_label.configure(text=self.__number_value)

    def quit(self):
        self.__mainwindow.quit()
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
