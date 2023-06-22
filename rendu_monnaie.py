def rendu_monnaie(prix, somme_payee):
    return somme_payee - prix


def decomposer_somme(somme):
    dict_billets_et_piece = {
        50000: 0,
        10000: 0,
        5000: 0,
        2000: 0,
        1000: 0,
        500: 0,
        200: 0,
        100: 0,
        50: 0,
        20: 0,
        10: 0,
        5: 0,
        2: 0,
        1: 0
    }

    somme = somme*100
    for valeur in dict_billets_et_piece:

        if somme // valeur >= 1:
            dict_billets_et_piece[valeur] = somme//valeur
            somme -= dict_billets_et_piece[valeur] * valeur

    return dict_billets_et_piece

    # return dict_billets_et_piece


prix = float(input("Entrez un prix:"))
somme = float(input("Entrez la somme payée :"))
monnaie = rendu_monnaie(prix, somme)
dict_billets = decomposer_somme(monnaie)

print("Prix à payer : %.2f" % prix, "€")
print("Rendu : %.2f" % monnaie, "€")
print("Décomposition :")


for argent in dict_billets:
    if dict_billets[argent] > 0:
        print(argent / 100, "€ : %d" % dict_billets[argent])
