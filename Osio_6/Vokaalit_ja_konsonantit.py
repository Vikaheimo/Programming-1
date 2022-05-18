"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    sana = input("Enter a word: ")
    vokaalit = 0
    konsonantit = 0
    for i in sana:
        if i in "aeiouy":
            vokaalit += 1
        elif i in "qwrtpsdfghjklzxcvbnm":
            konsonantit += 1
    print(f"The word \"{sana}\" contains {vokaalit} vowels and {konsonantit} consonants.")


if __name__ == "__main__":
    main()
