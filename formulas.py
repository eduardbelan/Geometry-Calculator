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
    a = ((U / 2) + math.sqrt((U / 2) ** 2 - 4 * A)) / 2
    b = A / a
    return (a, b)


# Triangle
# Dreiecksarten:
#   - allgemeines/unregelmößiges Dreieck
#   - gleichseitiges Dreieck
#   - gleichschenkliges Dreieck
#   - spitzwinkliges Dreieck
#   - rechtwinkliges Dreieck
#   - stumpfwinkliges Dreieck
# zu berechnende Werte:
#   - Seiten (a, b, c)
#   - Höhen (a, b, c)
#   - Winkel (alpha, beta, gamma)
#   - Umfang
#   - Fläche

# allgemeines/unregelmäßiges Dreieck
#   - basis & höhe
#   - seite & seite & seite
#   - seite & seite & eingeschlossener winkel
#   - seite & seite & gegenüberliegender winkel
def allg_BH(basis, hoehe):
    """allgemeines Dreieck, Basis & Höhe known"""

    # Länge Seiten
    seite_a = math.sqrt(hoehe ** 2 + (0.5 * basis) ** 2)
    seite_b = math.sqrt(hoehe ** 2 + ((basis - seite_a) / 2) ** 2)
    seite_c = basis

    # Winkel
    winkel_a = math.degrees(math.asin(hoehe / seite_a))
    winkel_b = math.degrees(math.asin(hoehe / seite_b))
    winkel_c = 180 - winkel_a - winkel_b

    # Umfang
    umfang = seite_a + seite_b + seite_c

    # Fläche
    flaeche = 0.5 * basis * hoehe

    # Höhen
    hoehe_a = 2 * flaeche / basis
    hoehe_b = 2 * flaeche / seite_b
    hoehe_c = basis

    # Made a specific function for a more beautiful print
    # gegeben = {
    #     "Basis / Seite C": basis,
    #     "Höhe C": hoehe_c
    # }
    # berechnet = {
    #     "Seite A": seite_a,
    #     "Seite B": seite_b,
    #     "Höhe A": hoehe_a,
    #     "Höhe B": hoehe_b,
    #     "\u03B1": winkel_a,  # alpha
    #     "\u03B2": winkel_b,  # beta
    #     "\u03B3": winkel_c,  # gamma
    #     "Umfang": umfang,
    #     "Fläche": flaeche
    # }
    #
    # print("Gegeben:")
    # for k, v in gegeben.items():
    #     print(k, round(v, 2))
    # print("")
    # print("Berechnet:")
    # for k, v in berechnet.items():
    #     print(k, round(v, 2))
    # print("")


def allg_SSS(seite_a, seite_b, seite_c):
    """allgemeines Dreieck, Seite & Seite & Seite known
    - same thing as if umfang and 2 sides are known,
    but I'll leave it up to the user to solve that 'entry problem' :D"""

    # Umfang
    umfang = seite_a + seite_b + seite_c

    # Halbumfang (für Flächenberechnung)
    hu = (seite_a + seite_b + seite_c) / 2

    # Fläche
    flaeche = math.sqrt(hu * (hu - seite_a) * (hu - seite_b) * (hu - seite_c))

    # Höhen
    hoehe_a = 2 * flaeche / seite_a
    hoehe_b = 2 * flaeche / seite_b
    hoehe_c = 2 * flaeche / seite_c

    # Winkel
    winkel_a = math.degrees(math.acos((seite_b ** 2 + seite_c ** 2 - seite_a ** 2) / (2 * seite_b * seite_c)))
    winkel_b = math.degrees(math.acos((seite_c ** 2 + seite_a ** 2 - seite_b ** 2) / (2 * seite_c * seite_a)))
    winkel_c = 180 - winkel_a - winkel_b


def allg_SSEW(seite_x, seite_y, winkel_x):
    """allgemeines Dreieck, Seite & Seite & Eingeschlossener Winkel"""

    # Bogenmaß des gegebenen Winkels
    winkel_x = math.radians(winkel_x)

    # Länge Seiten
    seite_z = math.sqrt(seite_x ** 2 + seite_y ** 2 - 2 * seite_x * seite_y * math.cos(winkel_x))

    # Winkel
    winkel_y = math.degrees(math.asin(b * math.sin(winkel_x) / seite_z))
    winkel_z = 180 - winkel_x - winkel_y

    # Fläche
    hu = (seite_x + seite_y + seite_z) / 2
    flaeche = math.sqrt(hu * (hu - seite_x) * (hu - seite_y) * (hu - seite_z))

    # Höhen
    hoehe_x = b * math.sin(winkel_x)
    hoehe_y = a * math.sin(winkel_y)
    hoehe_z = 0.5 * a * b * math.sin(winkel_x) / flaeche

    # Umfang
    umfang = seite_x + seite_y + seite_z

