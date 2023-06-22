import turtle
from random import randint


def forme_aleatoire(tortue):

    repetition = randint(50, 200)
    distance = randint(10, 200)
    angle = randint(0, 360)

    while repetition > 0:
        tortue.forward(distance)
        tortue.right(angle)
        repetition -= 1
        print(repetition)


maTortue = turtle.Turtle()
forme_aleatoire(maTortue)
