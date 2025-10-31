from logika.typ_umowy import TypUmowy
import sys

class ObslugaWejscia:
    @staticmethod
    def pobierz_dochod():
        try:
            dochod = float(input("Enter income: "))
            return dochod
        except ValueError as ex:
            raise ValueError("Incorrect contract type input") from ex
    
    @staticmethod
    def pobierz_typ_umowy():
        try:
            kod = input("Contract Type: (E)mployment, (C)ivil: ")
            typ_umowy = TypUmowy.z_kodu(kod[0])
            return typ_umowy
        except ValueError:
            print("Unknown type of contract!")
            sys.exit(1)
        except (IndexError, EOFError) as e:
            print("Error reading input!")
            print(str(e))
            sys.exit(1)