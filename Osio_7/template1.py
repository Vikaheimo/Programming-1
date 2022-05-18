"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():
    for a in sorted(PRICES.values()):
        nimi = list(PRICES.keys())[list(PRICES.values()).index(a)]
        print(f"{nimi} {a:.2f}")



if __name__ == "__main__":
    main()
