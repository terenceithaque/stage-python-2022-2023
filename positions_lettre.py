def positions(lettre, chaine):
    "Retourner sous forme de liste la position de chaque caractère lettre  présent dans la chaine de caractères chaine"
    liste_pos_lettre = []  # Liste contenant chaque position de la lettre indiquée
    if chaine.count(lettre) == 0:  # Si la lettre n'apparaît pas dans la chaine
        liste_pos_lettre.append(-1) # Ajouter la valeur -1 à la liste
    
    else: 
     
     for index in range(len(chaine)):  # Pour autant de caractères qu'il y a dans la chaine
        print(chaine[index])
        if chaine[index] == lettre:
           liste_pos_lettre.append(index)


         

            
            
                


            

      
               

    return liste_pos_lettre        

chaine = input("Tapez une chaine de caractères :")
lettre = input("Indiquez la lettre dont la position doit être trouvée :")

print(positions(lettre, chaine))