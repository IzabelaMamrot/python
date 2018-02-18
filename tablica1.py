#zbudowac taka tablice b w ktorej wartosci z tablicy a beda mniejsze od liczby zadanej przez uzytkownika
a = [1,25,2,523,95,5932,1954,12,94]
print("podaj liczbe")
b=[]
x=int(input())
for i in a: #a = [1 ,50 , 70] # for i in a -> i = 1, i = 50, i = 70 # for i in range (a) -> i = 0, i = 1, i = 2
    if x<i:
        b.append(i)
print(b)

#a = [ 1, 25, 2, 523, 95, 5932, 1954, 12, 94]
#x = int(input())
#b = [liczba for liczba in a if liczba < x]
#print (b)