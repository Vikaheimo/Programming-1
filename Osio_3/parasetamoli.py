"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def calculate_dose(massa, aika, annos):
    """
    laskee tarvittavan parasetamolin määrän annetuilla avoilla
    :param massa:
    :param aika:
    :param annos:
    :return:
    """
    maks_annos = 4000 - annos

    if maks_annos <= 0 and aika < 24 or aika < 6:
        return 0

    return min(massa*15, maks_annos)


def main():
    mass = int(input("Patient's weight (kg): "))
    time = int(input("How much time has passed from the previous dose (full hours): "))
    dose = int(input("The total dose for the last 24 hours (mg): "))

    print(f"The amount of Parasetamol to give to the patient: {calculate_dose(mass, time, dose)}")
    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()
