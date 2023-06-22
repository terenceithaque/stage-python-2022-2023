def nb_voyelles(chaine):
    "Retourner le nombre de voyelles présentes dans une chaîne donnée"
    liste_voyelles = ["a", "A", "e", "E", "i","I", "o","O", "u","U", "y","Y"] # Liste qui contient les voyelles (en maj. et en min.) auxquelles seront comparés les caractères de la chaîne

    n_voyelles = 0 # Nombre de voyelles dans la chaîne

    for caractere in chaine: # Pour chaque caractère de la chaîne
        for voyelle in liste_voyelles:
            if caractere == voyelle:
                n_voyelles += 1

    return n_voyelles


chaine = input("Tapez un mot ou des caractères quelconques :")

i = 0

while i < len(chaine):
    compter_voyelles = nb_voyelles(chaine)
    i+= 1


print(compter_voyelles, "voyelle(s) trouvée(s)")    
        

