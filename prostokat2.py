a = input("wysokosc ") #ilosc kolumn
b = input("dlugosc ") #ilosc wierszy
for x in range(0,a):
	print 
	for y in range(0,b):
		print '*', #,kolejne kolumny
		y+=1
	x+=1
	