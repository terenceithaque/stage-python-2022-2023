def div_euclidienne(a, b):
    "Retourner le quotient et le reste d'une division euclidienne"
    quot_et_reste = (a / b, a%b)  # Tuple contenant le quotient et le reste 
    return quot_et_reste
    
    
    
nombre1 = int(input("Choisissez le 1er nombre:"))
nombre2 = int(input("Choisissez le 2ème nombre:"))

print(div_euclidienne(nombre1, nombre2))



    