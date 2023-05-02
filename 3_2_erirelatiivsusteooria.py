# Nädal 3, ülesanne 2 - Einsteini erirelatiivsusteooria

def summa(u, v):
    c = 299792.458
    return (u + v) / (1 + (u * v)/(c * c))

u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese suhtes on: "))
x = float(input("Kolmanda keha kiirus teise suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda suhtes on: "))

print("Kiiruste summa on " + str(summa(summa(summa(u, v), x), y)) + " km/s")
