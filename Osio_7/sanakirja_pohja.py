"""
COMP.CS.100
Tekijä: Vili Ikäheimo
Opiskelijanumero: 150286761
"""


def content_printer(dictionary):
    """
    printtaa annetun sanakirjan
    :param dictionary: dict
    :return: None
    """
    print("Dictionary contents:")
    print(", ".join(sorted(dictionary)))


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}

    content_printer(english_spanish)
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "A":
            eng_word = input("Give the word to be added in English: ")
            spa_word = input("Give the word to be added in Spanish: ")
            english_spanish[eng_word] = spa_word
            content_printer(english_spanish)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from the dictionary.")

        elif command == "Q":
            print("Adios!")
            return

        elif command == "P":
            print()
            print("English-Spanish")

            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()

            print("Spanish-English")

            for word in sorted(english_spanish.values()):
                print(word, list(english_spanish.keys())[list(english_spanish.values()).index(word)])
            print()

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ").split()
            print("The text, translated by the dictionary: ")
            for word in text:
                if word in english_spanish:
                    print(english_spanish[word] + " ", end="")
                else:
                    print(word + " ", end="")
            print()
        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
