# dodawanie elementow w tablicy, F-cja sumowanie listy(sum_list) przyjmuje liste l
# is l empty? y-> 0, n-> l[0](obiekt pierwszy) + reszta(sum_list(reszta))
# mamy liste [1,2,3] n wiec 1 + f[2,3] -> 2 +f[3] -> 3 i pusta wiec suma dla listy 6
# return wynik





def suma_listy(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + suma_listy(lista[1:])
ligia_lista = [1, 2, 3]
suma = suma_listy(ligia_lista)
print(suma)
# is l empty? y-> 0, n-> l[0](obiekt pierwszy) + reszta(sum_list(reszta))
# lista [1,2,3] n -> 1 + f[2,3] -> 2 +f[3] -> 3 i pusta wiec suma dla listy 6
print("------------")


#1. max wartosci
#Pseudokod
#najwieksza_wartosc - argument
#Lista ma 1 element - return 1 element
#Lista>1element - reszta listy przypisana do zmiennej reszta
#rekurencja-wywolanie najwieksza_wartosc z listy reszta
#If 1>reszta to zwracamy 1 w przeciwnym razie reszta
def najwieksza_wartosc(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        jeden = lista[0]
        reszta = lista[1:]
        reszta = najwieksza_wartosc(reszta)
        if jeden > reszta:
            return jeden
        else:
            return reszta
#ligia_lista- zawiera dwolne argumenty
#wylowanie najwieksza_wartosc
#przypisanie max_element
ligia_lista = [1,2,3]
max_element = najwieksza_wartosc(ligia_lista)
print("Największy element w liście:{ligia_lista} to", max_element)

