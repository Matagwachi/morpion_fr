def init_plateau():
    new_plateau = [[0 for k in range(0, 3)] for k in range(0, 3)]
    return new_plateau

class Morpion:
    def __init__(self):
        self.plateau = init_plateau()

    def play(self, joueur, ligne, colonne):
        if joueur == 0:
            print("Préciser un joueur: joueur 0 n'existe pas")
            return False
        if ((((ligne < 0) or (ligne > 2)) or ((colonne < 0) or (colonne > 2)))):
            print("Vous ne pouvez pas jouer la")
            return False

        if (self.plateau[ligne][colonne] != 0):
            print("Vous ne pouvez pas jouer la")
            return False

        #on remplie le tableau
        self.plateau[ligne][colonne] = joueur

        return True

    def print(self):
        #Le joueur 1 aura une croix  X et le joueur 2 un rond O
        symbole = ['|   ', '| X ' , '| O '] #en utilisant l'index du tableau
        print("  __1___2___3__")
        for k in range(0, 3): #ligne
            print("{} ".format(k+1), end='')
            for i in range(0, 3): #colonne
                print(symbole[self.plateau[k][i]], end='')
            print("|")
        print()# pour rajouter un saut de lligne en plus

    def winner(self):
        # On verifie chaque ligne en meme temps que chaque colonne
        for k in range(0, 3):
            if ((self.plateau[k][0] == self.plateau[k][1]) and (self.plateau[k][1] == self.plateau[k][2])):
                joueur = self.plateau[k][0]
                if joueur != 0:
                    print("Le joueur {} a gagner".format(joueur))
                    return True
            if ((self.plateau[0][k] == self.plateau[1][k]) and (self.plateau[1][k] == self.plateau[2][k])):
                joueur = self.plateau[0][k]
                if joueur != 0:
                    print("Le joueur {} a gagner".format(joueur))
                    return True


        # On vérifie les deux diagonales
        if ((self.plateau[0][0] == self.plateau[1][1]) and (self.plateau[1][1] == self.plateau[2][2])):
            joueur = self.plateau[0][0]
            if joueur != 0:
                print("Le joueur {} a gagner".format(joueur))
                return True
        if ((self.plateau[0][2] == self.plateau[1][1]) and (self.plateau[1][1] == self.plateau[2][0])):
            joueur = self.plateau[0][2]
            if joueur != 0:
                print("Le joueur {} a gagner".format(joueur))
                return True
        return False

    def nul(self):
        for k in range(0, 3):
            for i in range(0,3):
                if self.plateau == 0:
                    return False
        return True