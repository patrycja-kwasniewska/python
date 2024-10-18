def liczba_dni(miesiac, rok):
    if 1800 <= rok <= 2200:
        if miesiac in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif miesiac in [4, 6, 9, 11]:
            return 30
        elif miesiac == 2:
            if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
                return 29  # Rok przestępny
            else:
                return 28
        else:
            return "Błędny miesiąc"
    else:
        return "Błędny rok"


from datetime import datetime


def czas_systemowy():
    teraz = datetime.now()

    # Wyświetlenie aktualnej daty i godziny
    print("Aktualna data i czas:", teraz)

    # Obliczenie procentu dnia, który minął
    sekundy_dnia = 24 * 60 * 60
    minelo_sekund = teraz.hour * 3600 + teraz.minute * 60 + teraz.second
    procent_dnia = (minelo_sekund / sekundy_dnia) * 100
    print(f"Minęło {procent_dnia:.2f}% dnia.")

    # Obliczenie procentu miesiąca, który minął
    dni_w_miesiacu = liczba_dni(teraz.month, teraz.year)
    minelo_dni = teraz.day
    procent_miesiaca = (minelo_dni / dni_w_miesiacu) * 100
    print(f"Minęło {procent_miesiaca:.2f}% miesiąca.")

    # Obliczenie procentu roku, który minął
    dni_w_roku = 366 if (teraz.year % 4 == 0 and teraz.year % 100 != 0) or (teraz.year % 400 == 0) else 365
    dzien_roku = teraz.timetuple().tm_yday
    procent_roku = (dzien_roku / dni_w_roku) * 100
    print(f"Minęło {procent_roku:.2f}% roku.")

# sprawdzenie
print(liczba_dni(2,2018))
czas_systemowy()