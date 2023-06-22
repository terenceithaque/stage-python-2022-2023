# Programme qui vérifie si un nombre est premier ou non

def is_premier(nb):
    i = 2
    while i < nb:
        if nb%i == 0:
            return False
        i += 1
        

    
    return True
    

  

#print(is_premier(10))


def nb_premiers(n):
    "Retourner les n premiers nombres premiers"
    liste_n_premiers = []
    i = 2
    while len(liste_n_premiers) < n:
        if is_premier(i):
            liste_n_premiers.append(i)
            print(liste_n_premiers)

        i += 1


        
        


print(nb_premiers(6))           