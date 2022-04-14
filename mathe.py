import time

while True:

    print(" , = . / - = Numpad-")

    x = float(input("x: "))
    y = float(input("y: "))


    print("Spalte 1: " + str(3* x -7* y))
    print("Spalte 2: " + str(3*( x -7 * y)))
    print("Spalte 3: " + str(3*(3* x -7)* y))
    print("Spalte 4: " + str((3* x -7)* y))

    print("")
    print("bitte warte 15sek für neue eingabe...")
    time.sleep(15)
    print("")
    print("")