"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def lue_teksti():
    """
    lukee tekstin käyttäjltä
    :return:
    """
    lista = []
    to_list = input()
    while to_list != "":
        for i in to_list:
            lista.append(i)
        lista.append(" ")
        to_list = input()

    return lista


def poista_tyhjat(lista):
    """
    poistaa tyhjät sanat listasta
    :param lista:
    :return:
    """
    for i, v in enumerate(lista):
        if len(v) == 0:
            lista.remove(v)


def etsi_sanat(sanalista):
    """
    etsii sanat annetusta listasta
    :param sanalista:
    :return:
    """
    uusi_sanalista = []
    edellinen_sana = 0
    for i, v in enumerate(sanalista):
        if v == " ":
            uusi_sanalista.append("".join(sanalista[edellinen_sana:i]))
            edellinen_sana = i +1
    poista_tyhjat(uusi_sanalista)
    return uusi_sanalista


def listan_pituuslaskuri(lista):
    """
    laskee listan arvojen pituudet summa
    :param lista:
    :return:
    """
    pituus = 0
    for e in lista:
        pituus += len(e)
    return pituus


def lisaa_valilyonnit(lista, valilyontien_maara_jokaiseen, ylijaama):
    """
    lisää välilynnit sanojen väliin
    :param lista:
    :param valilyontien_maara_jokaiseen:
    :param ylijaama:
    :return:
    """
    teksti = ""
    for e in lista:
        teksti += e + valilyontien_maara_jokaiseen * " "
        if ylijaama > 0:
            teksti += " "
            ylijaama -= 1
    return teksti


def print_listan_tekija(sanalista, merkkia_per_rivi):
    """
    tekee printattavan lsitan
    :param sanalista:
    :param merkkia_per_rivi:
    :return:
    """
    print_lista = []
    merkkien_lisaus = []
    for sana in sanalista:
        if listan_pituuslaskuri(merkkien_lisaus)+ len(merkkien_lisaus) + len(sana) <= merkkia_per_rivi:
            # Tämä ei ehkä toimi oikein
            # ensiksi listan merkkien pituus, sen jälkeen välilyönnit ja siteen tarkastetaan onko tilaa uudelle merkille
            # välilyntejä ei tarvitse huomioda koska se menee laskussa mukana
            merkkien_lisaus.append(sana)
        else:
            merkkien_lisauksen_pituus = listan_pituuslaskuri(merkkien_lisaus)
            sanojen_maara = len(merkkien_lisaus)
            tarvittavat_valilyonnit = merkkia_per_rivi - merkkien_lisauksen_pituus
            if sanojen_maara != 1:
                ylijaama = tarvittavat_valilyonnit % (sanojen_maara-1)
                valilyontien_maara_jokaiseen = int((tarvittavat_valilyonnit - ylijaama)/(sanojen_maara -1))

                lisaus = lisaa_valilyonnit(merkkien_lisaus, valilyontien_maara_jokaiseen, ylijaama)
                lisaus = lisaus.strip()
                print_lista.append(lisaus)
            else:
                jaa = ""
                for i in merkkien_lisaus:
                    jaa += i
                print_lista.append(jaa)
            merkkien_lisaus = [sana]

    print_lista.append(lisaa_valilyonnit(merkkien_lisaus, 1, 0))
    return print_lista


def aloitus():
    """
    tulostaa tarvittavat jutut ja pyörittää koko ohjelmaaa
    :return:
    """
    print("Enter text rows. Quit by entering an empty row.")
    teksti = lue_teksti()
    sanalista = etsi_sanat(teksti)
    merkkia_per_rivi = int(input("Enter the number of characters per line: "))
    print_lista = print_listan_tekija(sanalista, merkkia_per_rivi)
    for i in print_lista:
        print(i)


def main():
    aloitus()


if __name__ == "__main__":
    main()
