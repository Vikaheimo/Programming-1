"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    while True:
        bored = input("Bored? (y/n) ")

        if bored in "Yy":
            break

        elif bored in "nN":
            pass

        else:
            print("Incorrect entry.")
    print("Well, let's stop this, then.")

if __name__ == "__main__":
    main()
