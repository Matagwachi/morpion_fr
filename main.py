"""
    Les règles du jeu pour jouer au jeu de morpion en ligne (tic tac toe en anglais) sont les suivantes :
    Dans sa version classique, le plateau de jeu est constitué de 9 cases (carré de 3x3).
    Ce jeu se joue à deux et le but est d'aligner trois symboles identiques (croix et cercle) pour gagner la partie.
    Chaque joueur trace tour à tour son symbole dans une case et le premier qui aligne verticalement,
    horizontalement ou en diagonale ses symboles gagne la partie.
"""

from morpion import Morpion
from ia import IA

def levelSelection():
    game = input("0 - J1 vs J2\n1 - J1 vs IA (level 0)\nChoisissez votre niveau (0/1):")
    return game


def startConsole():
    morpion = Morpion()
    robot = None

    level = [0, 1]
    game = levelSelection()

    if game not in level:
        game = levelSelection()

    if game != '0':
        robot = IA(0, 2)

    while ((morpion.winner() == False) or (morpion.nul() == False)):
        morpion.print()

        print("Au joueur 1 de jouer")

        while (1):
            ligne = int(input("Ligne ?(1/2/3)"))
            colonne = int(input("Colonne ?(1/2/3)"))
            if morpion.play(1,ligne - 1,colonne - 1) == True:
                break

        morpion.print()
    
        print("Au joueur 2 de jouer")
        if robot:
            robot.playLevel0(morpion)
        else:
            while (1):
                ligne = int(input("Ligne ?(1/2/3)"))
                colonne = int(input("Colonne ?(1/2/3)"))
                if morpion.play(2, ligne - 1, colonne - 1) == True:
                    break

    morpion.print()

    restart = input("Voulez vous rejuer(y/n)")
    if (restart == 'y'):
        startConsole()

startConsole()

