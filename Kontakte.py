import datetime

first_name = []
last_name = []
age = []
year = []

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()





def save(f_name, l_name, a, y):
    first_name.append(f_name)
    last_name.append(l_name)
    age.append(a)
    year.append(y)
    print(" ")
    print(" ")
    print(" ")
    print("Person gespeichert! Die Person hat folgende Nummer: " + str(len(first_name) - 1))
    print(" ")
    print(" ")
    print(" ")

def read(number):
    print(" ")
    print(" ")
    print(" ")
    T = (date.year - int(year[number])) > 17
    print(first_name[number] + " " + last_name[number] + " Alter: " + age[number] + " Geburtsjahr: " + year[number] + " / Volljährig: " + str(T))
    print(" ")
    print(" ")
    print(" ")

def remove(number):
    print(" ")
    print(" ")
    print(" ")
    f = first_name[number]
    l = last_name[number]
    a = age[number]
    y = year[number]
    first_name.remove(f)
    last_name.remove(l)
    age.remove(a)
    year.remove(y)
    print(f + " " + l + " Alter: " + a + " Geburtsjahr: " + y + " wurde gelöscht!")
    print(" ")
    print(" ")
    print(" ")

def list():
    r = 0

    while not r == len(first_name):
        T = (date.year - int(year[r])) > 17
        print(str(r) + ". " + first_name[r] + " " + last_name[r] + " Alter: " + age[r] + " Geburtsjahr: " + year[r] + " / Volljährig: " + str(T))
        r += 1



while True:
    print("1: Person einspeichern. / 2: Person auslesen. / 3: Eine Person löschen. / 4: Liste. (" + str(date.year) + ")")
    choos = int(input("Bitte gebe die passende Zahl an: "))

    if choos == 1:
        print(" ")
        print(" ")
        print(" ")
        print("___Speichern___")
        f = input("Vorname: ")
        l = input("Nachname: ")
        a = input("Alter: ")
        y = input("Geburtsjahr: ")
        save(f, l, a, y)

    elif choos == 2:
        print(" ")
        print(" ")
        print(" ")
        print("___Lesen___")
        read(int(input("Nummer der Person: ")))

    elif choos == 3:
        print(" ")
        print(" ")
        print(" ")
        print("___Löschen___")
        remove(int(input("Nummer der Person: ")))

    elif choos == 4:
        print(" ")
        print(" ")
        print(" ")
        print("___Liste___")
        list()
        print(" ")
        print(" ")
        print(" ")


    else:
        print(" ")
        print(" ")
        print(" ")
        print("ERROR!")
        print(" ")
        print(" ")
        print(" ")
