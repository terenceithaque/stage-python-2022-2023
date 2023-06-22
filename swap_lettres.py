def swap_lettres(chaine, lettre1, lettre2):
    liste_caracteres = list(chaine)
    liste_caracteres[lettre1], liste_caracteres[lettre2] = liste_caracteres[lettre2], liste_caracteres[lettre1]
    chaine_inverse = "".join(liste_caracteres)
    return chaine_inverse

chaine = input("Tapez des caractères quelconques:")
position_lettre_a_echanger_1 = int(input("Indiquez la position du premier caractère à inverser :"))    
position_lettre_a_echanger_2 = int(input("Indiquez la position du deuxième caractère à inverser:"))

print(swap_lettres(chaine, position_lettre_a_echanger_1, position_lettre_a_echanger_2))
        