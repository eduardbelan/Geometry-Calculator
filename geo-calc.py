class GeoCalc:
    """A Model of a Calculator to find missing values in the following shapes:
    Square, Rectangle, Triangle, Trapezoid, Circle"""

    def __init__(self):
        """init some attributes if needed"""
        pass

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
            print("Square is calculated...")
        elif self.pick == 2:
            print("Rectangle is calculated...")
        elif self.pick == 3:
            print("Triangle is calculated...")
        elif self.pick == 4:
            print("Trapezoid is calculated...")
        elif self.pick == 5:
            print("Circle is calculated...")

calc = GeoCalc()
calc.user_choice()
