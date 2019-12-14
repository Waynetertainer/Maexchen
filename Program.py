""" Creates random identities with name and address. """

import random as rnd
from os import system

__author__ = "Tobias, 7232927, Schott, 7040759"
__credits__ = ""
__email__ = "s0798915@rz.uni-frankfurt.de, s7296105@stud.uni-frankfurt.de"

# TODO Table at gameend

standart_values = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3), (5, 1),
                   (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3), (6, 4),
                   (6, 5), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
ordered_values = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                  (2, 1), (2, 3), (2, 4), (2, 5), (2, 6),
                  (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
                  (4, 1), (4, 2), (4, 3), (4, 5), (4, 6),
                  (5, 1), (5, 2), (5, 3), (5, 4), (5, 6),
                  (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
                  (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]

history = []


class Options:
    value_m = (2, 1)
    value_h = (4, 2)
    shuffle_player = True
    dice_order = True
    max_points = 10
    points_s = 1
    points_m = 2
    points_h = 3
    god_mode = {}

    def reset(self):
        self.value_m = (2, 1)
        self.value_h = (4, 2)
        self.shuffle_player = True
        self.dice_order = True
        self.max_points = 10
        self.points_s = 1
        self.points_m = 2
        self.points_h = 3
        self.god_mode = {}


def menu_options(options):
    while True:
        options_choice = input(
            """Was möchten Sie tun?
            x, um ins Hauptmenü zurückzukehren.
            m, um den Wert von Mäxchen zu verändern.
            h, um den Wert von Hamburger zu verändern.
            sp, um den standart Punktabzug zu ändern.
            mp, um den Punktabzug für Mäxchen zu verändern.
            hp, um den Punktabzug für Hamburger zu verändern.
            p, um die Punkte zu Spielbegin zu ändern.
            s, um das Mischen der Spielerreihenfolge zu begin zu (de)aktivieren.
            o, um die Sortierung der Würfel zu (de)aktivieren.
            r, um alle Optionen zu resetten.""").lower()
        if options_choice == "x":
            return
        elif options_choice == "r":
            system("cls")
            options.reset()
            print("Alle Optionen wurden zurückgesetzt.")
        elif options_choice == "m":
            system("cls")
            value = input(
                "Auf welchen Wert soll Mäxchen geändert werden? " +
                "(2 Zahlen mit Komma getrennt eingeben)")
            options.value_m = (
                int(value.split(sep=',')[0]), int(value.split(sep=',')[1]))
            system("cls")
            print("Mäxchen hat nun den Wert", options.value_m)
        elif options_choice == "h":
            system("cls")
            value = input(
                "Auf welchen Wert soll Hamburger geändert werden? " +
                "(2 Zahlen mit Komma getrennt eingeben)")
            options.value_h = (
                int(value.split(sep=',')[0]), int(value.split(sep=',')[1]))
            system("cls")
            print("Hamburger hat nun den Wert", options.value_h)
        elif options_choice == "sp":
            system("cls")
            options.points_s = int(
                input("Welchen Punktabzug soll es im Standartfall geben?"))
            system("cls")
            print("Im Standartfall werden nun", options.points_s,
                  "Punkte abgezogen.")
        elif options_choice == "mp":
            system("cls")
            options.points_m = int(
                input("Welchen Punktabzug soll es für Mäxchen geben?"))
            system("cls")
            print("für Mäxchen werden nun", options.points_m,
                  "Punkte abgezogen.")
        elif options_choice == "hp":
            system("cls")
            options.points_h = int(
                input("Welchen Punktabzug soll es für Hamburger geben?"))
            system("cls")
            print("Für Mäxchen werden nun", options.points_h,
                  "Punkte abgezogen.")
        elif options_choice == "p":
            system("cls")
            options.max_points = int(
                input("Mit wie vielen Punkten sollen die Spieler starten?"))
            system("cls")
            print("Die Spieler starten nun mit", options.max_points,
                  "Punkte.")
        elif options_choice == "s":
            system("cls")
            user_input = input(
                "Soll die Spielerreihenfolge zu Begin gemischt werden? (j/n)")
            if user_input == "j":
                options.shuffle_player = True
            elif user_input == "n":
                options.shuffle_player = False
            system("cls")
            if options.shuffle_player:
                print("Die Spielerreihenfolge wird zu Begin gemischt")
            else:
                print("Die Spielerreihenfolge wird zu Begin nicht gemischt.")
        elif options_choice == "o":
            system("cls")
            user_input = input(
                "Soll die Sortierung der Würfel optmiert werden? (j/n)")
            if user_input == "j":
                options.dice_order = True
            elif user_input == "n":
                options.dice_order = False
            system("cls")
            if options.dice_order:
                print("Es wird immer die höchstmögliche Kombination genommen")
            else:
                print("Die Reihenfolge der Würfel ist stets festgelegt.")


def visualize(dice):
    """ Visualizes two given dice with Unicode Characters."""

    dice1 = dice[0]
    dice2 = dice[1]
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


def throw_dice(sort):
    dice1 = rnd.randint(1, 6)
    dice2 = rnd.randint(1, 6)
    if sort:
        return tuple(sorted((dice1, dice2), reverse=True))
    else:
        return dice1, dice2


def compare(options, own_dice, other_dice):
    if other_dice == options.value_h:
        return False
    if other_dice == options.value_m:
        return own_dice == options.value_h
    if own_dice == options.value_h or own_dice == options.value_m:
        return True
    if options.dice_order:
        return standart_values.index(own_dice) > standart_values.index(
            other_dice)
    else:
        return ordered_values.index(own_dice) > ordered_values.index(other_dice)


def gameround(options, player, players):
    round_data = [player[0], False, "", 0, (0, 0), (0, 0)]
    print(player[0], "ist an der Reihe.")
    input("Bestätigen, um die Runde zu beginnen")
    system("cls")
    if len(history) != 0 and not history[len(history) - 1][1]:
        previous_round_data = history[len(history) - 1]
        while True:
            system("cls")
            print(previous_round_data[0], "behauptet geworfen zu haben:")
            visualize(previous_round_data[5])
            believe = input("Glauben Sie das? (j/n)").lower()
            if believe == "j":
                break
            elif believe == "n":
                print("Tatsächlich hat", previous_round_data[0],
                      "folgendes geworfen:")
                visualize(previous_round_data[4])
                # Points to deduct.
                if previous_round_data[4] == options.value_m:
                    round_data[3] = options.points_m
                elif previous_round_data[4] == options.value_h:
                    round_data[3] = options.points_h
                else:
                    round_data[3] = options.points_s
                # Previous player said the truth.
                if previous_round_data[4] == previous_round_data[5]:
                    if options.god_mode[round_data[0]]:
                        round_data[3] = 0
                    print(previous_round_data[0], "hat die Wahrheit gesagt!")
                    round_data[2] = round_data[0]
                    [p for p in players if p[0] == round_data[0]][0][2] -= \
                        round_data[3]
                    print(player[0], "hat", round_data[3], "Punkte verloren")
                # Previous player lied.
                else:
                    if options.god_mode[previous_round_data[0]]:
                        round_data[3] = 0
                    print(previous_round_data[0], "hat gelogen!")
                    round_data[2] = previous_round_data[0]
                    [p for p in players if p[0] == round_data[0]][0][2] -= \
                        previous_round_data[3]

                    print(previous_round_data[0], "hat", round_data[3],
                          "Punkte verloren")
                break
            else:
                print("Eingabe ungültig.")

    cheat = input("""Möchten Sie einen Cheat aktivieren?
    h für Hamburger,
    m für Mäxchen,
    g für God Mode,
    jede andere Eingabe, um keinen Cheat zu aktivieren.""").lower()
    if cheat == "h":
        round_data[4] = options.value_h
    elif cheat == "m":
        round_data[4] = options.value_m
    elif cheat == "g":
        options.god_mode.update({player[0]: not options.god_mode[player[0]]})
        if options.god_mode[player[0]]:
            print("God Mode aktiviert.")
        else:
            print("God Mode deaktiviert.")
        round_data[4] = throw_dice(options.dice_order)
    else:
        round_data[4] = throw_dice(options.dice_order)
    print("Sie haben gewürfelt:")
    visualize(round_data[4])
    while True:
        lie = input("Möchten Sie lügen? (j/n)")
        if lie == "j":
            new_dice = input(
                "Auf welchen Wert sollen die Würfel geändert werden? " +
                "(2 Zahlen mit Komma getrennt eingeben)")
            round_data[5] = (
                int(new_dice.split(sep=',')[0]),
                int(new_dice.split(sep=',')[1]))
            break
        elif lie == "n":
            round_data[5] = round_data[4]
            break
        else:
            print("Eingabe ungültig.")
    if len(history) != 0:
        previous_round_data = history[len(history) - 1]
        if round_data[2] == "" and not previous_round_data[1]:
            if not compare(options, round_data[5], previous_round_data[5]):
                if options.god_mode[player[0]]:
                    round_data[3] = 0
                elif previous_round_data[5] == options.value_m:
                    round_data[3] = options.points_m
                elif previous_round_data[5] == options.value_h:
                    round_data[3] = options.points_h
                else:
                    round_data[3] = options.points_s

                round_data[2] = round_data[0]
                [p for p in players if p[0] == round_data[0]][0][2] -= \
                    round_data[3]
                print(player[0], "hat", round_data[3], "Punkte verloren")
                print("Zu schlagende Würfel zurückgesetzt.")
                round_data[1] = True
    history.append(round_data)
    input("Zum Beenden der Runde bestätigen.")
    system("cls")


def game(options):
    players = []
    computer = False
    system("cls")
    while True:
        user_choice = input("""Was möchten Sie tun? 
        +, um einen Spieler hinzuzufügen. 
        c, um den Computergegner zu (de)aktivieren. 
        s, um das Spiel zu starten. 
        x, um zurückzukehren. """)
        system("cls")
        if user_choice == "+":
            players.append([
                input("Bitte Spielernamen eingeben: "), False,
                options.max_points])
            system("cls")
        elif user_choice == "c":
            computer = not computer
            if computer:
                print("Der Computergegner ist nun aktiviert.")
            else:
                print("Der Computergegner ist nun deaktiviert.")
        elif user_choice == "s":
            if computer:
                players.append(["Computer", True, options.max_points])
            if options.shuffle_player:
                rnd.shuffle(players)
            print("Die Spielreihenfolge ist", [p[0] for p in players])
            options.god_mode = dict.fromkeys([p[0] for p in players], False)
            iterator = 0
            iterator_prefix = 1
            while True:
                active_players = [p for p in players if p[2] > 1]
                if len(active_players) <= 1:
                    break
                player = active_players[iterator % len(active_players)]
                if player[1]:
                    pass  # Is computer.
                else:
                    gameround(options, player, players)
                if history[len(history) - 1][3] == options.points_h or \
                        history[len(history) - 1][3] == options.points_m:
                    iterator_prefix *= -1
                iterator += iterator_prefix
            print([p for p in players if p[2] > 1][0][0],
                  "hat gewonnen!")
            return
        elif user_choice == "x":
            return
        else:
            print("Eingabe ungültig.")


def main():
    """Docstring. """

    options = Options()
    while True:
        system("cls")
        menu_choice = input(
            "Was möchten Sie tun?\n"
            "o für Optionen, s, um ein Spiel zu erstellen, x zum Beenden.") \
            .lower()
        if menu_choice == 'o':
            menu_options(options)
        elif menu_choice == 's':
            game(options)
        elif menu_choice == 'x':
            return
        else:
            print("Eingabe ungültig.")


if __name__ == "__main__":
    main()
