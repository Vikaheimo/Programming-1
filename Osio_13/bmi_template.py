"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150286761
Name:       Vili Ikäheimo
Email:      vili.ikaheimo@tuni.fi

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()


        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry()
        self.__weight_exp = Label(text="Weight (KG)")

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry()
        self.__height_exp = Label(text="Height (cm)")

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(text="Laske BMI", command=self.calculate_BMI, background="red",
                                         foreground="green")

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(text="")

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label()

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(text="Lopeta MUT!", command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=1)
        self.__height_value.grid(row=1, column=1)
        self.__calculate_button.grid(row=2,columnspan=2)
        self.__stop_button.grid(row=3,columnspan=2)
        self.__result_text.grid(row=4,columnspan=2)
        self.__explanation_text.grid(row=5,columnspan=2)
        self.__height_exp.grid(row=1, column=0)
        self.__weight_exp.grid(row=0, column=0)


    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            paino = float(self.__weight_value.get())
            korkeus = float(self.__height_value.get())/100
            if paino <= 0 or korkeus <= 0:
                self.__explanation_text.configure(text="Error: height and weight must be positive.")
                self.reset_fields()
                return

            bmi = paino/(korkeus**2)
            if 18.5 <= bmi <= 25:
                self.__explanation_text.configure(text="Your weight is normal.")
            elif bmi > 25:
                self.__explanation_text.configure(text="You are overweight.")
            else:
                self.__explanation_text.configure(text="You are underweight.")

            self.__result_text.configure(text=f"{bmi:.2f}")
        except ValueError:
            self.reset_fields()
            self.__explanation_text.configure(text="Error: height and weight must be numbers.")


    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        self.__result_text.configure(text="")
        self.__height_value.delete(0, END)
        self.__weight_value.delete(0, END)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
