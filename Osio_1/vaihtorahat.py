"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():

    hinta = int(input("Purchase price: "))
    maksu = int(input("Paid amount of money: "))
    vaihtorahat = maksu-hinta

    if vaihtorahat > 0:
        raha_10 = (vaihtorahat-vaihtorahat % 10)/10
        vaihtorahat -= raha_10 * 10

        raha_5 = (vaihtorahat-vaihtorahat % 5)/5
        vaihtorahat -= raha_5 * 5

        raha_2 = (vaihtorahat-vaihtorahat  %2)/2
        vaihtorahat -= raha_2 * 2

        raha_1 = vaihtorahat

        print("Offer change:")
        raha_10 = int(raha_10)
        raha_5 = int(raha_5)
        raha_2 = int(raha_2)
        raha_1 = int(raha_1)

        if raha_10 > 0:
            print(str(raha_10) + " ten-euro notes")

        if raha_5 > 0:
            print(str(raha_5) + " five-euro notes")

        if raha_2 > 0:
            print(str(raha_2) + " two-euro coins")

        if raha_1 > 0:
            print(str(raha_1) + " one-euro coins")
    else:
        print("No change")


if __name__ == "__main__":
    main()
