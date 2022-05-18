"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def etsi_valilyonnit(teksti):
    """
    etsii välilynnit tekstistä ja palauttaa niiden indeksit
    :param teksti:
    :return:
    """
    lista = []
    for c, v in enumerate(teksti):
        if v == " ":
            lista.append(c)
    return lista


def oikean_tekstin_valitsija(teksti, rivin_pituus, edellinen_sana_loppuu, edellinen_rivi_loppuu):
    """
    palauttaa tekstin siten että ei leikata sanoja
    :param teksti:
    :param rivin_pituus:
    :param edellinen_sana_loppuu:
    :param edellinen_rivi_loppuu:
    :return:
    """
    edellinen_sana_loppuu += 1
    if teksti[edellinen_rivi_loppuu+rivin_pituus] == " ":
        return teksti[edellinen_rivi_loppuu:edellinen_rivi_loppuu+rivin_pituus].strip()
    else:
        return teksti[edellinen_rivi_loppuu:edellinen_sana_loppuu].strip()


def valilyonnit_oikeille_paikoille(teksti, pituus):
    """
    lisää välilyntejä tarvittaessa
    :param teksti:
    :param pituus:
    :return:
    """
    uusi_teksti = ""
    valilyonnit = etsi_valilyonnit(teksti)
    edellinen_paattuu = 0
    if len(teksti) == pituus:
        return teksti
    lisavalilyonnit = pituus - len(teksti)
    ylimaara = lisavalilyonnit % len(valilyonnit)
    montako_lisaa = (lisavalilyonnit-ylimaara) / len(valilyonnit)
    for c in valilyonnit:
        uusi_teksti += teksti[edellinen_paattuu:c] + " " * int(montako_lisaa)
        edellinen_paattuu = c
        if ylimaara > 0:
            uusi_teksti += " "
            ylimaara -= 1

    return uusi_teksti + teksti[edellinen_paattuu:]


def poista_valilyonnit(teksti):
    uusi = ""
    for i in teksti:
        if i != " ":
            uusi += i
    return uusi

def tekstin_rivitys(teksti, merkkien_maara):
    """
    rivttää tekstin oikein
    :param teksti:
    :param merkkien_maara:
    :return:
    """
    palautus_lista = []
    edellinen_sana = 0
    rivin_pituus = 0
    edellinen_rivi_loppuu = 0
    c = -1
    while c < len(teksti)-1:
        c += 1
        v = teksti[c]
        if v == " ":
            edellinen_sana = c
        rivin_pituus += 1

        if merkkien_maara == rivin_pituus:
            oikea = oikean_tekstin_valitsija(teksti,rivin_pituus, edellinen_sana, edellinen_rivi_loppuu)
            palautus_lista.append(valilyonnit_oikeille_paikoille(oikea, merkkien_maara))
            rivin_pituus = 0
            edellinen_rivi_loppuu += len(oikea)+1
            c = edellinen_rivi_loppuu
    palautus_lista.append(teksti[edellinen_rivi_loppuu:])
    return palautus_lista


def lue_teksti():
    """
    lukee tekstin ja palauttaa sen
    :return:
    """
    palautus = ""
    teksti = input()
    while teksti != "":
        palautus += " " + teksti.strip()
        teksti = input()
    return palautus.strip()


def main():
    print("Enter text rows. Quit by entering an empty row.")
    msg = lue_teksti()
    merkkia_per_rivi = int(input("Enter the number of characters per line: "))
    teksti_lista = tekstin_rivitys(msg, merkkia_per_rivi)
    for i in teksti_lista:
        print(i)


if __name__ == "__main__":
    main()
