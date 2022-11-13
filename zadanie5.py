# Dla następującego fragmentu kodu:
# parzyste = range(2, 100, 2) proszę:
# •	trzy pierwsze elementy przypisać do zmiennych:
# pierwsza, druga, trzecia, pozostałe elementy należy przypisać do zmiennej reszta

# •	przypisać do zmiennych początek i koniec odpowiednio
# pierwszą i ostatnią wartość z parzyste

# •	zbudować listę zawierającą wszystkie elementy poza pierwszym i ostatnim

parzyste = range(2, 100, 2)

zmienna1 = parzyste[0]
zmienna2 = parzyste[1]
zmienna3 = parzyste[2]
reszta = list(parzyste[3:])

print(list(parzyste))
print(zmienna1, zmienna2, zmienna3)
print(list(reszta))

poczatek = parzyste[0]
print(poczatek)
koniec = parzyste[len(parzyste)-1]
print(koniec)