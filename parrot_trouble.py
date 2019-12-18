# parametr „godzina” to bieżący czas w zakresie 0..23
# Mamy kłopoty, jeśli papuga mówi, a godzina jest przed 7 lub po 20
# zwroc True jesli mamy klopoty

def parrot_trouble(talking, hour):
    if talking == True and hour > 7 or talking == True and hour < 20:
        return True
    else:
        return False


print ('Wywolujemy parrot_trouble(True, 6)')
wynik = parrot_trouble(True, 6)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy parrot_trouble(True, 7)')
wynik = parrot_trouble(True, 7)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy parrot_trouble(False, 6)')
wynik = parrot_trouble(False, 6)
print ('Wynik funkcji to', wynik)
