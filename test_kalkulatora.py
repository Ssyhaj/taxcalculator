from logika.fabryka_podatkow import FabrykaPodatkow
from logika.typ_umowy import TypUmowy

def test_obliczenia():

    testy = [
        (10000, TypUmowy.CYWILNA, 7278.39),
        (10000, TypUmowy.PRACOWNICZA, 7034.39),
        (5999, TypUmowy.CYWILNA, 4366.65),
        (5999, TypUmowy.PRACOWNICZA, 4246.65),
        (3500, TypUmowy.PRACOWNICZA, 2505.34),
        (3500, TypUmowy.CYWILNA, 2547.34),
    ]
    
    print("Rozpoczynam testy...\n")
    
    for dochod, typ_umowy, oczekiwany_wynik in testy:
        print(f"Test: dochód={dochod}, typ umowy={typ_umowy.name}")
        
        obliczanie_podatku = FabrykaPodatkow.utworz_obliczanie_podatku(typ_umowy, dochod)
        obliczanie_podatku.oblicz()
        
        dane = obliczanie_podatku.pobierz_dane_do_wydruku()
        otrzymany_wynik = dane["Net income"]
        
        print(f"  Oczekiwany: {oczekiwany_wynik:.2f}")
        print(f"  Otrzymany:  {otrzymany_wynik:.2f}")
        
        assert abs(otrzymany_wynik - oczekiwany_wynik) < 0.01, \
            f"Błąd! Dla dochodu {dochod} ({typ_umowy.name}) oczekiwano {oczekiwany_wynik:.2f}, otrzymano {otrzymany_wynik:.2f}"
        
        print("  ✓ Test passed\n")
    
    print("="*50)
    print("Wszystkie testy zakończone sukcesem!")
    print("="*50)

if __name__ == "__main__":
    test_obliczenia()
