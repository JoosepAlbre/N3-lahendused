# Nädal 3, ülesanne 3 - Moosi keetmine
def moos(s, v, kg):
    if s * 5 + v < kg: #Moosi rohkem, kui karpide kogumahutavus
        return -1

    karpide_arv = 0
    mahutatud_kogus = 0

    if s * 5 < kg: #Kõik suured karbid peab ära kasutama
        karpide_arv += s
        mahutatud_kogus = s * 5
    else: # Ei pea kõiki suuri karpe ära kasutama
        karpide_arv += int(kg/5)
        mahutatud_kogus = karpide_arv * 5

    if mahutatud_kogus == kg: # Moosi saab mahutatud ainult suurte karpidega
        return karpide_arv

    if mahutatud_kogus + v < kg: # Pole piisavalt väikeseid karpe, et moos täpselt ära mahutada
        return -1

    veel_vaja = kg - mahutatud_kogus
    karpide_arv += veel_vaja

    return karpide_arv
  
print(moos(2, 6, 14))
print(moos(3, 3, 8))
print(moos(1, 2, 10))
print(moos(5, 1, 9))
print(moos(10, 10, 10))
print(moos(0, 10, 10))
