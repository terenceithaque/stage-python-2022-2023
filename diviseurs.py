def diviseurs(nb):
    liste_diviseurs = []
    diviseurs = 1
    while diviseurs <= nb:
        if nb % diviseurs == 0:
            liste_diviseurs.append(diviseurs)
        diviseurs += 1    

    return liste_diviseurs
            



nombre = int(input("Choisissez un nombre:"))

print(diviseurs(nombre))