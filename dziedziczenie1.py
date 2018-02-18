#z jednej klasy do innej klasy potomna po rodzicielskiej dziedziczy zmienne, obiekty, funkcje
#class Klasa1():
 #   def wypisz1(self):
  #      print("Klasa1")
#class Klasa2(Klasa1):
 #   def wypisz2(self):
  #      print("Klasa2")
#obiekt=Klasa2()
#obiekt.wypisz1()
#obiekt.wypisz2()

class Parents():

    def nazwisko(self):
        print("Mamrot")
class Child(Parents):
    def imie(self):
        print("Iza")
osoba=Child()
osoba.nazwisko()
osoba.imie()