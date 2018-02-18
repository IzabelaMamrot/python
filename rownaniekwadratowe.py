#rownaniekwadratowe delta=b^2-4ac
import math
print("podaj a, b, c")
a=int(input())
b=int(input())
c=int(input())
delta=b**2-4*a*c #math.pow(b,2)
print (delta)

if delta>0 and a!=0:
    x1=(-b-(delta)**(0.5))/(2*a)
    x2=(-b+(delta)**(0.5))/(2*a)
    print("{} x1 wynosi, {} x2 wynosi".format(x1,x2), )
elif delta==0 and a!=0:
    x0=(-b)/(2*a)
    print("x0 wynosi",x0)
elif delta<0 and a!=0:
    "brak miejsc zerowych"
else:
    print("nie dziel przez zero")
