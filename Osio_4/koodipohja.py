"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def print_box(width, height, border_mark="#", inner_mark=" "):
    """
    tulostaa laatikon halutuilla arvoilla
    jos ulkomerkkiä tai sisämerkkiä ei spesifioida niin ne otetaan oletusarvoista
    :param width:
    :param height:
    :param border_mark:
    :param inner_mark:
    :return:
    """
    print(width*border_mark)
    for i in range(height-2):
        print(border_mark+inner_mark*(width-2)+border_mark)
    print(width * border_mark)
    print()


def main():
    print_box(5, 4)
    print_box(3, 8, "*")
    print_box(5, 4, "O", "o")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)


if __name__ == "__main__":
    main()
