from typing_extensions import Self


class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        #self.obwod = a + b + c

    def obwod(self):
        return self.a + self.b + self.c

    def pole(self):
        # TODO
        return (self.a * self.h_a)/2

    

trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_ligii = Trojkat(8, 6, 10,4)
print(trojkat_rownoboczny.obwod())

class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        #self obwod
    def obwod(self):
        return 2 * self.a + 2 * self.b
    def pole(self):
        return self.a * self.b
prostokat_ligii = Prostokat(5, 10)
print(prostokat_ligii.obwod())
print(prostokat_ligii.pole())
print("----------------------------")


class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def __int__(self):
        return 5
    
    def dodaj_oceny(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) /len(self.oceny)

student_ligia = Student("Ligia", "Kaczmarek", 123456)
student_ligia.dodaj_oceny(4.5)
student_ligia.dodaj_oceny(5)
print(int(student_ligia))
print(student_ligia.oceny)
print("--------------")


class Ubranie:
    def __init__(self, rodzaj, marka, rozmiar, kolor, material, dopasowanie, dodatki, dopasowanie_do_wieku):
        self.rodzaj = rodzaj
        self.marka = marka
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.material = material
        self.dopasowanie = dopasowanie
        self.dodatki = dodatki
        self.dopasowanie_do_wieku = dopasowanie_do_wieku
        self.ceny = []

    def __str__(self):
        return f"{self.rodzaj} {self.marka} {self.rozmiar} {self.kolor} {self.material} {self.dopasowanie} {self.dodatki} {self.dopasowanie_do_wieku} {self.ceny}"

    def dodaj_cene(self, cena):
        self.ceny.append(cena)

    def zwroc_srednia_cena(self):
        if len(self.ceny) > 0:
            return sum(self.ceny) / len(self.ceny)
        else:
            return 0.0


ubranie_Zara = Ubranie("sukienka", "Zara", "36", "biały", "bawełna", "slim", "koronka", "18lat")
ubranie_Zara.dodaj_cene(100)
ubranie_Zara.dodaj_cene(150)

ubranie_nike = Ubranie("spodnie", "Nike", "M", "czarny", "poliester", "luźne", "brak", "dowolny")
ubranie_nike.dodaj_cene(80)
ubranie_nike.dodaj_cene(90)
ubranie_nike.dodaj_cene(100)

print(ubranie_Zara)
print(ubranie_nike)

print("Średnia cena dla ubrania Ligia:", ubranie_Zara.zwroc_srednia_cena())
print("Średnia cena dla ubrania Nike:", ubranie_nike.zwroc_srednia_cena())

print("-----------------------")





    
    









