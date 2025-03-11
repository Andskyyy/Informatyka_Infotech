with open("tekst.txt") as plik:
    tekst = plik.readline()

lista_napisow = tekst.split()
print(tekst)
licznik = 0
for napis in lista_napisow:
    for i in range(len(napis)-1):
        if napis[i] == napis[i+1]:
            licznik += 1
            break
print(licznik)

print(licznik)
slownik = {}
for znak in tekst:
    if znak != ' ' and znak !='\n':
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
print(sorted(slownik.items()))
suma = sum(slownik.values())
print(suma)
for kr in sorted(slownik.items()):
    print(kr[0], ":", kr[1],round(100*kr[1]/suma,2), "%")

