def trojkat(bok_a, bok_b, bok_c, wysokosc_a):
    obwod = bok_a + bok_b + bok_c
    pole = (bok_a * wysokosc_a) / 2
    return obwod, pole
    

# kwadrat, prostokat dla studenta 1
def kwadrat(bok):
    pole = (bok * bok)
    obwod = (bok * 4)
    return obwod, pole


def prostokat(bok_a, bok_b):
    pole = (bok_a * bok_b)
    obwod = (2 * bok_a + 2 * bok_b)
    return obwod, pole

# rownoleglobok i romb dla studenta 2
def rownoleglobok(bok_a, bok_b, wysokosc_a):
    obwodRW = (bok_a*2)+(bok_b*2)
    poleRW = bok_a * wysokosc_a 
    return obwodRW, poleRW

def romb(bok, wysokosc):
    obwodR = bok * 4
    poleR = bok * wysokosc
    return obwodR, poleR 

# trapez i kolo dla studenta 3
def trapez(bok_a, bok_b, bok_c, bok_d, wysokosc_a):
    pole = (bok_a+bok_b)*wysokosc_a/2
    obwod = bok_a+bok_b+bok_c+bok_d
    return obwod, pole


def kolo(promien, pi):
    pole = pi*promien^2
    obwod = 2*pi*promien
    return pole,obwod


assert trojkat(10, 15, 16, 8) == (41, 40)
assert kwadrat(20) == (80, 400)
assert prostokat(12, 10) == (44, 120)
assert rownoleglobok(6, 5, 2) == (22, 12)
assert romb(10, 5) == (40, 50)
assert trapez(10, 15, 7, 14, 2) == (46, 25)
# TODO na koniec! dopisz 2 testy dla kola i dla kazdej innej figury po jednym dodatkowym tescie
assert rownoleglobok(5, 5, 5) == (20, 25)
assert romb(12, 8) == (48, 96)
assert kwadrat(10) == (40, 100)
assert prostokat(10, 20) == (60, 200)
