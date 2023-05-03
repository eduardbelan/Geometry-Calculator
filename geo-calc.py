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
            print("Rectangle is calculated...")
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


calc = GeoCalc()
calc.user_choice()
