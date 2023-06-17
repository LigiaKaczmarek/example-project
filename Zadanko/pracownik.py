import csv

class Pracownik:
    def __init__(self, imie, nazwisko, wynagrodzenie_brutto):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wynagrodzenie_brutto = float(wynagrodzenie_brutto)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    def pensja_brutto(self):
        return self.wynagrodzenie_brutto

    def oblicz_wynagrodzenie_netto(self):
        wynagrodzenie_netto = self.wynagrodzenie_brutto * 0.68
        return wynagrodzenie_netto

    def oblicz_calkowity_koszt(self):
        koszt_pracodawcy = self.wynagrodzenie_brutto * 1.19 
        return koszt_pracodawcy

    @staticmethod
    def oblicz_calkowity_koszt_pracodawcy(pracownicy):
        koszt_pracodawcy = 0
        for pracownik in pracownicy:
            koszt_pracodawcy += pracownik.oblicz_calkowity_koszt()
        return koszt_pracodawcy

pracownicy = []
with open('/Users/ligiakaczmarek/example-project/Zadanko/praca.csv', 'r', newline='') as plik_csv:
    czytnik_csv = csv.DictReader(plik_csv)
    for wiersz in czytnik_csv:
        imie = wiersz['imie']
        nazwisko = wiersz['nazwisko']
        wynagrodzenie_brutto = wiersz['wynagrodzenie_brutto']
        pracownik = Pracownik(imie, nazwisko, wynagrodzenie_brutto)
        pracownicy.append(pracownik)

for pracownik in pracownicy:
    print("Pracownik:", pracownik)
    print("Pensja brutto:", pracownik.pensja_brutto())
    print("Pensja netto:", pracownik.oblicz_wynagrodzenie_netto())
    print("Koszty pracodawcy:", pracownik.oblicz_calkowity_koszt())
    print("---------")

suma_kosztow = Pracownik.oblicz_calkowity_koszt_pracodawcy(pracownicy)
print("Suma kosztów wynagrodzeń:", suma_kosztow)



        

