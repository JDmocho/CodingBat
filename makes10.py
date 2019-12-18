# bierze pod uwagę dwie liczby calkowite a i b
# funkcja makes10, zwraca True jezeli ktoras z liczb rowna sie 10 badz suma z nich rowna sie 10

def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False

print ('Wywolujemy funkcje makes10(9,10)')
wynik = makes10(9, 10)
print ('Wynik funkcji to', wynik)


print ('Wywolujemy funkcje makes10(9,9)')
wynik = makes10(9, 9)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy funkcje makes10(1,9)')
wynik = makes10(1, 9)
print ('Wynik funkcji to', wynik)
