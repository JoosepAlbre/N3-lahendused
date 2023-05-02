# Nädal 3, ülesanne 1 - Pagari kassaaparaat
import math

def koogi_hind(kook, x):
  if kook == "Napoleoni kook":
      return round(0.08 * x * x, 2)
  elif kook == "šokolaadikook":
      return round(0.05 * math.pi * x * x, 2)
  elif kook == "ploomikook":
      return round(0.04 * math.pi * x * x, 2)
  else:
      return -1

  nimi = input("Sisesta koogi nimi: ")
  mõõt = float(input("Sisesta koogi mõõt: "))

  hind = koogi_hind(nimi, mõõt)
  if hind < 0:
      print("Sellist kooki pagarikoda ei valmista.")
  else:
      print("Selle koogi hind on " + str(hind) + " eurot.")
