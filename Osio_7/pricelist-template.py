"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    kysytty_tuote = input("Enter product name: ").strip()
    while kysytty_tuote != "":
        if kysytty_tuote in PRICES:
            print(f"The price of {kysytty_tuote} is {PRICES[kysytty_tuote]:.2f} e")
        else:
            print(f"Error: {kysytty_tuote} is unknown.")

        kysytty_tuote = input("Enter product name: ").strip()
    print("Bye!")


if __name__ == "__main__":
    main()
