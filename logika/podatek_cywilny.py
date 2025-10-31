from logika.obliczanie_podatku import ObliczaniePodatku

class PodatekCywilny(ObliczaniePodatku):
    PROCENT_PODATKU_UBEZPIECZENIA_SPOLECZNEGO = 9.76
    PROCENT_PODATKU_UBEZPIECZENIA_ZDROWOTNEGO_SPOLECZNEGO = 1.5
    PROCENT_PODATKU_UBEZPIECZENIA_CHOROBOWEGO = 2.45
    PROCENT_PODSTAWOWEGO_PODATKU_ZDROWOTNEGO = 9
    PROCENT_WTORNEGO_PODATKU_ZDROWOTNEGO = 7.75
    PROCENT_PODATKU_ZALICZKOWEGO = 18
    PROCENT_PODATKU_KOSZTOW_UZYSKANIA = 20
    
    def __init__(self, dochod):
        super().__init__(dochod)
        self.dochod_wolny_od_podatku = 0
    
    def oblicz_podatki_ubezpieczenia_spolecznego(self):
        self.podatek_ubezpieczenia_spolecznego = (self.dochod * self.PROCENT_PODATKU_UBEZPIECZENIA_SPOLECZNEGO) / 100
        self.podatek_ubezpieczenia_zdrowotnego_spolecznego = (self.dochod * self.PROCENT_PODATKU_UBEZPIECZENIA_ZDROWOTNEGO_SPOLECZNEGO) / 100
        self.podatek_ubezpieczenia_chorobowego = (self.dochod * self.PROCENT_PODATKU_UBEZPIECZENIA_CHOROBOWEGO) / 100
        self._zapisz_podatek_ubezpieczenia_spolecznego()
        self.dochod = self.dochod - self.podatek_ubezpieczenia_spolecznego - self.podatek_ubezpieczenia_zdrowotnego_spolecznego - self.podatek_ubezpieczenia_chorobowego
        self._zapisz_podstawowy_dochod()
    
    def _zapisz_podstawowy_dochod(self):
        self.dane_podatkowe["Income for calculating health security tax"] = self.dochod
    
    def _zapisz_podatek_ubezpieczenia_spolecznego(self):
        self.dane_podatkowe["Income"] = self.dochod_poczatkowy
        self.dane_podatkowe["Social security tax"] = self.podatek_ubezpieczenia_spolecznego
        self.dane_podatkowe["Health social security tax"] = self.podatek_ubezpieczenia_zdrowotnego_spolecznego
        self.dane_podatkowe["Sickness social security tax  "] = self.podatek_ubezpieczenia_chorobowego
    
    def oblicz_podatki_zdrowotne(self):
        self.podstawowy_podatek_zdrowotny = (self.dochod * self.PROCENT_PODSTAWOWEGO_PODATKU_ZDROWOTNEGO) / 100
        self.wtorny_podatek_zdrowotny = (self.dochod * self.PROCENT_WTORNEGO_PODATKU_ZDROWOTNEGO) / 100
        self._zapisz_podatek_zdrowotny()
    
    def _zapisz_podatek_zdrowotny(self):
        self.dane_podatkowe["Health security tax: 9%"] = self.podstawowy_podatek_zdrowotny
        self.dane_podatkowe["Health security tax: 7,75%"] = self.wtorny_podatek_zdrowotny
    
    def oblicz_podatek_kosztow_uzyskania(self):
        self.podatek_kosztow_uzyskania = (self.dochod * self.PROCENT_PODATKU_KOSZTOW_UZYSKANIA) / 100
        self.dochod_opodatkowany = self.dochod - self.podatek_kosztow_uzyskania
        self._zapisz_dochod_opodatkowany()
    
    def _zapisz_dochod_opodatkowany(self):
        self.dane_podatkowe["Tax deductible expenses"] = self.podatek_kosztow_uzyskania
        self.dane_podatkowe["income to be taxed"] = self.dochod_opodatkowany
        self.dochod_opodatkowany_zaokraglony = float("{0:.0f}".format(self.dochod_opodatkowany))
    
    def oblicz_podatek_zaliczkowy(self):
        self.podatek_zaliczkowy = (self.dochod_opodatkowany_zaokraglony * self.PROCENT_PODATKU_ZALICZKOWEGO) / 100
        self.zaplacony_podatek = self.podatek_zaliczkowy
        self.zaplacony_podatek_zaliczkowy = self.podatek_zaliczkowy - self.wtorny_podatek_zdrowotny - self.dochod_wolny_od_podatku
        self.zaplacony_podatek_zaliczkowy_zaokraglony = float("{0:.0f}".format(self.zaplacony_podatek_zaliczkowy))
        self._zapisz_podatek_zaliczkowy()
    
    def _zapisz_podatek_zaliczkowy(self):
        self.dane_podatkowe["rounded"] = self.zaplacony_podatek_zaliczkowy_zaokraglony
        self.dane_podatkowe["Advance tax 18%"] = self.podatek_zaliczkowy
        self.dane_podatkowe["Already paid tax"] = self.zaplacony_podatek
        self.dane_podatkowe["Advance tax"] = self.zaplacony_podatek_zaliczkowy
    
    def oblicz_dochod_netto(self):
        self.dochod_netto = self.dochod_poczatkowy - ((self.podatek_ubezpieczenia_spolecznego + self.podatek_ubezpieczenia_zdrowotnego_spolecznego + self.podatek_ubezpieczenia_chorobowego) + self.podstawowy_podatek_zdrowotny + self.zaplacony_podatek_zaliczkowy_zaokraglony)
        self._zapisz_dochod_netto()
    
    def _zapisz_dochod_netto(self):
        self.dane_podatkowe["Net income"] = self.dochod_netto