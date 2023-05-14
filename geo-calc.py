import math

RECTANGLE_PICKS = []
TRIANGLE_GEGEBEN = {}
TRIANGLE_BERECHNET = {}


def triangle_print():
    """Make a print order and print gegeben and berechnet values in correct order"""

    print_order = ["Seite 1:", "Seite 2:", "Seite 3:",
                   "Seite A:", "Seite B:", "Seite C:",
                   "Kathete 1:", "Kathete 2:",
                   "Höhe 1:", "Höhe 2:", "Höhe 3:",
                   "Höhe A:", "Höhe B:", "Höhe C:",
                   "Winkel 1:", "Winkel 2:", "Winkel 3:",
                   "Winkel X:", "Winkel Y:", "Winkel Z:",
                   "\u03B1:", "\u03B2:", "\u03B3:",
                   "Umfang:", "Fläche:"]

    print("\nGegeben:")
    for k in print_order:
        if k in TRIANGLE_GEGEBEN:
            print(k, round(TRIANGLE_GEGEBEN[k], 2))
    print("")

    print("Berechnet:")
    for k in print_order:
        if k in TRIANGLE_BERECHNET:
            print(f"{k} {round(TRIANGLE_BERECHNET[k], 2)}")
    print("")


class GeoCalc:
    """A Model of a Calculator to find missing values in the following shapes:
    Square, Rectangle, Triangle, Trapezoid, Circle"""

    def __init__(self):
        """init some attributes if needed"""
        self.triangle_berechnet = None
        self.triangle_gegeben = None
        self.triangle_hoehe_c = None
        self.triangle_seite_c = None
        self.triangle_whats_given = None
        self.pick = None
        self.square_whats_given = None
        self.square_seite = None
        self.square_umfang = None
        self.square_flaeche = None
        self.rectangle_seite_a = None
        self.rectangle_seite_b = None
        self.rectangle_umfang = None
        self.rectangle_flaeche = None

    def user_choice(self):
        """Ask User to choose shape"""
        pick = int(input("1. Square\n"
                         "2. Rectangle\n"
                         "3. Triangle\n"
                         "4. Trapezoid\n"
                         "5. Circle\n"
                         "Type a Number to pick a Shape: "))
        self.pick = pick
        self.user_evaluation()

    def user_evaluation(self):
        """Evaluates the choice of the User"""
        print("")
        if self.pick == 1:
            self.square_input()
        elif self.pick == 2:
            self.rectangle_input()
        elif self.pick == 3:
            self.triangle_input()
        elif self.pick == 4:
            print("Trapezoid is calculated...")
        elif self.pick == 5:
            print("Circle is calculated...")

    def square_input(self):
        """User chooses known value, User enters known value"""
        whats_given = int(input("1. Seitenlänge\n"
                                "2. Umfang\n"
                                "3. Flächeninhalt\n"
                                "Type a Number to pick the known value: "))
        self.square_whats_given = whats_given

        if whats_given == 1:
            self.square_seite = float(input("\nEnter Seitenlänge: "))
        elif whats_given == 2:
            self.square_umfang = float(input("\nEnter Umfang: "))
        elif whats_given == 3:
            self.square_flaeche = float(input("\nEnter Fläche: "))
        self.square_calc()

    def square_calc(self):
        """Missing values of Square are calculated"""

        # Seitenlänge known
        if self.square_whats_given == 1:
            square_umfang = self.square_seite * 4
            square_flaeche = self.square_seite * self.square_seite
            print(f"\nGegeben Seitenlänge: {self.square_seite}\n"
                  f"Berechnet Umfang: {square_umfang}\n"
                  f"Berechnet Fläche: {square_flaeche}")

        # Umfang known
        elif self.square_whats_given == 2:
            square_seite = self.square_umfang / 4
            square_flaeche = square_seite * square_seite
            print(f"\nGegeben Umfang: {self.square_umfang}\n"
                  f"Berechnet Seitenlänge: {square_seite}\n"
                  f"Berechnet Fläche: {square_flaeche}")

        # Fläche known
        elif self.square_whats_given == 3:
            square_seite = math.sqrt(self.square_flaeche)
            square_umfang = square_seite * 4
            print(f"f\nGegeben Fläche: {self.square_flaeche}\n"
                  f"Berechnet Seitenlänge: {square_seite}\n"
                  f"Berechnet Umfang: {square_umfang}")

    def rectangle_input(self):
        """User chooses known value, User enters known value"""
        whats_given = input("1. Seitenlänge a\n"
                            "2. Seitenlänge b\n"
                            "3. Umfang\n"
                            "4. Flächeninhalt\n"
                            "Type two Numbers to pick the known values in this format 'num1num2': ")
        print("")

        two_picks = False
        while not two_picks:
            if len(whats_given) != 2:
                whats_given = input("Invalid Input. "
                                    "Enter two digits with no spaces in between in this format 'num1num2': ")
                print("")
            else:
                RECTANGLE_PICKS.append(int(whats_given[0]))
                RECTANGLE_PICKS.append(int(whats_given[1]))
                RECTANGLE_PICKS.sort()
                break

        for i in RECTANGLE_PICKS:
            if i == 1:
                self.rectangle_seite_a = float(input("Enter Seitenlänge a: "))
            elif i == 2:
                self.rectangle_seite_b = float(input("Enter Seitenlänge b: "))
            elif i == 3:
                self.rectangle_umfang = float(input("Enter Umfang: "))
            elif i == 4:
                self.rectangle_flaeche = float(input("Enter Flächeninhalt: "))
        self.rectangle_calc()

    def rectangle_calc(self):
        """Missing values of Rectangle are calculated"""

        # Seitenlängen a und b known
        if 1 in RECTANGLE_PICKS and 2 in RECTANGLE_PICKS:
            rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Umfang: {rectangle_umfang}\n"
                  f"Berechnet Fläche: {rectangle_flaeche}")

        # Seitenlänge a und Umfang known
        elif 1 in RECTANGLE_PICKS and 3 in RECTANGLE_PICKS:
            rectangle_seite_b = (self.rectangle_umfang - 2 * self.rectangle_seite_a) / 2
            rectangle_flaeche = self.rectangle_seite_a * rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge b: {rectangle_seite_b}\n"
                  f"Berechnet Fläche: {rectangle_flaeche}")

        # Seitenlänge b und Umfang known
        elif 2 in RECTANGLE_PICKS and 3 in RECTANGLE_PICKS:
            rectangle_seite_a = (self.rectangle_umfang - 2 * self.rectangle_seite_b) / 2
            rectangle_flaeche = rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge a: {rectangle_seite_a}\n"
                  f"Berechnet Fläche: {rectangle_flaeche}")

        # Seitenlänge a und Fläche known
        elif 1 in RECTANGLE_PICKS and 4 in RECTANGLE_PICKS:
            rectangle_seite_b = self.rectangle_flaeche / self.rectangle_seite_a
            rectangle_umfang = 2 * (self.rectangle_seite_a + rectangle_seite_b)
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge b: {rectangle_seite_b}\n"
                  f"Berechnet Umfang: {rectangle_umfang}")

        # Seitenlänge b und Fläche known
        elif 2 in RECTANGLE_PICKS and 4 in RECTANGLE_PICKS:
            rectangle_seite_a = self.rectangle_flaeche / self.rectangle_seite_b
            rectangle_umfang = 2 * (rectangle_seite_a + self.rectangle_seite_b)
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {rectangle_seite_a}\n"
                  f"Berechnet Umfang: {rectangle_umfang}")

        # Umfang und Fläche known
        elif 3 in RECTANGLE_PICKS and 4 in RECTANGLE_PICKS:
            rectangle_seite_a = ((self.rectangle_umfang / 2)
                                 + math.sqrt((self.rectangle_umfang / 2) ** 2 - 4 * self.rectangle_flaeche)) / 2
            rectangle_seite_b = self.rectangle_flaeche / rectangle_seite_a
            print(f"\nGegeben Umfang: {self.rectangle_umfang}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {rectangle_seite_a}\n"
                  f"Berechnet Seitenlänge b: {rectangle_seite_b}")

    def triangle_input(self):
        """User chooses known value, User enters known value"""
        whats_given = int(input("Allgemeines / Unregelmäßiges Dreieck:\n"
                                "\t1. Basis & Höhe\n"
                                "\t2. Alle Seiten\n"
                                "\t3. Zwei Seiten und der eingeschlossene Winkel\n"
                                "\t4. Zwei Seiten und der gegenüberliegende Winkel der längeren Seite\n"
                                "\t5. Eine Seite und zwei Winkel\n"
                                "Rechtwinkliges Dreieck:\n"
                                "\t6. Zwei Katheten und der rechte Winkel\n"
                                "Gleichschenkliges Dreieck:\n"
                                "\t7. Basis & Gamma\n"
                                "\t8. Basis & Höhe\n"
                                "Gleichseitiges Dreieck:\n"
                                "\t9. Seite\n"
                                "\t10. Höhe\n"
                                "\t11. Umfang\n"
                                "\t12. Fläche\n"
                                "Type a Number to pick the known value: "))
        print("")
        self.triangle_whats_given = whats_given

        if whats_given == 1:
            self.triangle_seite_c = float(input("Enter Basis: "))
            TRIANGLE_GEGEBEN["Seite C:"] = self.triangle_seite_c
            self.triangle_hoehe_c = float(input("Enter Höhe: "))
            TRIANGLE_GEGEBEN["Höhe C:"] = self.triangle_hoehe_c

        elif whats_given == 2:
            self.triangle_seite_a = float(input("Enter Seite A: "))
            TRIANGLE_GEGEBEN["Seite A:"] = self.triangle_seite_a
            self.triangle_seite_b = float(input("Enter Seite B: "))
            TRIANGLE_GEGEBEN["Seite B:"] = self.triangle_seite_b
            self.triangle_seite_c = float(input("Enter Seite C: "))
            TRIANGLE_GEGEBEN["Seite C:"] = self.triangle_seite_c

        elif whats_given == 3:
            self.triangle_seite_x = float(input("Enter Seite 1: "))
            TRIANGLE_GEGEBEN["Seite 1:"] = self.triangle_seite_x
            self.triangle_seite_y = float(input("Enter Seite 2: "))
            TRIANGLE_GEGEBEN["Seite 2:"] = self.triangle_seite_y
            self.triangle_winkel_x = float(input("Enter Winkel: "))
            TRIANGLE_GEGEBEN["Winkel X:"] = self.triangle_winkel_x

        elif whats_given == 4:
            self.triangle_seite_x = float(input("Enter längere Seite: "))
            self.triangle_seite_y = float(input("Enter kürzere Seite: "))
            if self.triangle_seite_x < self.triangle_seite_y:
                self.triangle_seite_x, self.triangle_seite_y = self.triangle_seite_y, self.triangle_seite_x
            TRIANGLE_GEGEBEN["Seite 1:"] = self.triangle_seite_x
            TRIANGLE_GEGEBEN["Seite 2:"] = self.triangle_seite_y
            self.triangle_winkel_x = float(input("Enter Winkel: "))
            TRIANGLE_GEGEBEN["Winkel X:"] = self.triangle_winkel_x

        elif whats_given == 5:
            self.triangle_seite1 = float(input("Enter Seite: "))
            TRIANGLE_GEGEBEN["Seite 1:"] = self.triangle_seite1
            self.triangle_winkel1 = float(input("Enter Winkel 1: "))
            TRIANGLE_GEGEBEN["Winkel 1:"] = self.triangle_winkel1
            self.triangle_winkel2 = float(input("Enter Winkel 2: "))
            TRIANGLE_GEGEBEN["Winkel 2:"] = self.triangle_winkel2

        elif whats_given == 6:
            self.triangle_kathete1 = float(input("Enter Kathete 1: "))
            TRIANGLE_GEGEBEN["Kathete 1:"] = self.triangle_kathete1
            self.triangle_kathete2 = float(input("Enter Kathete 2: "))
            TRIANGLE_GEGEBEN["Kathete 2:"] = self.triangle_kathete2

        elif whats_given == 7:
            self.triangle_seite_c = float(input("Enter Basis: "))
            TRIANGLE_GEGEBEN["Seite C:"] = self.triangle_seite_c
            self.triangle_winkel_gamma = float(input("Enter Gamma: "))
            TRIANGLE_GEGEBEN["\u03B3:"] = self.triangle_winkel_gamma

        elif whats_given == 8:
            self.triangle_seite_c = float(input("Enter Basis: "))
            TRIANGLE_GEGEBEN["Seite C:"] = self.triangle_seite_c
            self.triangle_hoehe_c = float(input("Enter Höhe: "))
            TRIANGLE_GEGEBEN["Höhe C:"] = self.triangle_hoehe_c

        elif whats_given == 9:
            self.triangle_seite1 = float(input("Enter Seite: "))
            TRIANGLE_GEGEBEN["Seite A:"] = self.triangle_seite1

        elif whats_given == 10:
            pass

        elif whats_given == 11:
            pass

        elif whats_given == 12:
            pass
        self.triangle_calc()

    def triangle_calc(self):
        """Missing values of Triangle are calculated"""

        # Basis & Höhe known
        if self.triangle_whats_given == 1:

            # Länge Seiten
            TRIANGLE_BERECHNET["Seite A:"] = math.sqrt(self.triangle_hoehe_c ** 2
                                                       + (0.5 * self.triangle_seite_c) ** 2)
            TRIANGLE_BERECHNET["Seite B:"] = math.sqrt(self.triangle_hoehe_c ** 2
                                                       + ((self.triangle_seite_c - TRIANGLE_BERECHNET["Seite A:"])
                                                          / 2) ** 2)

            # Winkel alpha, beta, gamma
            TRIANGLE_BERECHNET["\u03B1:"] = math.degrees(math.asin
                                                         (self.triangle_hoehe_c / TRIANGLE_BERECHNET["Seite A:"]))
            TRIANGLE_BERECHNET["\u03B2:"] = math.degrees(math.asin
                                                         (self.triangle_hoehe_c / TRIANGLE_BERECHNET["Seite B:"]))
            TRIANGLE_BERECHNET["\u03B3:"] = 180 - TRIANGLE_BERECHNET["\u03B1:"] - TRIANGLE_BERECHNET["\u03B2:"]

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = TRIANGLE_BERECHNET["Seite A:"] + \
                                            TRIANGLE_BERECHNET["Seite B:"] + \
                                            self.triangle_seite_c

            # Fläche
            TRIANGLE_BERECHNET["Fläche:"] = 0.5 * self.triangle_seite_c * self.triangle_hoehe_c

            # Höhen
            TRIANGLE_BERECHNET["Höhe A:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite_c
            TRIANGLE_BERECHNET["Höhe B:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / TRIANGLE_BERECHNET["Seite B:"]

        # Seite & Seite & Seite known
        elif self.triangle_whats_given == 2:

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = self.triangle_seite_a + self.triangle_seite_b + self.triangle_seite_c

            # Halbumfang für Flächenberechnung
            hu = TRIANGLE_BERECHNET["Umfang:"] / 2

            # Fläche
            TRIANGLE_BERECHNET["Fläche:"] = math.sqrt(hu * (hu - self.triangle_seite_a) *
                                                      (hu - self.triangle_seite_b) *
                                                      (hu - self.triangle_seite_c))

            # Höhen
            TRIANGLE_BERECHNET["Höhe A:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite_a
            TRIANGLE_BERECHNET["Höhe B:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite_b
            TRIANGLE_BERECHNET["Höhe C:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite_c

            # Winkel
            TRIANGLE_BERECHNET["\u03B1:"] = math.degrees(math.acos(
                (self.triangle_seite_b ** 2 + self.triangle_seite_c ** 2 - self.triangle_seite_a ** 2) /
                (2 * self.triangle_seite_b * self.triangle_seite_c)))
            TRIANGLE_BERECHNET["\u03B2:"] = math.degrees(math.acos(
                (self.triangle_seite_c ** 2 + self.triangle_seite_a ** 2 - self.triangle_seite_b ** 2) /
                (2 * self.triangle_seite_c * self.triangle_seite_a)))
            TRIANGLE_BERECHNET["\u03B3:"] = 180 - TRIANGLE_BERECHNET["\u03B1:"] - TRIANGLE_BERECHNET["\u03B2:"]

        # Seite & Seite & Eingeschlossener Winkel known
        elif self.triangle_whats_given == 3:

            # Bogenmaß des gegebenen Winkels
            winkel_rad = math.radians(self.triangle_winkel_x)

            # Länge Seiten
            TRIANGLE_BERECHNET["Seite 3:"] = math.sqrt(self.triangle_seite_x ** 2 +
                                                       self.triangle_seite_y ** 2 -
                                                       2 * self.triangle_seite_x *
                                                       self.triangle_seite_y *
                                                       math.cos(winkel_rad))

            # Winkel
            TRIANGLE_BERECHNET["Winkel Y:"] = math.degrees(math.asin(
                self.triangle_seite_y *
                math.sin(winkel_rad) /
                TRIANGLE_BERECHNET["Seite 3:"]))
            TRIANGLE_BERECHNET["Winkel Z:"] = 180 - self.triangle_winkel_x - TRIANGLE_BERECHNET["Winkel Y:"]

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = self.triangle_seite_x + \
                                            self.triangle_seite_y + \
                                            TRIANGLE_BERECHNET["Seite 3:"]

            # Fläche (und Halbumfang für Fläche)
            hu = TRIANGLE_BERECHNET["Umfang:"] / 2
            TRIANGLE_BERECHNET["Fläche:"] = math.sqrt(hu * (hu - self.triangle_seite_x) *
                                (hu - self.triangle_seite_y) *
                                (hu - TRIANGLE_BERECHNET["Seite 3:"]))

            #Höhen
            TRIANGLE_BERECHNET["Höhe 1:"] = self.triangle_seite_y * math.sin(winkel_rad)
            TRIANGLE_BERECHNET["Höhe 2:"] = self.triangle_seite_x * math.sin(
                math.radians(TRIANGLE_BERECHNET["Winkel Y:"]))
            TRIANGLE_BERECHNET["Höhe 3:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite_y

        # Seite & Seite & Gegenüberliegender Winkel known
        elif self.triangle_whats_given == 4:

            # Bogenmaß des gegebenen Winkels
            winkel_rad = math.radians(self.triangle_winkel_x)

            # Winkel
            TRIANGLE_BERECHNET["Winkel Y:"] = math.degrees(math.asin(
                self.triangle_seite_y * math.sin(winkel_rad) / self.triangle_seite_x))
            TRIANGLE_BERECHNET["Winkel Z:"] = 180 - self.triangle_winkel_x - TRIANGLE_BERECHNET["Winkel Y:"]

            # Bogenmaß des berechneten Winkels Y
            winkel_rad_z = math.radians(TRIANGLE_BERECHNET["Winkel Z:"])

            # Länge Seiten
            TRIANGLE_BERECHNET["Seite 3:"] = self.triangle_seite_x * math.sin(winkel_rad_z) / math.sin(winkel_rad)

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = self.triangle_seite_x + self.triangle_seite_y + \
                                            TRIANGLE_BERECHNET["Seite 3:"]

            # Fläche
            hu = TRIANGLE_BERECHNET["Umfang:"] / 2
            TRIANGLE_BERECHNET["Fläche:"] = math.sqrt(hu * (hu - self.triangle_seite_x) *
                                                      (hu - self.triangle_seite_y) *
                                                      (hu - TRIANGLE_BERECHNET["Seite 3:"]))

            # Höhen
            TRIANGLE_BERECHNET["Höhe A:"] = self.triangle_seite_x * \
                                            math.sin(math.radians(TRIANGLE_BERECHNET["Winkel Z:"]))
            TRIANGLE_BERECHNET["Höhe B:"] = self.triangle_seite_y * \
                                            math.sin(math.radians(TRIANGLE_BERECHNET["Winkel Z:"]))
            TRIANGLE_BERECHNET["Höhe C:"] = self.triangle_seite_x * \
                                            math.sin(math.radians(TRIANGLE_BERECHNET["Winkel Y:"]))

        # Seite & Winkel & Winkel known
        elif self.triangle_whats_given == 5:

            # Winkel
            TRIANGLE_BERECHNET["Winkel 3:"] = 180 - self.triangle_winkel1 - self.triangle_winkel2

            # Bogenmaß
            winkel1_rad = math.radians(self.triangle_winkel1)
            winkel2_rad = math.radians(self.triangle_winkel2)
            winkel3_rad = math.radians(TRIANGLE_BERECHNET["Winkel 3:"])

            # Seiten
            TRIANGLE_BERECHNET["Seite 2:"] = self.triangle_seite1 * math.sin(winkel2_rad) / math.sin(winkel1_rad)
            TRIANGLE_BERECHNET["Seite 3:"] = self.triangle_seite1 * math.sin(winkel3_rad) / math.sin(winkel1_rad)

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = self.triangle_seite1 + TRIANGLE_BERECHNET["Seite 2:"] + \
                                            TRIANGLE_BERECHNET["Seite 3:"]

            # Fläche
            hu = TRIANGLE_BERECHNET["Umfang:"] / 2
            TRIANGLE_BERECHNET["Fläche:"] = math.sqrt(hu * (hu - self.triangle_seite1) *
                                                      (hu - TRIANGLE_BERECHNET["Seite 2:"]) *
                                                      (hu - TRIANGLE_BERECHNET["Seite 3:"]))

            # Höhen
            TRIANGLE_BERECHNET["Höhe 1:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / self.triangle_seite1
            TRIANGLE_BERECHNET["Höhe 2:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / TRIANGLE_BERECHNET["Seite 2:"]
            TRIANGLE_BERECHNET["Höhe 3:"] = 2 * TRIANGLE_BERECHNET["Fläche:"] / TRIANGLE_BERECHNET["Seite 3:"]

        # Kathete & Kathete & Rechter Winkel known
        elif self.triangle_whats_given == 6:

            # Länge Seiten
            TRIANGLE_BERECHNET["Seite C:"] = math.sqrt(self.triangle_kathete1 ** 2 + self.triangle_kathete2 ** 2)

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = self.triangle_kathete1 + \
                                            self.triangle_kathete2 + TRIANGLE_BERECHNET["Seite C:"]

            # Fläche
            TRIANGLE_BERECHNET["Fläche:"] = (self.triangle_kathete1 * self.triangle_kathete2) / 2

            # Winkel
            TRIANGLE_GEGEBEN["\u03B3:"] = 90
            TRIANGLE_BERECHNET["\u03B1:"] = math.degrees(math.asin(
                self.triangle_kathete1 / TRIANGLE_BERECHNET["Seite C:"]))
            TRIANGLE_BERECHNET["\u03B2:"] = 180 - TRIANGLE_BERECHNET["\u03B1:"] - TRIANGLE_GEGEBEN["\u03B3:"]

            # Höhe
            TRIANGLE_BERECHNET["Höhe A:"] = self.triangle_kathete2
            TRIANGLE_BERECHNET["Höhe B:"] = self.triangle_kathete1
            TRIANGLE_BERECHNET["Höhe C:"] = self.triangle_kathete1 * math.sin(
                math.radians(TRIANGLE_BERECHNET["\u03B2:"]))

        # Basis & Winkel Vertex known
        elif self.triangle_whats_given == 7:

            # Schenkel
            schenkel = self.triangle_seite_c / (2 * math.sin(math.radians(self.triangle_winkel_gamma / 2)))
            TRIANGLE_BERECHNET["Seite A:"] = schenkel
            TRIANGLE_BERECHNET["Seite B:"] = schenkel

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = (2 * schenkel) + self.triangle_seite_c

            # Fläche
            hu = TRIANGLE_BERECHNET["Umfang:"] / 2
            TRIANGLE_BERECHNET["Fläche:"] = math.sqrt(hu * (hu - self.triangle_seite_c) *
                                                      (hu - schenkel) * (hu - schenkel))

            # Höhe
            TRIANGLE_BERECHNET["Höhe C:"] = schenkel * math.cos(math.radians(self.triangle_winkel_gamma / 2))
            TRIANGLE_BERECHNET["Höhe A:"] = (2 * TRIANGLE_BERECHNET["Fläche:"]) / schenkel
            TRIANGLE_BERECHNET["Höhe B:"] = (2 * TRIANGLE_BERECHNET["Fläche:"]) / schenkel

            # Winkel
            TRIANGLE_BERECHNET["\u03B1:"] = (180 - self.triangle_winkel_gamma) / 2
            TRIANGLE_BERECHNET["\u03B2:"] = TRIANGLE_BERECHNET["\u03B1:"]

        # Basis & Höhe known
        elif self.triangle_whats_given == 8:

            # Schenkel
            schenkel = math.sqrt((4 * (self.triangle_hoehe_c ** 2)) + (self.triangle_seite_c ** 2)) / 2
            TRIANGLE_BERECHNET["Seite A:"] = schenkel
            TRIANGLE_BERECHNET["Seite B:"] = schenkel

            # Winkel
            TRIANGLE_BERECHNET["\u03B1:"] = math.degrees(math.acos((self.triangle_seite_c / 2) / schenkel))
            TRIANGLE_BERECHNET["\u03B2:"] = TRIANGLE_BERECHNET["\u03B1:"]
            TRIANGLE_BERECHNET["\u03B3:"] = 180 - TRIANGLE_BERECHNET["\u03B1:"] - TRIANGLE_BERECHNET["\u03B2:"]

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = (2 * schenkel) + self.triangle_seite_c

            # Fläche
            TRIANGLE_BERECHNET["Fläche:"] = (self.triangle_seite_c * self.triangle_hoehe_c) / 2

            # Höhe
            TRIANGLE_BERECHNET["Höhe A:"] = (2 * TRIANGLE_BERECHNET["Fläche:"]) / schenkel
            TRIANGLE_BERECHNET["Höhe B:"] = (2 * TRIANGLE_BERECHNET["Fläche:"]) / schenkel

        # Seite known
        elif self.triangle_whats_given == 9:

            # Seiten
            TRIANGLE_BERECHNET["Seite B:"] = self.triangle_seite1
            TRIANGLE_BERECHNET["Seite C:"] = self.triangle_seite1

            # Winkel
            TRIANGLE_BERECHNET["\u03B1:"] = 60
            TRIANGLE_BERECHNET["\u03B2:"] = 60
            TRIANGLE_BERECHNET["\u03B3:"] = 60

            # Höhe
            TRIANGLE_BERECHNET["Höhe A:"] = (math.sqrt(3) / 2) * self.triangle_seite1
            TRIANGLE_BERECHNET["Höhe B:"] = TRIANGLE_BERECHNET["Höhe A:"]
            TRIANGLE_BERECHNET["Höhe C:"] = TRIANGLE_BERECHNET["Höhe C:"]

            # Umfang
            TRIANGLE_BERECHNET["Umfang:"] = 3 * self.triangle_seite1

            # Fläche
            TRIANGLE_BERECHNET["Fläche:"] = (math.sqrt(3) / 4) * self.triangle_seite1 ** 2

        # Ausgabe
        triangle_print()


calc = GeoCalc()
calc.user_choice()
