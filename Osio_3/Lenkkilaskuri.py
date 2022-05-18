"""
COMP.CS.100
Tekijä: Vili Ikäheimo ja Petrus Pakarinen
Opiskelijanumero: 150286761
Tehtävä 3.3
"""


def main():
    summa = 0
    laiska = False
    matka = 1
    p1 = 1.0
    p2 = 1.0

    paivat = int(input("Enter the number of days: "))  # kysytään päivien lukumäärän

    for p in range(1, paivat+1):  # käy läpi kaikki päivät

        matka = float(input(f"Enter day {p} running length: "))
        summa += matka

        if matka == 0 and matka == p2 and matka == p1:  # jos henkilö syöttää kolme peräkkäistä nollaa niin hypätään pois loopista
            laiska = True
            break

        p2 = p1     # tallennetaan edellisen päivän matkat uuusiin muuttujiin
        p1 = matka

    keskiarvo = summa/paivat
    print()

    if laiska:
        print("You had too many consecutive lazy days!")

    elif keskiarvo < 3:
        print(f"Your running mean of {keskiarvo:.2f} km was too low!")

    else:
        print(f"You were persistent runner! With a mean of {keskiarvo:.2f} km.")


if __name__ == "__main__":
    main()
