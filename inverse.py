def inverse(liste):

    i = len(liste) - 1
    liste2 = []
    while i >= 0:
        liste2.append(liste[i])
        i -= 1
    return liste2


print(inverse([1, 5, 2, 6]))
