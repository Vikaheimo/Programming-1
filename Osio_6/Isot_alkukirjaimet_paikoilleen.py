"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def capitalize_initial_letters(teksi):
    """
    ottaa teksin ja palauttaa takaisin teksitin kaikki sanat isoilla alkukirjaimilla
    ja loput merkit pienellä
    :param teksi:
    :return:
    """
    teksi = teksi.lower()
    isolla = ""
    seuraava_isolla = True
    for l in teksi:
        if l == " ":
            seuraava_isolla = True
            isolla += l
        elif seuraava_isolla:
            seuraava_isolla = False
            isolla += l.upper()
        else:
            isolla += l

    return isolla

def main():
    print(capitalize_initial_letters("kKidklfsdkljfioKJLIÖHiolö kjh jkldsflkjhlkj lkjH LKj lkujdsf lkjdhs"))



if __name__ == "__main__":
    main()