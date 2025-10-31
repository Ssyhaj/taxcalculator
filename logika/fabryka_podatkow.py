from logika.typ_umowy import TypUmowy
from logika.podatek_pracowniczy import PodatekPracowniczy
from logika.podatek_cywilny import PodatekCywilny

class FabrykaPodatkow:
    @staticmethod
    def utworz_obliczanie_podatku(typ_umowy, dochod):
        if typ_umowy == TypUmowy.PRACOWNICZA:
            return PodatekPracowniczy(dochod)
        elif typ_umowy == TypUmowy.CYWILNA:
            return PodatekCywilny(dochod)
        else:
            raise ValueError(f"Nieznany typ umowy: {typ_umowy}")