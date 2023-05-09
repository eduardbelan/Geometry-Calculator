import math

PICKS_RECTANGLE = []


class GeoCalc:
    """A Model of a Calculator to find missing values in the following shapes:
    Square, Rectangle, Triangle, Trapezoid, Circle"""

    def __init__(self):
        """init some attributes if needed"""
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
            self.square_umfang = self.square_seite * 4
            self.square_flaeche = self.square_seite * self.square_seite
            print(f"\nGegeben Seitenlänge: {self.square_seite}\n"
                  f"Berechnet Umfang: {self.square_umfang}\n"
                  f"Berechnet Fläche: {self.square_flaeche}")

        # Umfang known
        elif self.square_whats_given == 2:
            self.square_seite = self.square_umfang / 4
            self.square_flaeche = self.square_seite * self.square_seite
            print(f"\nGegeben Umfang: {self.square_umfang}\n"
                  f"Berechnet Seitenlänge: {self.square_seite}\n"
                  f"Berechnet Fläche: {self.square_flaeche}")

        # Fläche known
        elif self.square_whats_given == 3:
            self.square_seite = math.sqrt(self.square_flaeche)
            self.square_umfang = self.square_seite * 4
            print(f"f\nGegeben Fläche: {self.square_flaeche}\n"
                  f"Berechnet Seitenlänge: {self.square_seite}\n"
                  f"Berechnet Umfang: {self.square_umfang}")

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
                PICKS_RECTANGLE.append(int(whats_given[0]))
                PICKS_RECTANGLE.append(int(whats_given[1]))
                PICKS_RECTANGLE.sort()
                break

        for i in PICKS_RECTANGLE:
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
        if 1 in PICKS_RECTANGLE and 2 in PICKS_RECTANGLE:
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge a und Umfang known
        elif 1 in PICKS_RECTANGLE and 3 in PICKS_RECTANGLE:
            self.rectangle_seite_b = (self.rectangle_umfang - 2 * self.rectangle_seite_a) / 2
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge b und Umfang known
        elif 2 in PICKS_RECTANGLE and 3 in PICKS_RECTANGLE:
            self.rectangle_seite_a = (self.rectangle_umfang - 2 * self.rectangle_seite_b) / 2
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge a und Fläche known
        elif 1 in PICKS_RECTANGLE and 4 in PICKS_RECTANGLE:
            self.rectangle_seite_b = self.rectangle_flaeche / self.rectangle_seite_a
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}")

        # Seitenlänge b und Fläche known
        elif 2 in PICKS_RECTANGLE and 4 in PICKS_RECTANGLE:
            self.rectangle_seite_a = self.rectangle_flaeche / self.rectangle_seite_b
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}")

        # Umfang und Fläche known
        elif 3 in PICKS_RECTANGLE and 4 in PICKS_RECTANGLE:
            self.rectangle_seite_a = ((self.rectangle_umfang / 2)
                                      + math.sqrt((self.rectangle_umfang / 2) ** 2 - 4 * self.rectangle_flaeche)) / 2
            self.rectangle_seite_b = self.rectangle_flaeche / self.rectangle_seite_a
            print(f"\nGegeben Umfang: {self.rectangle_umfang}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}")

    def triangle_input(self):
        """User chooses known value, User enters known value"""
        whats_given = int(input("Allgemeines / Unregelmäßiges Dreieck:\n"
                                "\t1. Basis & Höhe\n"
                                "\t2. Alle Seiten\n"
                                "\t3. Zwei Seiten und der eingeschlossene Winkel\n"
                                "\t4. Zwei Seiten und ein gegenüberliegender Winkel\n"
                                "Type a Number to pick the known value: "))
        print("")
        self.triangle_whats_given = whats_given

        if whats_given == 1:
            self.triangle_seite_c = float(input("Enter Basis: "))
            self.triangle_hoehe_c = float(input("Enter Höhe: "))
        elif whats_given == 2:
            self.triangle_seite_a = float(input("Enter Seite A: "))
            self.triangle_seite_b = float(input("Enter Seite B: "))
            self.triangle_seite_c = float(input("Enter Seite C: "))
        elif whats_given == 3 or self.triangle_whats_given == 4:
            self.triangle_seite_x = float(input("Enter Seite 1: "))
            self.triangle_seite_y = float(input("Enter Seite 2: "))
            self.triangle_winkel_x = float(input("Enter Winkel: "))
        self.triangle_calc()

    def triangle_calc(self):
        """Missing values of Triangle are calculated"""


calc = GeoCalc()
calc.user_choice()
