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
print(tuple(lista))
