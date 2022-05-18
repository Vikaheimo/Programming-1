"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def calculate_angle(k1, k2=90):
    """
    ottaa kaksi kulman suurutta ja palauttaa viimeisen suuruden
    jos syötetään vain yksi kulma niin silloin toinen kulma oletetaan
    suoraksi kulmaksi
    :param k1:
    :param k2:
    :return:
    """
    return 180-k1-k2


def main():
    print(calculate_angle(12))


if __name__ == "__main__":
    main()
