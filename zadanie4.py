# Proszę zbudować krotkę, zawierającą cztery elementy będące dowolnymi literami alfabetu. Następnie korzystając z dokumentacji str.join proszę wyświetlić dane litery w takiej formie:
# •	'xyhw'
# •	‘x y h w'
# •	'x,y,h,w'

krotka = ('x', 'y', 'h', 'w')

krotkaString = krotka
print(krotkaString)

print("".join(krotka))
print(" ".join(krotka))
print(",".join(krotka))