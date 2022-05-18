"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


class Character:
    """
    Class for the character
    """
    def __init__(self, name):
        self.__name = name
        self.__inventory = {}

    def give_item(self, item_to_give):
        """

        :param item_to_give:
        :return:
        """
        if item_to_give in self.__inventory:
            self.__inventory[item_to_give] += 1
        else:
            self.__inventory[item_to_give] = 1

    def remove_item(self, item_to_remove):
        """

        :param item_to_remove:
        :return:
        """
        if item_to_remove not in self.__inventory:
            pass
        elif self.__inventory[item_to_remove] == 1:
            del self.__inventory[item_to_remove]
        else:
            self.__inventory[item_to_remove] -= 1

    def printout(self):
        """

        :return:
        """
        print("Name:", self.__name)
        if self.__inventory:
            for i in sorted(self.__inventory):
                print(" ", self.__inventory[i], i)
        else:
            print("  --nothing--")

    def get_name(self):
        """

        :return:
        """
        return self.__name

    def has_item(self, item):
        """

        :param item:
        :return:
        """
        return item in self.__inventory

    def how_many(self, item):
        """

        :param item:
        :return:
        """
        if item in self.__inventory:
            return self.__inventory[item]
        else:
            return 0


def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()
