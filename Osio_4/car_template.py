"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size, to_fill, gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            values = drive(x, y, new_x, new_y, gas, gas_consumption)
            gas = values[0]
            x = values[1]
            y = values[2]
        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(size_of_the_tank, requested_amount, current_gas):
    """
    returns the amount of gas after filling up the gas
    :param size_of_the_tank:
    :param requested_amount:
    :param current_gas:
    :return:
    """
    if requested_amount + current_gas < size_of_the_tank and requested_amount >=0:
        return requested_amount + current_gas
    elif size_of_the_tank == current_gas or requested_amount < 0:
        return current_gas
    else:
        return size_of_the_tank


def drive(old_x, old_y, new_x, new_y,current_fuel, fuel_consumption):
    """
    drive function of the car
    checks if you can travel the distance specified
    if you have enough gas
    if not calculates where you can get with your current gas

    :param current_fuel:
    :param fuel_consumption:
    :param old_x:
    :param old_y:
    :param new_x:
    :param new_y:
    :return:
    """
    full_distance = sqrt((old_x-new_x)**2+(old_y-new_y)**2)

    if check_if_enough_fuel(current_fuel, fuel_consumption, full_distance):
        x = new_x
        y = new_y

        return how_much_fuel_left(current_fuel, fuel_consumption, full_distance), x, y
    else:
        p = max_distance_with_current_fuel(current_fuel, fuel_consumption)
        m = full_distance
        x = old_x + (p/m)*(new_x-old_x)
        y = old_y + (p/m)*(new_y-old_y)
        return 0.00, x, y


def max_distance_with_current_fuel(current_fuel, fuel_consumption):
    """
    calculates max distance with current fuel
    :param current_fuel:
    :param fuel_consumption:
    :return:
    """
    return current_fuel / (fuel_consumption/100)


def check_if_enough_fuel(current_fuel, fuel_consumption, distance):
    """
    checks if enough gas is present for the specifed distance
    :param current_fuel:
    :param fuel_consumption:
    :param distance:
    :return:
    """
    if current_fuel - fuel_consumption * (distance/100) < 0:
        return False
    return True


def how_much_fuel_left(current_fuel, fuel_consumption, distance_travelled):
    """
    calculates how much fuel is left after driving
    :param current_fuel:
    :param fuel_consumption:
    :param distance_travelled:
    :return:
    """
    return current_fuel - fuel_consumption * (distance_travelled/100)


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
