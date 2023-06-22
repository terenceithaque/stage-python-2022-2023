import turtle

def surface(rayon):
    rayon_au_carre = rayon * rayon
    surf = rayon_au_carre * 3.14
    return surf


#print(surface(5))


def perimetre(rayon):
    pi = 3.14
    perimetre = 2 *pi*rayon
    return perimetre

#print(perimetre(6))


def creer_cercle(rayon):
    tortue = turtle.Pen()
    tortue.circle(rayon)
"""    longueur = 0
    degre = 10
    while longueur < rayon:
        tortue.forward(20)
        tortue.right(degre)
        longueur += 1    """

#creer_cercle(50)
rayon = int(input("Veuillez entrer le rayon :"))
print(surface(rayon = rayon))
print(perimetre(rayon= rayon))
creer_cercle(rayon=rayon)

