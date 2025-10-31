from enum import Enum

class TypUmowy(Enum):
    CYWILNA = 'C'
    PRACOWNICZA = 'E'
    
    @staticmethod
    def z_kodu(kod):
        for typ in TypUmowy:
            if typ.value == kod:
                return typ
        raise ValueError(f"Unknown type of contract:: {kod}")