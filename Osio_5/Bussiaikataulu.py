"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
Tehtävä
"""


def main():
    aikataulu = [630, 1015, 1415, 1620, 1720, 2000, 630, 1015]
    seuraava_bussi = 630
    aika = int(input("Enter the time (as an integer): "))
    if aika <= 2000:
        for a in aikataulu:
            seuraava_bussi = a
            if seuraava_bussi >= aika:
                break

    print("The next buses leave:")
    k = aikataulu.index(seuraava_bussi)
    print(seuraava_bussi, aikataulu[k+1], aikataulu[k+2], sep="\n")


if __name__ == "__main__":
    main()
1