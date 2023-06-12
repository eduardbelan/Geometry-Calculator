import math
from q_formulas import umfang, flaecheninhalt, gegeben_umfang, gegeben_flaecheninhalt


def berechnung_frage():
    end = False
    while not end:

        again = input("Neue Berechnung? [J/N]: ")
        if again.lower() == "j":
            berechnung_rechnung()
        elif again.lower() == "n":
            print("Tschüssi")
            end = True
        else:
            print("Ungültige Eingabe")


def berechnung_rechnung():
    enough = False
    while not enough:

        eingabe = input("Eingabe, Rechteck/Quadrat, [R/Q]: ")
        if eingabe.lower() == "q":
            nummer = input("Seite, Flächeninhalt, Umfang, [S/F/U]: ")
            if nummer.lower() == "s":
                usr_choice = float(input("Seitenlänge: "))
                print(f"Umfang: {umfang(usr_choice)}")
                print(f"Flächeninhalt: {flaecheninhalt(usr_choice)}")
                enough = True
            elif nummer.lower() == "f":
                usr_choice = float(input("Flächeninhalt: "))
                seite = gegeben_flaecheninhalt(num_1=usr_choice)
                print(f"Seitenlänge: {gegeben_flaecheninhalt(usr_choice)}")
                print(f"Umfang: {umfang(seite)}")
                enough = True
            elif nummer.lower() == "u":
                usr_choice = float(input("Umfang: "))
                seite = gegeben_umfang(usr_choice)
                print(f"Flächeninhalt: {flaecheninhalt(seite)}")
                print(f"Seitenlänge: {gegeben_umfang(usr_choice)}")
                enough = True
        else:
            print("Ungültige Eingabe")


berechnung_frage()
