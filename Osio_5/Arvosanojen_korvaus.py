"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def convert_grades(lista):
    """
    ottaa arvoksi listan arvosanoja muuttaa ne 6 jos
    arvosana on suurempaa kuin 0
    :param lista:
    :return:
    """
    for i in lista:
        if i > 0:
            lista[lista.index()]



def main():
    lista = [1,2,3,5,1,0,0,1,2]
    convert_grades(lista)
    print(lista)


if __name__ == "__main__":
    main()
