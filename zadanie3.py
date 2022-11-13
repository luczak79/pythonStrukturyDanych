# Proszę zbudować listę, zawierającą jedynie liczby podzielne bez reszty przez 3
# z zakresu 1-100 włącznie. Następnie proszę:
# •	Usunąć z utworzonej listy co drugi element zaczynając od piątego i ją wyświetlić.
# •	Z finalnej wersji listy proszę wyliczyć średnią i ją wyświetlić.

lista = []
for i in range(3, 101):
    if (i % 3 == 0):
        lista.append(i)

print(lista)

lista2 = range(3,100,3)
print(list(lista2))

