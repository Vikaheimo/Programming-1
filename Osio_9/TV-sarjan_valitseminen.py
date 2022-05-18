"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def main():
    series = {}
    all_genres = []
    filename = input("Enter the name of the file: ")
    file = open(filename, mode="r")
    for line in file:
        line_data = line.rstrip().split(";")
        genres = []
        for i in line_data[1].split(","):
            if i not in all_genres:
                all_genres.append(i)
            genres.append(i)
        series[line_data[0]] = genres
    file.close()
    print("Available genres are:", ", ".join(sorted(all_genres)))

    word = input("> ")
    while word != "exit":
        sarjat = []
        for ser in series:
            for e in series[ser]:
                if e == word:
                    sarjat.append(ser)
        for i in sorted(sarjat):
            print(i)
        word = input("> ")


if __name__ == "__main__":
    main()
