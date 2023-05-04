import math


# Square
def umfang(num_1):
    return num_1 * 4


def flaecheninhalt(num_1):
    return num_1 * num_1


def gegeben_umfang(num_1):
    return num_1 / 4


def gegeben_flaecheninhalt(num_1):
    return math.sqrt(num_1)


# Rectangle
def umfang(a, b):
    return 2 * (a + b)


def flaecheninhalt(a, b):
    return a * b


def gegeben_breite_umfang(b, U):
    return (U - 2 * b) / 2


def gegeben_laenge_umfang(a, U):
    return (U - 2 * a) / 2

def gegeben_breite_flaecheninhalt(b, A):
    return A / b

def gegeben_laenge_flaecheninhalt(a, A):
    return A / a

def gegeben_umfang_flaecheninhalt(U, A):
    a = ((U / 2) + math.sqrt((U / 2)**2 - 4*A)) / 2
    b = A / a
    return (a, b)
