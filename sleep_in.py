# funkcja sleep_in sprawdza kiedy mozemy spac
# jesli nie jest to dzien powszedni lub sa to wakacje ma zwrocic True

def sleep_in(weekday, vacation):
    if weekday == False or vacation == True:
        return True
    else:
        return False



print ('Wywolujemy funkcje sleep_in(False,False)')
wynik = sleep_in(False, False)
print ('Wynik funkcji to', wynik)


print ('Wywolujemy funkcje sleep_in(False,True)')
wynik = sleep_in(False, True)
print ('Wynik funkcji to', wynik)


print ('Wywolujemy funkcje sleep_in(True, True)')
wynik = sleep_in(True, True)
print ('Wynik funkcji to', wynik)


print ('Wywolujemy funkcje sleep_in(True, False)')
wynik = sleep_in(True, False)
print ('Wynik funkcji to', wynik)
