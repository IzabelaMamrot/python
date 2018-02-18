#OBIEKTOWKA - kalkulator
class Calculator():
    #def __init__(self):
     #   self.liczba=10
    def __init__(self): #init wykonuje sie automatycznie podczas tworzenia instakcji=calc
        self.ostatniwynik=0 #zeby nie bral pod uwage wszystkich wyników tylko ostatni
                            #self przechowuje poszczegolne instancjie self=calc
    def dodawanie(self,a,b):
        wynik=a+b
        print(wynik)
    def odejmowanie(self,a,b):
        wynik=a-b
        print(wynik)
    def mnozenie(self,a,b):
        wynik=a*b
        self.ostatniwynik=wynik #zastepujemy ostatni wynik ktory=0 biezacycm
        print(wynik)
calc=Calculator()
#calc.liczba+=5
#print(calc.liczba)
calc.dodawanie(5,3)
calc.odejmowanie(5,2)
calc.mnozenie(2,2)
print("ostatni wynik to: {}".format(calc.ostatniwynik))




