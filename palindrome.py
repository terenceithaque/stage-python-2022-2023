def mot_inverse(mot):
    "Inverser les caractères d'un mot donné"
    chaine = ""

    for i in range(len(mot) - 1, -1, -1):
        chaine += mot[i]

    return chaine 

def est_palindrome(mot):
    
  if mot_inverse(mot) == mot:
     return True
  
  else:
     return False
            


mot = input("Tapez un mot quelconque :")
if est_palindrome(mot)  == True:
    print(mot, "est un palindrome")

else:
    print(mot, "n'est pas un palindrome")                    