from logika.fabryka_podatkow import FabrykaPodatkow
from logika.typ_umowy import TypUmowy
from narzedzia.obsluga_wejscia import ObslugaWejscia
from narzedzia.drukarka import Drukarka

dochod = 0
typ_umowy = None

def main():
    global dochod, typ_umowy
    dochod = ObslugaWejscia.pobierz_dochod()
    typ_umowy = ObslugaWejscia.pobierz_typ_umowy()
    try:
        if typ_umowy == TypUmowy.PRACOWNICZA:
            print("EMPLOYMENT")
        elif typ_umowy == TypUmowy.CYWILNA:
            print("CIVIL")
            
        obliczanie_podatku = FabrykaPodatkow.utworz_obliczanie_podatku(typ_umowy, dochod)
        obliczanie_podatku.oblicz()
        Drukarka.drukuj(obliczanie_podatku.pobierz_dane_do_wydruku())
    except ValueError as e:
        print(str(e))

if __name__ == "__main__":
    main()