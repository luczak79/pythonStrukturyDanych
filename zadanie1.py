# Proszę zbudować krotkę zawierającą zmienne typu int z przedziału (0,5) oraz zmienne typu str opisujące słownie cyfry z przedziału (5,10),
# czyli „pięć”, „sześć” etc. Następnie proszę:
# •	Stworzyć i wyświetlić listę z dwóch pierwszych elementów.
# •	Zbudować osobną krotkę z trzech ostatnich elementów, a następnie ją wyświetlić.
# •	Zbudować kolejną listę zawierającą co drugi element krotki (zaczynając od pierwszego indeksu) i ją wyświetlić.
# •	Sprawdzić funkcją len() długość szóstego elementu początkowej krotki i ją wyświetlić.

mojaKrotka = (0, 1, 2, 3, 4, 5, 'piec', 'sześć', 'siedem', 'osiem', 'dziewiec', 'dzieciec')


# •	Stworzyć i wyświetlić listę z dwóch pierwszych elementów.
newKrotka = mojaKrotka[0:2]
print(newKrotka)

# •	Zbudować osobną krotkę z trzech ostatnich elementów, a następnie ją wyświetlić.
newKrotka = mojaKrotka[-3:]
print(newKrotka)

# •	Zbudować kolejną listę zawierającą co drugi element krotki (zaczynając od pierwszego indeksu) i ją wyświetlić.
newKrotka2 = mojaKrotka[1::2]
print(newKrotka2)

# •	Sprawdzić funkcją len() długość szóstego elementu początkowej krotki i ją wyświetlić.
print(mojaKrotka[6].__len__())









