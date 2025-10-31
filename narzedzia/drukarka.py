class Drukarka:
    @staticmethod
    def drukuj(dane):
        for klucz in dane.keys():
            print(f"{klucz} : {dane[klucz]:.2f}")