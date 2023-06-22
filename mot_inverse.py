def mot_inverse(mot):
    "Inverser les caractères d'un mot donné"
    chaine = ""

    for i in range(len(mot) - 1, -1, -1):
        chaine += mot[i]

    return chaine        
              
              



mot = input("Tapez un mot quelquonque :")




print(mot_inverse(mot))    
            
        
        