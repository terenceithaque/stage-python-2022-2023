def bonjour(prenom, nom):
    print("Bonjour {} {} !".format(prenom, nom))


bonjour("Térence", "Le Thierry")


def somme(nombre1, nombre2):
    return nombre1 + nombre2


print(somme(15, 15))


def minimum(nombre1, nombre2):
    if nombre1 < nombre2:
        return nombre1
    elif nombre2 < nombre1:
        return nombre2


print(minimum(15, 11))


def puissance(nombre1, nombre2):
    return nombre1 * nombre2


print(puissance(4, 5))


def fibonnaci(nombre):
    print("Nombre =", nombre)
    if nombre == 0:
        return 0
    elif nombre == 1:
        return 1
    else:
        return fibonnaci(nombre - 1) + fibonnaci(nombre - 2)


print(fibonnaci(11))


def menu():
    nom_fonctions = ["bonjour", "somme", "minimum", "puissance", "fibonnaci"]
    fonction = input(
        "Exécuter une fonction. Fonctions possibles {}".format(nom_fonctions))
    print(fonction)
    if fonction == nom_fonctions[0]:
        prenom = input(
            "Votre prénom :")
        nom = input("Votre nom :")

        print(bonjour(prenom, nom))
    elif fonction == nom_fonctions[1]:
        nombre1 = input("1er nombre :")
        nombre1 = int(nombre1)

        nombre2 = input("Deuxième nombre :")
        nombre2 = int(nombre2)
        print(somme(nombre1, nombre2))
    elif fonction == nom_fonctions[2]:
        nombre1 = input("1er nombre :")
        nombre1 = int(nombre1)

        nombre2 = input("2ème nombre :")
        nombre2 = int(nombre2)
        print(minimum(nombre1, nombre2))
    elif fonction == nom_fonctions[3]:

        nombre1 = input("1er nombre :")
        nombre1 = int(nombre1)

        nombre2 = input("2ème nombre :")
        nombre2 = int(nombre2)

        print(puissance(nombre1, nombre2))
    elif fonction == nom_fonctions[4]:
        nombre = input("Un seul nombre :")
        nombre = int(nombre)
        print(fibonnaci(nombre))


menu()
