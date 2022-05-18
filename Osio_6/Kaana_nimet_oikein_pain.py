"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""

def reverse_name(nimi):
    """
    kääntää nimen oikein päin riippuen pilkusta
    :param nimi:
    :return:
    """
    ei_valiluonteja = nimi.strip()
    pilkun_paikka = ei_valiluonteja.find(",")
    if pilkun_paikka == -1:
        return nimi.strip()
    elif pilkun_paikka == 0:
        return ei_valiluonteja[1:].strip()
    elif pilkun_paikka == len(ei_valiluonteja)-1:
        return ei_valiluonteja[:-1].strip()
    else:
        return ei_valiluonteja[pilkun_paikka+1:].strip() + " " + ei_valiluonteja[:pilkun_paikka].strip()


def main():
    print(reverse_name("X,"))


if __name__ == "__main__":
    main()
