"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    mieliala = int(input("How do you feel? (1-10) "))

    if mieliala == 10:
        print("A suitable smiley would be :-D")

    elif mieliala == 1:
        print("A suitable smiley would be :'(")

    elif mieliala > 7 and mieliala < 10:
        print("A suitable smiley would be :-)")

    elif mieliala < 4 and mieliala > 1:
        print("A suitable smiley would be :-(")

    elif mieliala >= 4 and mieliala <= 7:
        print("A suitable smiley would be :-|")

    else:
        print("Bad input!")


if __name__ == "__main__":
    main()
