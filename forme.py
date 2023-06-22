import turtle
tortue = turtle.Turtle()


def forme(nb_cotes, tailles_cotes):
    n = 0
    while n < nb_cotes:
        tortue.forward(tailles_cotes)
        tortue.right(tailles_cotes)
        n += 1


forme(4, 200)
