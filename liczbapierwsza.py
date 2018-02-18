print("PROGRAM SPRAWDZAJACY CZY ZADANA LICZBA JEST LICZB? PIERWSZ?")
print("Jak? liczb? chcesz zbada??")
x = int(input())

for i in range (x):
    i += 1
    if i != 1 & i != x:
        if x % i != 0:
            continue
            print ("kupa")
        if x % i == 0:
            print("%d nie jest liczb? pierwsz?" % x)
            break
        else:
            print("%d jest liczb? pierwsz?" % x)
            break