def tekst_hex():
    print("Program do konwersji HEX->BASE, BASE-> HEX")
    odp = input("""Wybierz:
    1. Dla HEX->BASE
    2. DLA BASE->HEX""")
    print(odp)
    if odp == "1":
        liczba = input("Podaj liczbe HEX").lower()
        try:
            wynik = int(liczba,16)
            print (wynik)
        except ValueError:
            print("Nie jest to liczba HEX. Sprobuj jeszcze raz")
            tekst_hex()
    elif odp == "2":
        liczba = input("Podaj liczbe dziesietna").lower()
        try:
            wynik = int(liczba)
            wynik = hex(wynik)
            print (wynik)
        except ValueError:
            print("Nie jest to liczba dziesietna sprobuj jeszcze raz. Sprobuj jeszcze raz")
            tekst_hex()
    else:
        print("ERROR. Wybierz opcje klikajac 1 lub 2.")
        tekst_hex()
tekst_hex()

