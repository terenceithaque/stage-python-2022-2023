def del_doublons(liste):
    liste_sans_doublons = []

    for element in liste:
        if element not in liste_sans_doublons:
            liste_sans_doublons.append(element)

    return liste_sans_doublons            
                 
    

liste = list(input("Indiquez les éléments à insérer dans la liste :"))
print(liste)
print(del_doublons(liste))          