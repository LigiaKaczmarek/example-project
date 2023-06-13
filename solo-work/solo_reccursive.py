# dodawanie elementow w tablicy, F-cja sumowanie listy(sum_list) przyjmuje liste l
# is l empty? y-> 0, n-> l[0](obiekt pierwszy) + reszta(sum_list(reszta))
# mamy liste [1,2,3] n wiec 1 + f[2,3] -> 2 +f[3] -> 3 i pusta wiec suma dla listy 6
# return wynik





from unittest import result


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
print("Największy element w liście to", max_element)

#2. Suma Listy
#Suma_listy
# is l empty ? 
#(yes) y -> 0
#(no) n -> l(0) + suma(reszta)
#Funkcja suma_listy,przyjmująca listę jako argment

def suma_listy (lista):
    if len(lista) == 0:    
        return 0           
    else:
        return lista[0] + suma_listy(lista[1:])   

#ligia_lista- zawiera dwolne argumenty
#wywołanie sumy listy
ligia_lista = [1,2,3]
sum = suma_listy(ligia_lista)
print(f"Suma listy wynosi", sum)
print("------------")

#3. Silnia
#Silnia(n)
# Czy n = 0     ?     
# (yes) y -> 1 bo 0!=1
# (no)  y -> n * silnia(n-1)

def Silnia(n):
    if n == 0:       
        return 1
    else:
        return n * Silnia(n-1)
Cyfra = 3
result = Silnia(Cyfra)
print(f"Silnia wynosi:", result)
print("----------")

#4. Ciąg fibonaciego
#Fibonacci(n)
# Czy n <=1 ?         
# (yes) y -> n        
# (no)  y -> fibonacci(n-1) + fibonacci(n-2)      

def Fibonacci(n):
    if n <= 1:               
        return n             
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)  
Cyfra= 4
result = Fibonacci(Cyfra)
print(f"Wartosc n-tego elementu ciągu wynosi", result)
print("------")


#5. SUDOKU 4x4

#1. board = 4X4
#2. F-cja empty_cell = Wyszukiwanie pustego pola -empty_cell
#3. F-cja Rekursja = Brak pustych pól = rozwiazanie
#4. Jeżeli wstawienie cyfry jest poprawne, przypisz ją do pola
#5. Rekurencyjne rozwiązanie sudoku
#6. Jeżeli rekurencja zakończyła się niepowodzeniem, cofnięto wstawioną cyfrę
#7. Sprawdzenie czy plansza jest poprawnego rozmiaru


def solve_sudoku(board):
    size = len(board)

    def empty_cell():
        for row in range(size):
            for col in range(size):
                if board[row][col] == 0:
                    return row, col
        return None, None

    def Rekursja():
        row, col = empty_cell()
        if row is None:
            return True

        for num in range(1, size + 1):
            if solve_sudoku(board, row, col, num):
                board[row][col] = num
                if Rekursja():
                    return True
                board[row][col] = 0
        return False

    if size < 4 or size % 2 != 0:
        print("Niepoprawny rozmiar planszy!")
        return

    if Rekursja():
        print("Rozwiązane Sudoku:")
        for row in board:
            print(row)
    else:
        print("Błąd = Nie można rozwiązać Sudoku dla danej planszy.")


# Przykładowa-dowolna plansza Sudoku 4x4
sudoku_board = [
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0],
    [0, 2, 0, 0]
]

solve_sudoku(sudoku_board)

