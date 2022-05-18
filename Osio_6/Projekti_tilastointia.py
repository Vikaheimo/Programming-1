""""
COMP.CS.100 Python-Ohjelma
Tekijä: Petrus Pakarinen ja Vili Ikäheimo
Opiskelijanumero: 150178798 ja 150286761
"""
from math import sqrt


def list_management():
    """
    Kysyy käyttäjältä dataa, tarkistaa onko data tyhjää vai ei, sitten sijoittaa annetun datan listaan data_values.
    :data_values: Lista joka sisältää käyttäjän syöttämän datan
    :data_value: Käyttäjän syöttämä data
    :return: Palautusarvona lista, joka sisältää käyttäjän syöttämän datan
    """
    data_values=[]
    data_value = input()
    while data_value!="": #Tarkistaa että syötetty data ei ole tyhjää, sitten sijoittaa datan listaan
        data_values.append(float(data_value))
        data_value=input()
    if data_value == "":
        if len(data_values)<2: # Tarkistaa että käyttäjä on syöttänyt ainakin 2 arvoa. Jos näin ei ole, tulostaa virheilmoituksen
            print("Error: need two or more values")
            return data_values
        else: # Lopettaa ohjelman ja palauttaa palautusarvona käyttäjän datan sisältävän listan
            return data_values


def keskiarvo(lista):
    """
    laskee keskiarvon listan arvoille
    :param lista: list
    :return: float
    """
    s = summa(lista)
    lukujen_lukumaara = len(lista)
    return s/lukujen_lukumaara
def summa(lista):
    """
    laskee listaan arvoille summan
    :param lista: list
    :return: float
    """
    s = 0
    for i in lista:
        s += i
    return s


def varianssi(lista):
    """
    laskee listan arvoille varianssin
    :param lista: list
    :return: float
    """
    lukujen_lukumaara = len(lista)
    k = keskiarvo(lista)
    s = 0
    for i in lista: # lasketaan varianssin kaavasssa oleva summa
        s += (k-i)**2
    return (1/(lukujen_lukumaara-1))*s


def keskihajonta(lista):
    """
    Laskee keskihajonnan listan arvoille
    :param lista: list
    :return: float
    """
    return sqrt(varianssi(lista))


def histogrammi_laskuri(alaraja, ylaraja, lista, keskiarvo):
    """
    laskee kuinka monta arvoa on annetulla välillä annetussa listassa
    :param alaraja: float
    :param ylaraja: float
    :param lista: list
    :return: int
    """
    laskuri = 0 # laskuri jolla lasketaan arven määrä
    for luku in lista: # käydään listan arvojen läpi
        if alaraja <= abs(luku - keskiarvo) < ylaraja:
            laskuri += 1
    return laskuri


def kategoriat(k_hajonta, data_values):
    """
    Muodostaa kategoriat, ja tulostaa oikean määrän merkkejä kuhunkin kategoriaan
    :param k_hajonta: float
    :return: none
    """
    for kategorian_numero in range(0, 6):
        alaraja = kategorian_numero * 0.5 * k_hajonta
        ylaraja = (kategorian_numero + 1) * 0.5 * k_hajonta
        tahdet=histogrammi_laskuri(alaraja, ylaraja, data_values, keskiarvo(data_values))*"*" #Laskee histogrammi_laskuri funktion avulla oikean määrän tulostettavia merkkejä
        print(f"Values between std. dev. {alaraja:.2f}-{ylaraja:.2f}: {tahdet} ")


def main():
    print("Enter the data, one value per line.")
    print("End by entering empty line.")
    data_values=list_management()
    if len(data_values) < 2:
        return
    k_arvo=keskiarvo(data_values)
    vars = varianssi(data_values)
    k_hajonta=keskihajonta(data_values)
    print(f"The mean of given data was: {k_arvo:.2f}")
    if k_hajonta==0:  # Tarkistaa onko keskihajonta nolla
        print(f"The standard deviation of given data was: {k_hajonta:.2f}")
        print("Deviation is zero.")
    else:
        print(f"The standard deviation of given data was: {k_hajonta:.2f}")
        kategoriat(k_hajonta, data_values)


if __name__ == "__main__":
    main()
