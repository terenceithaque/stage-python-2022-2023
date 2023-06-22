def tri(liste_nombres):
  #all_numbers = 0 # Tous les nombres de la liste

  #position = liste_nombres[0]
  element = liste_nombres[0]
  for indice in range(len(liste_nombres)):
    for indice2 in range(len(liste_nombres) - 1):
      if liste_nombres[indice2] > liste_nombres[indice2+1]:
        tmp = liste_nombres[indice2]
        liste_nombres[indice2] = liste_nombres[indice2+1]
        liste_nombres[indice2+1] = tmp
        print(liste_nombres)
    print()

  return liste_nombres
     
      
print(tri([5,4,3,2,6]))




    



    

#def afficher(liste_nombres = []):
  #  long = len(liste_nombres)
   # i = 0
   # while i < long:
   #   print(liste_nombres[i])
      
   #   i += 1
    
      


#safficher([4, 5, 6, 7, 8])
#print(tri([1, 3, 8, 2, 9])
