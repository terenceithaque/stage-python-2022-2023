def is_pair(nb):
   reste = nb%2
   if reste == 0:
      return True
   else:
      return False
         
  



nombre = int(input("Choisissez le nombre à vérifier :"))   
      
        

if is_pair(nombre):
   print(nombre, "est pair")

else:
   print(nombre, "est impair")   