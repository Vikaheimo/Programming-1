"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    try:
        file_name = input("Enter the name of the score file: ")
        pisteet = {}
        file = open(file_name, mode="r")
        for line in file:
            sanat = line.rstrip().split()
            value = sanat[1]
            if sanat[0] not in pisteet:
                pisteet[sanat[0]] = int(sanat[1])
            else:
                pisteet[sanat[0]] += int(sanat[1])

        print("Contestant score:")
        for pelaajan_nimi in sorted(pisteet):
            print(pelaajan_nimi, pisteet[pelaajan_nimi])
    except OSError:
        print("There was an error in reading the file.")
    except ValueError:
        print("There was an erroneous score in the file:")
        print(value)
    except IndexError:
        print("There was an erroneous line in the file:")
        print(" ".join(sanat))


if __name__ == "__main__":
    main()
