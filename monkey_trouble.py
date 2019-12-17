# funkcja monkey_trouble sprawdza kiedy mamy klopoty
# jeśli mamy kłopoty, dwie @ się umismiechaja badz dwie @ sie nie usmiechaja


def monkey_trouble(a_smile, b_smile):
    if a_smile == True and b_smile == True:
        return True
    elif a_smile == False and b_smile == False:
        return True
    else:
        return False


print ('Wywolujemy funkcje monkey_trouble(True, True)')
wynik = monkey_trouble(True, True)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy funkcje monkey_trouble(False, False)')
wynik = monkey_trouble(False, False)
print ('Wynik funkcji to', wynik)

print ('Wywolujemy funkcje monkey_trouble(True, False)')
wynik = monkey_trouble(True, False)
print ('Wynik funkcji to', wynik)
