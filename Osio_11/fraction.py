"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return self.return_string()

    def __lt__(self, frac2):
        """
        less than operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator < frac2.__numerator/frac2.__denominator

    def __le__(self, frac2):
        """
        less than or equal operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator <= frac2.__numerator/frac2.__denominator

    def __gt__(self, frac2):
        """
        greater than operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator > frac2.__numerator/frac2.__denominator

    def __ge__(self, frac2):
        """
        greater than or equal operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator >= frac2.__numerator/frac2.__denominator

    def __eq__(self, frac2):
        """
        equality operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator == frac2.__numerator/frac2.__denominator

    def __ne__(self, frac2):
        """
        not equal operator
        :param frac2:
        :return:
        """
        return self.__numerator/self.__denominator != frac2.__numerator/frac2.__denominator

    def simplify(self):
        """
        returns the simplifed versions of the numbers
        :return: float
        """
        gcd = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__denominator /= gcd
        self.__numerator /= gcd

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""
        return f"{sign}{abs(self.__numerator):.0f}/{abs(self.__denominator):.0f}"

    def complement(self):
        """
        calculates the complement of a fraction
        :return: Fraction: new fraction
        """
        return Fraction(-self.__numerator, self.__denominator)


    def reciprocal(self):
        """
        calculates the complement of a fraction
        :return: Fraction: new fraction
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, frac2):
        """
        calculates the multiplication of two fractions
        :param frac2: second fraction
        :return: Fraction: new fraction
        """
        return Fraction(self.__numerator*frac2.__numerator,self.__denominator*frac2.__denominator)

    def divide(self, frac2):
        """
        calculates the division of two fractions
        :param frac2: second fraction
        :return: Fraction: new fraction
        """
        return Fraction(self.__numerator*frac2.__denominator,self.__denominator*frac2.__numerator)

    def add(self, frac2):
        """
        calculates the sum of two fractions
        :param frac2: second fraction
        :return: Fraction: new fraction
        """
        return Fraction(self.__numerator*frac2.__denominator+frac2.__numerator*self.__denominator,self.__denominator*frac2.__denominator)

    def deduct(self, frac2):
        """
        calculates the difference of two fractions
        :param frac2: second fraction
        :return: Fraction: new fraction
        """
        return Fraction(self.__numerator*frac2.__denominator-frac2.__numerator*self.__denominator,self.__denominator*frac2.__denominator)


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    a = Fraction(1,2)
    print(a)
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    lista = []
    a = input()
    while a != "":
        fraction_parts = a.split("/")
        lista.append(Fraction(int(fraction_parts[0]), int(fraction_parts[1])))
        a = input()
    print("The given fractions in their simplified form:")
    for i in lista:
        a = i.return_string()
        i.simplify()
        print(a, "=", i)

if __name__ == "__main__":
    main()
