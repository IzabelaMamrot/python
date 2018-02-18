#wyswietlanie liczb od 1-10 petla for
#za pomoca petli for
for i in range(1,11): #petla wykona sie 10 razy poczatek od 1 koniec na 11
    print (i) # wyświetli liczby od 1-10

#za pomoca petly while
#petla while wyswietlanie liczb od 1-10

i = 1 #zmienna i ma wartosc 1
while i <=10: #jesli zmienna jest mniejsza lub rowna 10
    print (i) #wyswietla
    i+=1 #dodaj 1
    
#kolejny przyklad
suma = 0
while suma<50:
	print("liczba")
	x = input()
	suma += int(x)
	print(suma)
print

#[wyrazenie for zmienna in sekwencja if warunek]
for x in range(0,100):
	if not (x%3) or not (x%5):
		print x