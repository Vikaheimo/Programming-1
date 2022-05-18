"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__throws = []

    def get_name(self):
        return self.__name

    def add_points(self, score):
        self.__throws.append(score)
        if self.__score + score > 50:
            print(f"{self.__name} gets penalty points!")
            self.__score = 25
        else:
            self.__score += score

        if 40 <= self.__score <= 49:
            print(f"{self.__name} needs only {50 - self.__score} "
                  f"points. It's better to avoid knocking down the pins with "
                  f"higher points.")

    def accuracy(self):
        """
        calulates the hit accuracy
        based on how many throws hit the target
        :return:
        """
        if len(self.__throws) == 0:
            return 0
        else:
            return (len(self.__throws)-self.__throws.count(0))/len(self.__throws)*100

    def average_points(self):
        return sum(self.__throws)/len(self.__throws)

    def has_won(self):
        """
        checks if a player has won the game
        :return: bool
        """
        return self.__score == 50

    def get_points(self):
        """
        returns the amount of points
        :return: int
        """
        return self.__score

    def cheer(self, score):
        """
        cheers if the score is better than average
        :param score:
        :return:
        """
        if score > self.average_points():
            print(f"Cheers {self.__name}!")


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        in_turn.cheer(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), f"p, hit percentage {player1.accuracy():.1f}")
        print(player2.get_name() + ":", player2.get_points(), f"p, hit percentage {player2.accuracy():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
