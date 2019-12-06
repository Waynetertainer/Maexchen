""" Creates random identities with name and address. """

import random as rnd
import os

__author__ = "Tobias, 7232927, Schott, 7040759"
__credits__ = ""
__email__ = "s0798915@rz.uni-frankfurt.de, s7296105@stud.uni-frankfurt.de"

standart_values = [(3, 1), (3, 2), (4, 1), (4, 3), (5, 1), (5, 2), (5, 3),
                   (5, 4), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (1, 1),
                   (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (2, 1), (4, 2)]
options = {"maexchen": (2, 1), "hamburger": (4, 2), }
standart_options = {"maexchen": (2, 1), "hamburger": (4, 2), }


def menu_options():
    while True:
        print(options)
        options_choice = input(
            """Was möchten Sie ändern?
            x, um ins Hauptmenü zurückzukehren.
            m für Mäxchen.
            h für Hamburger.""").lower()
        if options_choice == "x":
            return
        elif options_choice == "m":
            value = input(
                "Auf welchen Wert soll Mäxchen geändert werden? " +
                "2 Zahlen mit Komma getrennt eingeben)")
            options["maexchen"] = (
                int(value.split(sep=',')[0]), int(value.split(sep=',')[1]))


def visualize(dice1, dice2):
    """ Visualizes two given dice with Unicode Characters."""

    dice1 -= 1
    dice2 -= 1
    empty = chr(0x2503) + chr(32) * 9 + chr(0x2503)
    left = chr(0x2503) + chr(32) + chr(0x20DD) + chr(32) * 7 + chr(0x2503)
    left_right = chr(0x2503) + chr(32) + chr(0x20DD) + chr(32) * 5 + chr(
        0x20DD) + chr(32) + chr(0x2503)
    middle = chr(0x2503) + chr(32) * 4 + chr(0x20DD) + chr(32) * 4 + chr(0x2503)
    right = chr(0x2503) + chr(32) * 7 + chr(0x20DD) + chr(32) + chr(0x2503)
    line1 = chr(0x250F) + chr(0x2501) * 9 + chr(0x2513) + chr(32) + chr(
        0x250F) + chr(0x2501) * 9 + chr(0x2513)
    line2 = [empty, left, left, left_right, left_right, left_right]
    line3 = [middle, empty, middle, empty, middle, left_right]
    line4 = [empty, right, right, left_right, left_right, left_right]
    line5 = chr(0x2517) + chr(0x2501) * 9 + chr(0x251B) + chr(32) + chr(
        0x2517) + chr(0x2501) * 9 + chr(0x251B)

    print(line1, line2[dice1] + " " + line2[dice2],
          line3[dice1] + " " + line3[dice2], line4[dice1] + " " + line4[dice2],
          line5, sep="\n")


def gameround():
    pass


def game():
    pass


def main():
    """Docstring. """

    visualize(1, 6)
    while True:
        menu_choice = input(
            "Was möchtest du tun?\n"
            "o für Optionen, s, um ein Spiel zu starten, x zum Beenden.").lower()
        if menu_choice == 'o':
            menu_options()
        elif menu_choice == 's':
            pass
        elif menu_choice == 'x':
            return
        else:
            print("Eingabe ungültig.")


if __name__ == "__main__":
    main()
