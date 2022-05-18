"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def read_file(filename):
    """
    lukee tiedostosta ja paluttaa arvot sanakirjana
    :param filename:
    :return:
    """
    contacts = {}
    file = open(filename, mode="r")
    for line_num, text_line in enumerate(file):
        teksti = text_line.replace("\n", "").split(";")
        all_contacts = {}
        if line_num != 0:
            for num, value in  enumerate(teksti):
                if num != 0:
                    all_contacts[arvot[num]] = value
            contacts[teksti[0]] = all_contacts
        else:
            arvot = teksti
    return contacts


def main():
    print(read_file("contacts.csv"))


if __name__ == "__main__":
    main()
