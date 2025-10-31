from abc import ABC, abstractmethod
from collections import OrderedDict

class ObliczaniePodatku(ABC):
    def __init__(self, dochod):
        self.dane_podatkowe = OrderedDict()
        self.dochod = dochod
        self.dochod_poczatkowy = dochod
        self.podatek_ubezpieczenia_spolecznego = 0.0
        self.podatek_ubezpieczenia_zdrowotnego_spolecznego = 0.0
        self.podatek_ubezpieczenia_chorobowego = 0.0
        self.podstawowy_podatek_zdrowotny = 0.0
        self.wtorny_podatek_zdrowotny = 0.0
        self.podatek_kosztow_uzyskania = 0.0
        self.dochod_opodatkowany = 0.0
        self.dochod_opodatkowany_zaokraglony = 0.0
        self.podatek_zaliczkowy = 0.0
        self.dochod_wolny_od_podatku = 0.0
        self.zaplacony_podatek_zaliczkowy = 0.0
        self.zaplacony_podatek_zaliczkowy_zaokraglony = 0.0
        self.dochod_netto = 0.0
        self.zaplacony_podatek = 0.0
    
    def oblicz(self):
        self.oblicz_podatki_ubezpieczenia_spolecznego()
        self.oblicz_podatki_zdrowotne()
        self.oblicz_podatek_kosztow_uzyskania()
        self.oblicz_podatek_zaliczkowy()
        self.oblicz_dochod_netto()
    
    @abstractmethod
    def oblicz_podatki_ubezpieczenia_spolecznego(self):
        pass
    
    @abstractmethod
    def oblicz_podatki_zdrowotne(self):
        pass
    
    @abstractmethod
    def oblicz_podatek_kosztow_uzyskania(self):
        pass
    
    @abstractmethod
    def oblicz_podatek_zaliczkowy(self):
        pass
    
    @abstractmethod
    def oblicz_dochod_netto(self):
        pass
    
    def pobierz_dane_do_wydruku(self):
        return self.dane_podatkowe