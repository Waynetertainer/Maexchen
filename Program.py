""" A game of "Mäxchen".

 Shoud be started via the program "Startup". """

import random as rnd
from os import system

__author__ = "Tobias, 7232927, Schott, 7040759"
__credits__ = ""
__email__ = "s0798915@rz.uni-frankfurt.de, s7296105@stud.uni-frankfurt.de"

history = []


class Options:
    """ An object for storing the options during the game. """

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
        """ Resets all values to default. """

        self.value_m = (2, 1)
        self.value_h = (4, 2)
        self.shuffle_player = True
        self.dice_order = True
        self.max_points = 10
        self.points_s = 1
        self.points_m = 2
        self.points_h = 3
        self.god_mode = {}


def get_dice_list(options):
    """ Returns the actual order of dice. """

    higher_dice_values = [(2, 1), (3, 1), (3, 2), (4, 1), (4, 2), (4, 3),
                          (5, 1),
                          (5, 2), (5, 3), (5, 4), (6, 1), (6, 2), (6, 3),
                          (6, 4),
                          (6, 5), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5),
                          (6, 6)]
    unsorted_dice_values = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                            (2, 1), (2, 3), (2, 4), (2, 5), (2, 6),
                            (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
                            (4, 1), (4, 2), (4, 3), (4, 5), (4, 6),
                            (5, 1), (5, 2), (5, 3), (5, 4), (5, 6),
                            (6, 1), (6, 2), (6, 3), (6, 4), (6, 5),
                            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
    if options.dice_order:
        return [dice for dice in higher_dice_values if
                dice != options.value_m and
                dice != options.value_h] + [
                   options.value_m] + [
                   options.value_h]
    else:
        return [dice for dice in unsorted_dice_values if
                dice != options.value_m and
                dice != options.value_h] + [
                   options.value_m] + [
                   options.value_h]


def menu_options(options):
    """ Manages the options menu. """

    while True:
        options_choice = input(
            """Was möchten Sie tun?
            x, um ins Hauptmenü zurückzukehren.
            m, um den Wert von Mäxchen zu verändern.
            h, um den Wert von Hamburger zu verändern.
            sp, um den Standartpunktabzug zu ändern.
            mp, um den Punktabzug für Mäxchen zu verändern.
            hp, um den Punktabzug für Hamburger zu verändern.
            p, um die Punkte zu Spielbegin zu ändern.
            s, um das Mischen der Spielerreihenfolge zu Beginn zu \
(de)aktivieren.
            o, um die Sortierung der Würfel zu (de)aktivieren.
            r, um alle Optionen zu resetten.""").lower()
        # Returns from options.
        system("cls")
        if options_choice == "x":
            return
        # Resets all options.
        elif options_choice == "r":
            system("cls")
            options.reset()
            print("Alle Optionen wurden zurückgesetzt.")
        # Changes the value of Mäxchen.
        elif options_choice == "m":
            system("cls")
            while True:
                value = input(
                    "Auf welchen Wert soll Mäxchen geändert werden? " +
                    "(2 Zahlen mit Komma getrennt eingeben)")
                system("cls")
                if len(value.split(sep=',')) == 2 and (
                        int(value.split(sep=',')[0]),
                        int(value.split(sep=',')[1])) in get_dice_list(
                    options):
                    options.value_m = (
                        int(value.split(sep=',')[0]),
                        int(value.split(sep=',')[1]))
                    print("Mäxchen hat nun den Wert", options.value_m)
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes the value of Hamburger.
        elif options_choice == "h":
            system("cls")
            while True:
                value = input(
                    "Auf welchen Wert soll Hamburger geändert werden? " +
                    "(2 Zahlen mit Komma getrennt eingeben)")
                system("cls")
                if (int(value.split(sep=',')[0]),
                    int(value.split(sep=',')[1])) in get_dice_list(options):
                    options.value_h = (
                        int(value.split(sep=',')[0]),
                        int(value.split(sep=',')[1]))
                    print("Hamburger hat nun den Wert", options.value_h)
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes points to deduct for standart case.
        elif options_choice == "sp":
            system("cls")
            while True:
                value = input(
                    "Welchen Punktabzug soll es im Standartfall geben?")
                system("cls")
                if value.isdigit() and int(value) >= 0:
                    options.points_s = int(value)
                    print("Im Standartfall werden nun", options.points_s,
                          "Punkte abgezogen.")
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes points to deduct for Mäxchen.
        elif options_choice == "mp":
            system("cls")
            while True:
                value = input("Welchen Punktabzug soll es für Mäxchen geben?")
                system("cls")
                if value.isdigit() and int(value) >= 0:
                    options.points_m = int(value)
                    print("für Mäxchen werden nun", options.points_m,
                          "Punkte abgezogen.")
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes points to deduct for Hamburger.
        elif options_choice == "hp":
            system("cls")
            while True:
                value = input(
                    "Welchen Punktabzug soll es für Hamburger geben?")
                system("cls")
                if value.isdigit() and int(value) >= 0:
                    options.points_h = int()
                    print("Für Mäxchen werden nun", options.points_h,
                          "Punkte abgezogen.")
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes to amount of points the players start with.
        elif options_choice == "p":
            system("cls")
            while True:
                value = input(
                    "Mit wie vielen Punkten sollen die Spieler starten?")
                system("cls")
                if value.isdigit() and int(value) >= 0:
                    options.max_points = int(value)
                    print("Die Spieler starten nun mit", options.max_points,
                          "Punkte.")
                    break
                else:
                    print("Eingabe ungültig.")
        # Changes whether to mix the order of players at start.
        elif options_choice == "s":
            system("cls")
            while True:
                user_input = input(
                    "Soll die Spielerreihenfolge zu Begin gemischt werden?\
(j/n)")
                system("cls")
                if user_input == "j":
                    options.shuffle_player = True
                    break
                elif user_input == "n":
                    options.shuffle_player = False
                    break
                else:
                    print("Eingabe ungültig.")
            if options.shuffle_player:
                print("Die Spielerreihenfolge wird zu Begin gemischt")
            else:
                print("Die Spielerreihenfolge wird zu Begin nicht gemischt.")
        # Changes whether the dice should be ordered or not.
        elif options_choice == "o":
            system("cls")
            while True:
                user_input = input(
                    "Soll die Sortierung der Würfel optmiert werden? (j/n)")
                system("cls")
                if user_input == "j":
                    options.dice_order = True
                    break
                elif user_input == "n":
                    options.dice_order = False
                    break
                else:
                    print("Eingabe ungültig.")
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
    middle = chr(0x2503) + chr(32) * 4 + chr(0x20DD) + chr(32) * 4 + chr(
        0x2503)
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
    """ Creates a tupel of two numbers between 1 and 6 representing two dice.

    """

    dice1 = rnd.randint(1, 6)
    dice2 = rnd.randint(1, 6)
    if sort:
        return tuple(sorted((dice1, dice2), reverse=True))
    else:
        return dice1, dice2


def compare(options, own_dice, other_dice):
    """ Determines the higher roll of two pairs of dice.

    Returns whether the first given pair of dice is higher than the second
    pair.
    """

    dice_list = get_dice_list(options)
    return dice_list.index(own_dice) > dice_list.index(other_dice)


def create_table(options, players):
    """ Creates a history for the points of each player in each round. """

    system("cls")
    point_history = dict.fromkeys([p[0] for p in players], options.max_points)
    print("{:6}".format("Round"), end="")
    for name in point_history.keys():
        print("|", "{:>10}".format(name + " "), end="")
    print()
    iterator = 1
    for item in history:
        if item[2] in point_history.keys():
            point_history.update({item[2]: point_history[item[2]] - item[3]})
        print("{:6}".format(iterator), end="")
        for value in point_history.values():
            print("|", "{:>10}".format(str(value) + " "), end="")
        print()
        iterator += 1


def gameround(options, player, players):
    """ Manages the round of one player. """

    # round_data has 6 components with the following meanings:
    # [0] : Current player name.
    # [1] : Reset of streak to beat the previous player.
    # [2] : Name of player who lost points.
    # [3] : Amount of points lost.
    # [4] : Actual thrown dice.
    # [5] : Said thrown dice.
    round_data = [player[0], False, "", 0, (0, 0), (0, 0)]
    print(player[0], "ist an der Reihe.")
    input("Bestätigen, um die Runde zu beginnen")
    # Asks the player whether he wants to believe the previous player.
    if len(history) != 0 and not history[len(history) - 1][1]:
        previous_round_data = history[len(history) - 1]
        while True:
            system("cls")
            name = ""
            if previous_round_data[5] == options.value_m:
                name = " Mäxchen"
            elif previous_round_data[5] == options.value_h:
                name = " Hamburger"
            print(previous_round_data[0],
                  "behauptet" + name + " geworfen zu haben:")
            visualize(previous_round_data[5])
            believe = input("Glauben Sie das? (j/n)").lower()
            if believe == "j":
                break
            elif believe == "n":
                if previous_round_data[4] == options.value_m:
                    name = "Mäxchen"
                elif previous_round_data[4] == options.value_h:
                    name = "Hamburger"
                else:
                    name = "folgendes"
                print("Tatsächlich hat", previous_round_data[0],
                      name, "geworfen:")
                visualize(previous_round_data[4])
                # Points to deduct.
                if previous_round_data[4] == options.value_m:
                    round_data[3] = options.points_m
                elif previous_round_data[4] == options.value_h:
                    round_data[3] = options.points_h
                else:
                    round_data[3] = options.points_s
                # Previous player lied.
                if compare(options, previous_round_data[5],
                           previous_round_data[4]):
                    if options.god_mode[previous_round_data[0]]:
                        round_data[3] = 0
                    print(previous_round_data[0], "hat gelogen!")
                    round_data[2] = previous_round_data[0]
                    previous_player = \
                        [p for p in players if p[0] == previous_round_data[0]][
                            0]
                    previous_player[2] -= round_data[3]
                    print(previous_round_data[0], "hat", round_data[3],
                          "Punkte verloren und damit nur noch",
                          previous_player[2],
                          "Punkte.")
                # Previous player said the truth or said a smaller number.
                else:
                    if options.god_mode[round_data[0]]:
                        round_data[3] = 0
                    print(previous_round_data[0], "hat die Wahrheit gesagt!")
                    round_data[2] = round_data[0]
                    player[2] -= round_data[3]
                    print(player[0], "hat", round_data[3],
                          "Punkte verloren und damit nur noch", player[2],
                          "Punkte.")

                break
            else:
                print("Eingabe ungültig.")
    # Asks whether the player wants to cheat.
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
    if round_data[4] == options.value_m:
        name = " Mäxchen"
    elif round_data[4] == options.value_h:
        name = " Hamburger"
    else:
        name = ""
    print("Sie haben" + name + " gewürfelt:")
    visualize(round_data[4])
    # Asks whether the player wants to lie.
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
    # Checks whether the player beat the previous player.
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
                player[2] -= round_data[3]
                print(player[0], "hat", round_data[3],
                      "Punkte verloren und damit nur noch", player[2],
                      "Punkte.")
                print("Zu schlagende Würfel zurückgesetzt.")
                round_data[1] = True
    history.append(round_data)
    input("Zum Beenden der Runde bestätigen.")
    system("cls")


def computer_gameround(options, player, players):
    """ Manages the round of the computer player. """

    round_data = [player[0], False, "", 0, (0, 0), (0, 0)]
    print(player[0], "ist an der Reihe.")
    # Determines whether the computer believes the previous player.
    if len(history) != 0 and not history[-1][1]:
        previous_round_data = history[-1]
        if previous_round_data[5] == options.value_h:
            chance_not_to_believe = 1
        else:
            chance_not_to_believe = 0.4
            if previous_round_data[5] == options.value_m:
                chance_not_to_believe += 0.275
            if len(history) >= 2 and not history[-2][1]:
                dice_list = get_dice_list(options)
                if dice_list.index(history[-1][5]) == \
                        dice_list.index(history[-2][5]) + 1:
                    chance_not_to_believe += 0.275
            if player[2] <= 3:
                chance_not_to_believe -= 0.275
        # Computer does not believe the previous player.
        if rnd.random() < chance_not_to_believe:
            print("Der Computer glaubt", previous_round_data[0], "nicht.")
            if previous_round_data[4] == options.value_m:
                round_data[3] = options.points_m
            elif previous_round_data[4] == options.value_h:
                round_data[3] = options.points_h
            else:
                round_data[3] = options.points_s
            # Previous player lied.
            if compare(options, previous_round_data[5],
                       previous_round_data[4]):
                if options.god_mode[previous_round_data[0]]:
                    round_data[3] = 0
                round_data[2] = previous_round_data[0]
                previous_player = \
                    [p for p in players if p[0] == previous_round_data[0]][0]
                previous_player[2] -= round_data[3]
                print(previous_round_data[0], "hat", round_data[3],
                      "Punkte verloren und damit nur noch", previous_player[2],
                      "Punkte.")
            # Previous player said the truth or said a smaller number.
            else:
                round_data[2] = round_data[0]
                player[2] -= round_data[3]
                print("Der Computer hat", round_data[3],
                      "Punkte verloren und damit nur noch", player[2],
                      "Punkte.")
        else:
            print("Der Computer glaubt", previous_round_data[0])

    round_data[4] = throw_dice(options.dice_order)
    dice_list = get_dice_list(options)
    # Determines whether the computer lies.
    # 10% chance to lie if the dice of the computer are not high.
    if dice_list.index(round_data[4]) < 0.75 * len(dice_list):
        lie = rnd.random() < 0.1
    else:
        lie = False
    # 100% chance to lie if rolled dice are smaller than needed.
    if len(history) != 0 and not history[-1][1] and \
            not compare(options, round_data[4], history[-1][5]):
        lie = True
    if lie:
        if len(history) != 0 and round_data[2] == "":
            # Previous round cant be Hamburger, because the computer
            # would have uncovered it earlier.
            round_data[5] = rnd.choice(
                dice_list[dice_list.index(history[-1][4]) + 1:])
        else:
            round_data[5] = rnd.choice(
                dice_list[dice_list.index(round_data[4]) + 1:])
    else:
        round_data[5] = round_data[4]
    # Checks whether the computer beat the previous player.
    if len(history) != 0:
        previous_round_data = history[-1]
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
                round_data[1] = True
    history.append(round_data)


def game(options):
    """ Manages a complete game of Mäxchen. """

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
        # Adds a user.
        if user_choice == "+":
            players.append([
                input("Bitte Spielernamen eingeben: "), False,
                options.max_points])
            system("cls")
        # Adds or removes the computer.
        elif user_choice == "c":
            computer = not computer
            if computer:
                print("Der Computergegner ist nun aktiviert.")
            else:
                print("Der Computergegner ist nun deaktiviert.")
        # Starts the game.
        elif user_choice == "s":
            if computer:
                players.append(["Computer", True, options.max_points])
            if options.shuffle_player:
                rnd.shuffle(players)
            if len(players) >= 2:
                print("Die Spielreihenfolge ist", [p[0] for p in players])
                options.god_mode = dict.fromkeys([p[0] for p in players],
                                                 False)
                iterator = 0
                iterator_prefix = 1
                # Defines the core game loop.
                while True:
                    active_players = [p for p in players if p[2] >= 1]
                    if len(active_players) <= 1:
                        break
                    player = active_players[iterator % len(active_players)]
                    if player[1]:
                        computer_gameround(options, player, players)
                    else:
                        gameround(options, player, players)
                    if history[len(history) - 1][3] == options.points_h or \
                            history[len(history) - 1][3] == options.points_m:
                        iterator_prefix *= -1
                    iterator += iterator_prefix
                print([p for p in players if p[2] >= 1][0][0],
                      "hat gewonnen!")
                create_table(options, players)
                return
            else:
                print("Zu wenige Spieler.")
        # Closes the game.
        elif user_choice == "x":
            return
        else:
            print("Eingabe ungültig.")


def main():
    """ Manages the main menu of the game. """

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
