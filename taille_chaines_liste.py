def taille_chaines(liste):

    dict_chaines = {}

    for index in range(len(liste)):
        dict_chaines[liste[index]] = len(liste[index])


    return dict_chaines 


taille_liste = int(input("Indiquez la taille de la liste à créer :"))

liste = []

while len(liste) < taille_liste:
    chaine = input("Tapez un mot ou une phrase :")
    liste.append(chaine)

print(taille_chaines(liste))

