# Proszę zbudować listę studentów składającą się z czterech osób, a następnie proszę:
# •	Korzystając z funkcji append() dodać do listy kolejną osobę.
# •	Korzystając z funkcji extend() dodać dwie osoby.
# •	Posortować i wyświetlić alfabetycznie studentów, najpierw rosnąco, następnie malejąco.
# •	Wydrukować na ekranie:
# o	Drugiego studenta na liście.
# o	Czwartego oraz piątego studenta.
# o	Trzech ostatnich studentów.
# •	Usunąć przedostatniego studenta na liście, korzystając z odpowiedniej funkcji i wyświetlić listę.
# •	Utworzyć krotkę z finalnej wersji listy i ją wyświetlić.


lista = ['Janek', 'Ola', 'Tomek', 'Marcin']

lista.append('Janusz')
lista.extend(['Mirek', 'Gosia'])
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print(lista.__getitem__(1))
print(lista[3:5])
print(lista[-3:])
lista.remove(lista[-2])
print(lista)
krotka = tuple(lista)
print(krotka)
