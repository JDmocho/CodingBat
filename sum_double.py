# funkcja sum_double zwraca sume dwoch wartosci
# jesli dwie wartosci nie sa takie same zwroci dwukrotnosc sumy

def sum_double(a, b):
    if a == b:
        return 2*(a+b)
    elif a != b:
        return a + b

print ('Wywolujemy funkcje sum_double(1, 2)')
wynik = sum_double(1, 2)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy funkcje sum_double(3, 2)')
wynik = sum_double(3, 2)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy funkcje sum_double(2, 2)')
wynik = sum_double(2, 2)
print ('Wynik funkcji to', wynik)
