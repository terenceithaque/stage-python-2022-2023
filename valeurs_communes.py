def valeurs_communes(liste1, liste2):
    liste_valeurs_communes = []
    for index in range(len(liste1)):
        for valeur in liste2:
            if valeur == liste1[index]:
               liste_valeurs_communes.append(valeur)

    return liste_valeurs_communes           
            

liste1 = list(input("Indiquez les valeurs à insérer dans la première liste :"))
liste2 = list(input("Indiquez les valeurs à insérer dans la deuxième liste :"))

print(valeurs_communes(liste1, liste2))