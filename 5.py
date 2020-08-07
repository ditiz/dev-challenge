from random import *


def random_path():
    return 'n' if random() < 0.5 else 'e'


def get_opposite(letter):
    return "s" if letter == "n" else "w"


def walk(distance):
    go = [random_path() for i in range(int(distance / 2))]
    back = [get_opposite(letter) for letter in reversed(go)]
    return go + back


print(walk(10))
