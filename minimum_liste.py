def minimum_liste(liste_nombres):
    
    minimum = liste_nombres[0]
    for element in liste_nombres:
        
        if element < minimum:
            minimum = element
    return minimum                

        

        



print(minimum_liste([-16, 4, 16, 9]))

