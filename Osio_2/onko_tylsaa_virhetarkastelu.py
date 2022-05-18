"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    while True:
        bored = input("Answer Y or N: ")

        if bored.upper() in "YN":
            break
        print("Incorrect entry.")

    print("You answered " + bored)


if __name__ == "__main__":
    main()
