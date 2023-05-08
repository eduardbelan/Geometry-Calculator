import math


class GeoCalc:
    """A Model of a Calculator to find missing values in the following shapes:
    Square, Rectangle, Triangle, Trapezoid, Circle"""

    def __init__(self):
        """init some attributes if needed"""
        self.pick = None
        self.square_whats_given = None
        self.square_seite = None
        self.square_umfang = None
        self.square_flaeche = None
        self.rectangle_whats_given = None
        self.rectangle_whats_given_1 = None
        self.rectangle_whats_given_2 = None
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
            print("Triangle is calculated...")
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

        if self.square_whats_given == 1:
            seite = float(input("\nEnter Seitenlänge: "))
            self.square_seite = seite
        elif self.square_whats_given == 2:
            umfang = float(input("\nEnter Umfang: "))
            self.square_umfang = umfang
        elif self.square_whats_given == 3:
            flaeche = float(input("\nEnter Fläche: "))
            self.square_flaeche = flaeche
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
        two_picks = False
        while not two_picks:
            if len(whats_given) != 2:
                whats_given = input("Invalid Input. "
                                    "Enter two digits with no spaces in between in this format 'num1num2': ")
            else:
                whats_given_1 = int(whats_given[0])
                whats_given_2 = int(whats_given[1])
                self.rectangle_whats_given_1 = whats_given_1
                self.rectangle_whats_given_2 = whats_given_2
                print(f"1: {whats_given_1}\n"
                      f"2: {whats_given_2}")
                break

            ## maybe make a list and append whats_given values? sort them and then prompt user for values?

            if self.rectangle_whats_given == 1:
                seite_a = float(input("\nEnter Seitenlänge a: "))
                self.rectangle_seite_a = seite_a
            elif self.rectangle_whats_given == 2:
                seite_b = float(input("\nEnter Seitenlänge b: "))
                self.rectangle_seite_b = seite_b
            elif self.rectangle_whats_given == 3:
                umfang = float(input("\nEnter Umfang: "))
                self.rectangle_umfang = umfang
            elif self.rectangle_whats_given == 4:
                flaeche = float(input("\nEnter Flächeninhalt: "))
                self.rectangle_flaeche = flaeche
        self.rectangle_calc()

    def rectangle_calc(self):
        """Missing values of Rectangle are calculated"""

        # Seitenlängen a und b known
        if self.rectangle_whats_given == 1 and self.rectangle_whats_given == 2:
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge a und Umfang known
        elif self.rectangle_whats_given == 1 and self.rectangle_whats_given == 3:
            self.rectangle_seite_b = (self.rectangle_umfang - 2 * self.rectangle_seite_a) / 2
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge b und Umfang known
        elif self.rectangle_whats_given == 2 and self.rectangle_whats_given == 3:
            self.rectangle_seite_a = (self.rectangle_umfang - 2 * self.rectangle_seite_b) / 2
            self.rectangle_flaeche = self.rectangle_seite_a * self.rectangle_seite_b
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Umfang: {self.rectangle_umfang}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Fläche: {self.rectangle_flaeche}")

        # Seitenlänge a und Fläche known
        elif self.rectangle_whats_given == 1 and self.rectangle_whats_given == 4:
            self.rectangle_seite_b = self.rectangle_flaeche / self.rectangle_seite_a
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            print(f"\nGegeben Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}")

        # Seitenlänge b und Fläche known
        elif self.rectangle_whats_given == 2 and self.rectangle_whats_given == 4:
            self.rectangle_seite_a = self.rectangle_flaeche / self.rectangle_seite_b
            self.rectangle_umfang = 2 * (self.rectangle_seite_a + self.rectangle_seite_b)
            print(f"\nGegeben Seitenlänge b: {self.rectangle_seite_b}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Umfang: {self.rectangle_umfang}")

        # Umfang und Fläche known
        elif self.rectangle_whats_given == 3 and self.rectangle_whats_given == 4:
            self.rectangle_seite_a = ((self.rectangle_umfang / 2)
                                      + math.sqrt((self.rectangle_umfang / 2) ** 2 - 4 * self.rectangle_flaeche)) / 2
            self.rectangle_seite_b = self.rectangle_flaeche / self.rectangle_seite_a
            print(f"\nGegeben Umfang: {self.rectangle_umfang}\n"
                  f"Gegeben Fläche: {self.rectangle_flaeche}\n"
                  f"Berechnet Seitenlänge a: {self.rectangle_seite_a}\n"
                  f"Berechnet Seitenlänge b: {self.rectangle_seite_b}")


calc = GeoCalc()
calc.user_choice()
