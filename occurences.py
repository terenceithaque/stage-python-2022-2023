def occurences(chaine):
    "Trouver le nombre d'occurences de chaques caractères d'une chaine"
    dict_occurences = {}

    for caractere in chaine:
        
        occurences = chaine.count(caractere)
            
        dict_occurences[caractere] = occurences

    
    return dict_occurences



chaine = input("Tapez une chaîne de caractères quelconque :")

verifier_occurences = occurences(chaine)

for data in verifier_occurences:  # Pour chaque donnée qui est extraite du dictionnaire
    element = data
    occurences = verifier_occurences[element]
    print("Le caratcère {}".format(element), "apparaît", occurences, "fois")  
    

