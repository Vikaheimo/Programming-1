"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 150286761, 150178798
Name:       Vili Ikäheimo, Petrus Pakarinen
Email:      vili.ikaheimo@tuni.fi, petrus.pakarinen@tuni.fi

A
"""
import tkinter
from random import choice
from tkinter import *


class Hirsipuu:
    def __init__(self):
        # luodaan pääikkuna määritetään sen koko ja ikkunan nimi
        self.__mainwindow = Tk()
        self.__mainwindow.geometry("600x450")
        self.__mainwindow.title("Hirsipuu-Peli")

        # lista sisältää kaikki pelattavat sanat
        self.__arvattavat_sanat = ["jazz", "terveydenhoitolautakunta", "apulaisprofessori", "tietojenkäsittelyohjelma",
                                   "diplomi-insinööri", "sotasyyllisyysoikeudenkäynnit", "jauhelihaperunasoselaatikko",
                                   "diftongi", "tanssiravintola", "automaatiotestaus"]

        # luodaan kaikki tarvittavat muuttukat luokkaan
        self.__arvaukset = 12
        self.__arvattava_sana = ""
        self.__lopputulos = ""
        self.__arvattu_sana = []
        self.__arvatut_kirjaimet = []
        self.__kuva = PhotoImage(file="hirsipuu1.png")

        # luodaan kaikki tarvittavat napit ja tekstikentät
        self.__arvattava_sana_label = Label()
        self.__arvaus_selitys_label = Label(text="Arvattava Sana:")
        self.__arvatut_kirjaimet_label = Label()
        self.__kuva_label = Label()
        self.__reset_game_button = Button(text="Reset", command=self.reset_game)

        # alustetaan peli
        self.reset_game()

        # lisätään kuva näytölle
        self.__kuva_label.grid(row=1, column=1, columnspan=11)

        # muodostetaan viruaalinäppäimistöön tarvittavat napit
        self.__buttons = []
        for a in "qwertyuiopåasdfghjklöäzxcvbnm":
            # muodostetaan napit siten että jokainen nappi kutsuu funktion self.kirjain()
            # argumenttinä sen kirjain
            self.__buttons.append(Button(self.__mainwindow, text=a.upper(),
                                         command=lambda a=a: self.kirjain(a.upper())))

        # lisätään kaikki näppäimet näytölle tarkasti halutulle paikalle
        rivi = 3
        sarake = 0
        for button in self.__buttons:
            sarake += 1
            if sarake == 12:
                rivi += 1
                sarake = 1
            button.grid(row=rivi, column=sarake)

        # sitten vielä laitetaan loputkin objektit näytölle
        self.__arvattava_sana_label.grid(row=0, column=3, columnspan=6)
        self.__arvaus_selitys_label.grid(row=0, column=1, columnspan=3)
        self.__arvatut_kirjaimet_label.grid(row=1, column=12, columnspan=2, rowspan=1)
        self.__reset_game_button.grid(row=5, column=8)

        # käynnistetään ikkunan mainloop
        self.__mainwindow.mainloop()

    def pick_a_word(self):
        """
        metodi, jolla voidaan valita satunnaisesti sana
        self.__arvattavat sanat listasta
        :return: str, satunnaisesti arvttu sana
        """
        return choice(self.__arvattavat_sanat)

    def reset_game(self):
        """
        metodi pelin uudeleenkäynnistämiseen
        :return: None
        """
        # palautetaan kaikki muuttujat takaisin aloitusarvoille
        self.__arvattava_sana = self.pick_a_word()
        self.__arvaukset = 12
        self.__lopputulos = ""
        self.__arvattu_sana = []
        self.__arvatut_kirjaimet = []
        self.__kuva = PhotoImage(file="hirsipuu1.png")

        # listään self.__arvattu_sana listan yhtä monta alaviivaa, kuin
        # arvattavassa sanassa on kirjaimia
        for letter in self.__arvattava_sana:
            if letter == "-":
                self.__arvattu_sana.append("-")
            else:
                self.__arvattu_sana.append("_ ")

        # muokataan kaikki muuttuvat tekstikentät tyhjiksi
        self.__arvatut_kirjaimet_label.configure(text="")
        self.__arvattava_sana_label.configure(text="".join(self.__arvattu_sana))

        # listään ensimmäienen hirsipuu-kuva näytölle
        self.__kuva_label.configure(image=self.__kuva)

    def word_guess(self, guessed_letter):
        """

        :param guessed_letter: str, käyttäjän arvaama kirjain
        :return: None
        """
        # jos kirjain on jo arvattu tai peli on jo loppunut, niin
        # ei tehdä mitään
        if guessed_letter in self.__arvatut_kirjaimet or self.__lopputulos:
            return

        # jos kirjain on arvattavassa sanassa
        elif guessed_letter.lower() in self.__arvattava_sana:
            # kutsutaan arvatun kirjaimen vaihtamiseen tehty funktio
            self.change_guessed_letter(guessed_letter.lower())
            # lisätään arvattu kirjain arvattuihin kirjaimiin
            self.add_letter(guessed_letter)

        else:
            # lisätään arvattu kirjain arvattuihin kirjaimiin
            self.add_letter(guessed_letter)
            self.__arvaukset -= 1
            # vaihdetaan kuva seuraavaan
            self.image_changer()
            # jos pelaaja häviää pelin
            if self.__arvaukset == 0:
                self.game_over()

    def change_guessed_letter(self, guessed_letter):
        """
        metodi oikein arvatun kirjaimen paljastamiseen
        self.__arvattava_sana_label:iin
        :param guessed_letter: str, käyttäjän arvaama kirjain
        :return: None
        """
        # etsitään ja lisätään arvatut kirjaimet
        for count, letter in enumerate(self.__arvattava_sana):
            if letter == guessed_letter:
                self.__arvattu_sana[count] = letter
        self.__arvattava_sana_label.configure(text="".join(self.__arvattu_sana).upper())
        if "".join(self.__arvattu_sana) == self.__arvattava_sana:
            self.__lopputulos = "win"
            self.popup()

    def add_letter(self, letter):
        """
        metodi kirjainten lisäämiseen self.__arvatut_kirjaimet listaan
        :param letter: str, käyttäjän arvaama kirjain
        :return: None
        """
        self.__arvatut_kirjaimet.append(letter.upper())
        self.__arvatut_kirjaimet_label.configure(text=", ".join(self.__arvatut_kirjaimet))
        # Lisätään jokaisen kuuden sanan jälkeen rivinvaihto tilan säästämiseksi
        if len(self.__arvatut_kirjaimet) % 6 == 0:
            self.__arvatut_kirjaimet[-1] += "\n"

    def game_over(self):
        """
        metodi jos käyttääjä häviää pelin
        :return: None
        """
        # paljastetaan arvattava sana
        self.__arvattava_sana_label.configure(text=self.__arvattava_sana.upper())
        self.__lopputulos = "lose"
        # muodostetaan pop-up ikkuna
        self.popup()

    def image_changer(self):
        """
        metodi kuvan hirsipuukuvan vaihtamiseen
        :return: None
        """
        # valitaan kuva sen perusteella kuinka monta arvausta
        # käyttäjällä on jäljellä
        self.__kuva = PhotoImage(file=f"hirsipuu{13-self.__arvaukset}.png")
        self.__kuva_label.configure(image=self.__kuva)

    def popup(self):
        """
        metodi pop-up ikkunalle
        :return: None
        """
        # luodaan uusi ikkuna
        window = tkinter.Toplevel()
        lopputulos_kuva_label = Label(window)
        # tarkastetaan voittiko vai hävisikö käyttäjä pelin
        # ja valitaan näytettävä kuva sen perusteella
        if self.__lopputulos == "win":
            kuva = PhotoImage(file="voitto.png")

        else:
            kuva = PhotoImage(file="havio.png")
        # lisätään kuva näytölle
        lopputulos_kuva_label.configure(image=kuva)
        lopputulos_kuva_label.grid(row=0, column=0, columnspan=3)

        # lisätään myös nappi ikkunasta poistumiselle
        close_button = Button(window, text="Sulje", command=window.destroy)
        close_button.grid(row=1, column=2)
        # käynnistetään pop-up ikkuna
        window.mainloop()

    def kirjain(self, letter):
        """
        metodi kirjain-näppäimille, joka aktivoituu kun
        kirjain-näppäintä painetaan
        :param letter:
        :return:
        """
        self.word_guess(letter)


def main():
    Hirsipuu()


if __name__ == "__main__":
    main()
