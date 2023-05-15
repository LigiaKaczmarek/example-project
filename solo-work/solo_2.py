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
 



