
symboleJoueur1 = "X"
symboleJoueur2 = "O"


def recupererSymbole(numeroJoueur):
    "Récupérer le symbole en fonction du numéro du joueur donné"
    if numeroJoueur == 1:  # Si le numéro du joueur est 1
        return symboleJoueur1  # Retourner le symbole du joueur 1

    elif numeroJoueur == 2:  # Si le numéro du  joueur est 2
        return symboleJoueur2

    else:  # Dans tous les autres cas
        return " "  # Retourner un espace


def initialiserGrille():
    "Initialiser la grille du jeu"
    global grille  # On déclare la variable grille comme étant globale afin de pouvoir l'utiliser dans les autres fonctions du programme
    grille = [[0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0]
              ]  # Liste de listes représentant la grille du jeu. Pour chaque case : 0 = aucun jeton, 1 = jeton du joueur 1, 2 = jeton du joueur 2


def afficherGrille():
    "Afficher la grille du jeu"
    for ligne in grille:  # Pour chaque ligne  de la grille
        for case in ligne:  # Pour chaque case de la ligne courante
            # Afficher le symbole de la case
            print("|", end=" ")
            print(recupererSymbole(case), end=" ")

        print("|")
    print("  0   1   2   3   4   5   6")


def afficherFinDePartie(gagnant):
    "Afficher un message indiquant au joueur gagnant qu'il gagné la partie"
    afficherGrille()

    if gagnant == 1 or gagnant == 2:
        print("Bravo joueur n°", gagnant, "vous avez gagné la partie !")

    elif gagnant == 0:
        print("Match nul !")


initialiserGrille()
# afficherGrille()


def joueurGagne(joueur):
    "Vérifier si le joueur donné en paramètre a gagné la partie"
    pass


def verifierGrillePleine():
    "Vérifier si la grille du jeu est pleine"
    pass


def verifierHorizontalement(joueur):
    "Vérifier si le joueur passé en paramètre a placé 4 jetons horizontalement"
    # Nombre de fois où le numéro du joueur apparaît 4 fois de suite dans la ligne
    n_apparition_num_joueur = 0
    for ligne in grille:  # Pour chaque ligne de la grille
        for case in ligne:  # Pour chaque case de la ligne
            if joueur == case:  # Si le numéro du joueur apparaît dans la ligne
                # Augmenter le nombre de fois où l'on a vus le numéro du joueur
                n_apparition_num_joueur += 1
            else:
                n_apparition_num_joueur = 0

            if n_apparition_num_joueur == 4:  # Si le numéro du joueur apparaît 4 fois dans la ligne
                return True  # Alors le joueur a bien placé 4 jetons horizontalement

    return False  # Le joueur n'a pas placé 4 jetons horizontalement


def demanderColonne(joueur):
    "Demander au joueur donné en paramètre dans quelle colonne il souhaite placer un jeton"
    # Demander au joueur actuel dans quelle colonne placer un jeton
    colonne = int(input(
        "joueur n° {}, indiquez la colonne où vous souhaitez placer un jeton:".format(joueur)))

    if colonne < 0 or colonne > 6:
        while colonne < 0 or colonne > 6:
            print("joueur n° {}, la colonne {} est inexistante. Veuillez saisir de nouveau la colonne où vous souhaitez placer un jeton.".format(
                joueur, colonne))
            colonne = int(input(
                "joueur n° {},  indiquez la colonne où vous souhaitez placer un jeton:".format(joueur)))

    return colonne


def ligneLibreDeLaColonne(colonne):
    "Trouver la colonne libre la plus basse"

    # Pour chaque ligne comptée dans la colonne
    for i in range(len(grille)):
        # print(grille[i][colonne])
        # print(i)
        # print(grille[i][colonne])

        if grille[i][colonne] > 0:
            return i - 1
    return len(grille) - 1

    # Ajouter la ligne à la liste des lignes parcourues
    # liste_lignes_parcourues.append(ligne)
    # print(liste_lignes_parcourues)

    # Pour chaque numéro de ligne dans la liste


def boucleDeJeu():
    "Boucle principale du jeu"
    numero_joueur = 1  # Le premier joueur à jouer au début de la partie est le jouer n°1
   # while verifierGrillePleine() is not False:  # Tant que la grille n'est pas pleine
    while True:
        afficherGrille()  # Afficher la grille
        jouerLeTour(numero_joueur)  # Donner le tour au joueur actuel
        print(verifierHorizontalement(numero_joueur))

        if joueurGagne(numero_joueur):  # Si le joueur actuel gagne la partie
            return numero_joueur  # Retourner le numéro du joueur actuel

        else:
            if numero_joueur == 1:  # Si le joueur actuel est le joueur n°1
                numero_joueur = 2  # Passer le tour au joueur n°2

            if numero_joueur == 2:  # Si le joueur actuel est le joueur n°2
                numero_joueur = 1  # Passer le tour au joueur n°1

    return 0


def demanderRejouer():
    "Demander au joueur s'il souhaite démarrer de nouveau une partie"
    rejouer = input("Voulez-vous rejouer (o/n) ?")

    if rejouer == "o":
        return True

    elif rejouer == "n":
        return False

# coordonnees = (ligne, colonne)


def placerJeton(joueur, coordonnees):
    print(coordonnees)
    grille[coordonnees[0]][coordonnees[1]] = joueur

    afficherGrille()


# coordonnees = (ligne,colonne)


def jouerLeTour(joueur):
    "Donner le tour de jeu au joueur donné en paramètre"
    # Tant que le joueur demande la colonne -1, inexistante
    colonne = demanderColonne(joueur)
    ligne = ligneLibreDeLaColonne(colonne)
    while ligne == -1:
        print("Joueur n°{}, la colonne choisie n'est plus libre.".format(joueur))
        colonne = demanderColonne(joueur)  # Demander à nouveau la colonne
        ligne = ligneLibreDeLaColonne(colonne)

    placerJeton(joueur, (ligne, colonne))


def jeu():
    "Fonction qui lance le jeu"
    while demanderRejouer() == True:  # Tant que le joueur veut jouer
        initialiserGrille()  # Initialiser la grille
        boucleDeJeu()  # Effectuer les instructions du jeu en boucle
        # Afficher le message de fin de partie
        afficherFinDePartie(boucleDeJeu)

        if demanderRejouer() == False:  # Si le joueur décide d'arrêter de jouer
            # Afficher "Au revoir !" sur l'écran du joueur
            print("Au revoir !")


jeu()
