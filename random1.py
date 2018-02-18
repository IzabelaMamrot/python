# program wypelniajacy tablice o zadanej wielkosci losowymi wartosciami z przedzialu 100-200
import random
a=[]
print("podaj wymiar")
b=int(input()) #wymiar tablicy

for i in range(0,b): #rozmiar tab
    x=100*random.random()+100 #do randoma, ktory ma przedzial 0-1 musimy zrobic przedziala 100-200
    a.append(x) #random losuje liczby z przedzialu od 100-200
print (a)

#x = random.random 	# generuje liczbe z zakresu (0,1)
#x * 100 		# mnoży liczby (0,1) razy 100 czyli zmieni sie na (0*100, 1*100) -> (0,100)
#zakres od a do b
#to * (b-a)
#+a