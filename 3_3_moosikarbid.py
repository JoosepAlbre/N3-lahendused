# Nädal 3, ülesanne 3 - Moosi keetmine
def moos(s, v, kg):
    suuri = min(s, kg//5)
    if 5*suuri + v >= kg:
        return kg - 4*suuri
    else:
        return -1
  
print(moos(2, 6, 14))
print(moos(3, 3, 8))
print(moos(1, 2, 10))
print(moos(5, 1, 9))
print(moos(10, 10, 10))
print(moos(0, 10, 10))
