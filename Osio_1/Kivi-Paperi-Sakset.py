"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    p1voitto = "Player 1 won!"
    p2voitto = "Player 2 won!"
    pelaaja1 = input("Player 1, enter your choice (R/P/S): ")
    pelaaja2 = input("Player 2, enter your choice (R/P/S): ")

    if pelaaja1 == pelaaja2:
        print("It's a tie!")

    elif pelaaja1 == "R":

        if pelaaja2 == "P":
            print(p2voitto)

        else:
            print(p1voitto)

    elif pelaaja1 == "S":

        if pelaaja2 == "R":
            print(p2voitto)

        else:
            print(p1voitto)

    else:

        if pelaaja2 == "S":
            print(p2voitto)
        else:
            print(p1voitto)


if __name__ == "__main__":
    main()
