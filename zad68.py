def jednolity(napis):
    for i in range(len(napis)):
        if napis[i] != napis[i+1]:
            return False
    return True


lista_napisow = []
with open("dane_napisy.txt") as plik:
    for linia in plik:
        lista_napisow.append(linia.strip())
print(lista_napisow)
licznik = 0
for napisy in lista_napisow:
    if napisy[0] == napisy[1]:
        if jednolity(napisy[0]):
            licznik += 1
print(licznik)

licznik = 0
for napisy in lista_napisow:
    if sorted(napisy[0]) == sorted(napisy[1]):
        licznik += 1
print(licznik)