F1 = str(1)
F2 = str(2)
F3 = str(3)
F4 = str(4)
F5 = str(5)
F6 = str(6)
F7 = str(7)
F8 = str(8)
F9 = str(9)
game = True
reset = False

def x(pos):
    global F1
    global F2
    global F3
    global F4
    global F5
    global F6
    global F7
    global F8
    global F9

    if pos == 1:
        if F1 == "1":
            F1 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 2:
        if F2 == "2":
            F2 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 3:
        if F3 == "3":
            F3 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 4:
        if F4 == "4":
            F4 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 5:
        if F5 == "5":
            F5 = "x"
        else:
            print("Das Feld st bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 6:
        if F6 == "6":
            F6 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 7:
        if F7 == "7":
            F7 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 8:
        if F8 == "8":
            F8 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 9:
        if F9 == "9":
            F9 = "x"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    else:
        print("Das Feld exestirt nicht!")
        return ("F")

def o(pos):
    global F1
    global F2
    global F3
    global F4
    global F5
    global F6
    global F7
    global F8
    global F9

    if pos == 1:
        if F1 == "1":
            F1 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 2:
        if F2 == "2":
            F2 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 3:
        if F3 == "3":
            F3 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 4:
        if F4 == "4":
            F4 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 5:
        if F5 == "5":
            F5 = "o"
        else:
            print("Das Feld st bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 6:
        if F6 == "6":
            F6 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 7:
        if F7 == "7":
            F7 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 8:
        if F8 == "8":
            F8 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    elif pos == 9:
        if F9 == "9":
            F9 = "o"
        else:
            print("Das Feld ist bereits vergeben!")
            print("")
            print("")
            return ("F")
    else:
        print("Das Feld exestirt nicht!")
        return ("F")



while game:

    if F1 != "1" and F2 != "2" and F3 != "3" and F4 != "4" and F5 != "5" and F6 != "6" and F7 != "7" and F8 != "8" and F9 != "9":
        print("")
        print("")
        print("")
        print(F1 + "|" + F2 + "|" + F3)
        print(F4 + "|" + F5 + "|" + F6)
        print(F7 + "|" + F8 + "|" + F9)
        print("unentschieden!")
        print("")
        print("")
        print("")
        break

    if reset == False:
        print(F1 + "|" + F2 + "|" + F3)
        print(F4 + "|" + F5 + "|" + F6)
        print(F7 + "|" + F8 + "|" + F9)
        print("")
        choos = input("Spieler:x Welches Feld möschtest du Belegen: ")
        if choos == "q":
            break
        else:
            choos_x = int(choos)
        print("")
        print("")
        if x(choos_x) == "F":
            continue

        if F1 == F2 == F3 or F4 == F5 == F6 or F7 == F8 == F9 or F1 == F4 == F7 or F2 == F5 == F8 or F3 == F6 == F9 or F1 == F5 == F9 or F3 == F5 == F7:
            print("")
            print("")
            print("")
            print(F1 + "|" + F2 + "|" + F3)
            print(F4 + "|" + F5 + "|" + F6)
            print(F7 + "|" + F8 + "|" + F9)
            print("x hat gewonnen")
            print("")
            print("")
            print("")
            break


    if F1 != "1" and F2 != "2" and F3 != "3" and F4 != "4" and F5 != "5" and F6 != "6" and F7 != "7" and F8 != "8" and F9 != "9":
        print("")
        print("")
        print("")
        print(F1 + "|" + F2 + "|" + F3)
        print(F4 + "|" + F5 + "|" + F6)
        print(F7 + "|" + F8 + "|" + F9)
        print("unentschieden!")
        print("")
        print("")
        print("")
        break


    reset = False
    print(F1 + "|" + F2 + "|" + F3)
    print(F4 + "|" + F5 + "|" + F6)
    print(F7 + "|" + F8 + "|" + F9)
    print("")
    choos2 = input("Spieler:o Welches Feld möschtest du Belegen: ")
    if choos2 == "q":
        break
    else:
        choos_o = int(choos2)
    print("")
    print("")
    if o(choos_o) == "F":
        reset = True
        continue

    if F1 == F2 == F3 or F4 == F5 == F6 or F7 == F8 == F9 or F1 == F4 == F7 or F2 == F5 == F8 or F3 == F6 == F9 or F1 == F5 == F9 or F3 == F5 == F7:
        print("")
        print("")
        print("")
        print(F1 + "|" + F2 + "|" + F3)
        print(F4 + "|" + F5 + "|" + F6)
        print(F7 + "|" + F8 + "|" + F9)
        print("o hat gewonnen")
        print("")
        print("")
        print("")
        break