

def near_hundred(n):
    if (abs(100 - n) <= 10) or (abs(200 - n) <= 10):
        return True
    else:
        return False

print ('Wywolujemy near_hundred(93)')
wynik = near_hundred(93)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy near_hundred(90)')
wynik = near_hundred(90)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy near_hundred(89)')
wynik = near_hundred(89)
print ('Wynik funkcji to', wynik)
