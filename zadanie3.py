# Proszę zbudować listę, zawierającą jedynie liczby podzielne bez reszty przez 3
# z zakresu 1-100 włącznie. Następnie proszę:
# •	Usunąć z utworzonej listy co drugi element zaczynając od piątego i ją wyświetlić.
# •	Z finalnej wersji listy proszę wyliczyć średnią i ją wyświetlić.

# lista = []
# for i in range(3, 101):
#     if (i % 3 == 0):
#         lista.append(i)
#
# print(lista)

test_list = list(range(3,100,3))
remove_list = test_list[5::2]

wynik = [i for i in test_list if i not in remove_list]

print(wynik)

del test_list[5::2]
print(test_list)

print(sum(test_list)/len(test_list))



