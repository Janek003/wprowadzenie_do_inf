import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("brak rozwiazan")

elif delta == 0:    
    x0 = -b/(2*a)
    print(f"jedno rozwiazanie, dla: {x0}")

else:
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)

    print(f"dwa rozwiazania dla: {x1} oraz {x2}")

input("Nacisnij dowolny klawisz aby wyjsc...")