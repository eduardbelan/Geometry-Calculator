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
    winkel_rad = math.radians(winkel_x)

    # Länge Seiten
    seite_z = math.sqrt(seite_x ** 2 + seite_y ** 2 - 2 * seite_x * seite_y * math.cos(winkel_rad))

    # Winkel
    winkel_y = math.degrees(math.asin(b * math.sin(winkel_rad) / seite_z))
    winkel_z = 180 - winkel_x - winkel_y

    # Fläche
    hu = (seite_x + seite_y + seite_z) / 2
    flaeche = math.sqrt(hu * (hu - seite_x) * (hu - seite_y) * (hu - seite_z))

    # Höhen
    hoehe_x = b * math.sin(winkel_rad)
    hoehe_y = a * math.sin(winkel_y)
    hoehe_z = 2 * flaeche / seite_y

    # Umfang
    umfang = seite_x + seite_y + seite_z


def allg_SSGW(seite_x, seite_y, winkel_x):
    """allgemeines Dreieck, Seite & Seite & Gegenüberliegender Winkel"""

    # Bogenmaß des gegebenen Winkels
    winkel_rad = math.radians(winkel_x)

    # Länge Seiten
    seite_z = math.sqrt(seite_x ** 2 + seite_y ** 2 - 2 * seite_x * seite_y * math.cos(winkel_rad))

    # Winkel
    winkel_y = math.degrees(math.asin(seite_y * math.sin(winkel_rad) / seite_x))
    winkel_z = 180 - winkel_x - winkel_y

    # Umfang
    umfang = seite_x + seite_y + seite_z

    # Fläche
    hu = (seite_x + seite_y + seite_z) / 2
    flaeche = math.sqrt(hu * (hu - seite_x) * (hu - seite_y) * (hu - seite_z))

    # Höhen
    hoehe_a = seite_y * math.sin(winkel_rad)
    hoehe_b = seite_x * math.sin(math.radians(winkel_y))
    hoehe_c = 2 * flaeche / seite_x


def allg_SWW(seite1, winkel1, winkel2):
    """allgemeines Dreieck, Seite & Winkel & Winkel"""

    # Winkel
    winkel3 = 180 - winkel1 - winkel2

    # Bogenmaß
    winkel1_rad = math.radians(winkel1)
    winkel2_rad = math.radians(winkel2)
    winkel3_rad = math.radians(winkel3)

    # Seiten
    seite2 = seite1 * math.sin(winkel2_rad) / math.sin(winkel1_rad)
    seite3 = seite1 * math.sin(winkel3_rad) / math.sin(winkel1_rad)

    # Umfang
    umfang = seite1 + seite2 + seite3

    # Fläche
    hu = umfang / 2
    flaeche = math.sqrt(hu * (hu - seite1) * (hu - seite2) * (hu - seite3))

    # Höhen
    hoehe1 = 2 * flaeche / seite1
    hoehe2 = 2 * flaeche / seite2
    hoehe3 = 2 * flaeche / seite3


def rechtw_KKRW(kathete1, kathete2):
    """rechtwinkliges Dreieck, Kathete & Kathete & Rechter Winkel"""

    # Länge Seiten
    hypotenuse = math.sqrt(kathete1 ** 2 + kathete2 ** 2)

    # Umfang
    umfang = kathete1 + kathete2 + hypotenuse

    # Fläche
    flaeche = (kathete1 * kathete2) / 2

    # Winkel
    gamma = 90
    alpha = math.degrees(math.asin(kathete1 / hypotenuse))
    beta = 180 - alpha - gamma

    # Höhe
    hoehe = (kathete1 / kathete2) / hypotenuse


def gleichschenk_BW(basis, gamma):
    """gleichschenkliges Dreieck, Basis & Winkel Vertex known"""

    # Schenkel
    schenkel = basis / (2 * math.sin(math.radians(gamma / 2)))

    # Umfang
    umfang = (2 * schenkel) + basis

    # Fläche
    hu = umfang / 2
    flaeche = math.sqrt(hu * (hu - basis) * (hu - schenkel) * (hu - schenkel))

    # Höhe
    hoehe_basis = schenkel * math.cos(math.radians(gamma / 2))
    hoehe_schenkel = (2 * flaeche) / schenkel

    # Winkel
    alpha = (180 - gamma) / 2
    beta = alpha



def gleichschenk_BH(basis, hoehe_c):
    """gleichschenkliges Dreieck, Basis & Höhe der Basis known"""

    # Schenkel
    schenkel = math.sqrt((4 * (basis ** 2)) + (hoehe_c ** 2)) / 2

    # Winkel
    winkel = math.degrees(math.acos((basis / 2) / schenkel))

    # Umfang
    umfang = (2 * schenkel) + basis

    # Fläche
    flaeche = (basis * hoehe_c) / 2

    # Höhe
    hoehe_a = (2 * flaeche) / schenkel
    hoehe_b = (2 * flaeche) / schenkel


def gleichseit_S(seite):
    """gleichseitiges Dreieck, Seite known"""

    # Winkel
    winkel = 60

    # Höhe
    hoehe = (math.sqrt(3) / 2) * seite

    # Umfang
    umfang = 3 * seite

    # Fläche
    flaeche = (math.sqrt(3) / 4) * seite ** 2


def gleichseit_H(hoehe):
    """gleichseitiges Dreieck, Höhe known"""

    # Seite
    seite = 2 * hoehe / math.sqrt(3)

    # Umfang
    umfang = 3 * seite

    # Fläche
    flaeche = (math.sqrt(3) / 4) * seite ** 2

def gleichseit_U(umfang):
    """gleichseitiges Dreieck, Umfang known"""

    # Seiten
    seite = umfang / 3

    # Höhe
    hoehe = (math.sqrt(3) / 2) * seite

    # Fläche
    flaeche = (math.sqrt(3) / 4) * seite ** 2

def gleichset_A(flaeche):
    """gleichseitiges Dreieck, Fläche known"""

    # Seite
    seite = math.sqrt((4 * flaeche) / math.sqrt(3))

    # Höhe
    hoehe = (math.sqrt(3) / 2) * seite

    # Umfang
    umfang = 3 * seite