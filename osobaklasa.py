class Person():
    imie =" "
    nazwisko = " "
    def dane(self):
        print(self.imie, self.nazwisko)
    def zmiendane(self):
        self.imie=input(" podaj nowe imie: ")
        self.nazwisko=inpyt(" podaj nowe nazwisko: ")

osoba=Person()
osoba2=Person()

osoba.imie="Kasia"
osoba.nazwisko="Jakas"
osoba.dane()

osoba2.imie="marysia"
osoba2.nazwisko="lala"
osoba2.dane()