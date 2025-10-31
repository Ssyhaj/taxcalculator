Zmiany:

Podział kodu na mniejszeczęści
Oryginalny kod był jedną dużą klasą ze statycznymi metodami, która robiła wszystko naraz. Nowy kod został podzielony na logiczne moduły czyli osobny pakiet dla logiki podatkowej, osobny dla narzędzi pomocniczych. 
Każdy typ umowyma teraz swoją własną klasę zamiast długich bloków if-elif.

Zastosowanie wzorców projektowych
Wprowadzono kilka klasycznych wzorców:
- Factory do tworzenia odpowiednich obiektów kalkulacji
- Template Method to klasa bazowa definiuje kolejność obliczeń, konkretne klasy implementują szczegóły
- Enum zamiast znaków 'E' i 'C' dla typów umów

Jedna odpowiedzialność dla każdej klasy
Zamiast jednej klasy robiącej wszystko, każda klasa ma teraz jedno, konkretne zadanie. ObslugaWejscia tylko pobiera dane od użytkownika, 
Drukarka tylko wyświetla wyniki, a klasy podatków tylko liczą. To ułatwia zrozumienie kodu i jego modyfikację.

Eliminacja duplikacji
W oryginalnym kodzie logika dla obu typów umów była powielona w długich blokach warunkowych. Teraz wspólne elementy są w klasie bazowej, a różnice w klasach pochodnych.

Lepsze nazewnictwo
Zamiast skrótów jak t_socialSecurity, d_income czy taxedIncome0, kod używa pełnych, zrozumiałych nazw. Metody prywatne są oznaczone podkreślnikiem.

Usunięcie zmiennych globalnych
Oryginalny kod używał statycznych pól klasy jak zmiennych globalnych. Nowy kod tworzy instancje obiektów z własnymi polami, co jest bezpieczniejsze i bardziej obiektowe.

Podział długich metod
Metoda main() miała ponad 60 linii i robiła wszystko - pobieranie danych, obliczenia, wyświetlanie. Teraz jest krótka i tylko koordynuje pracę innych klas. 
Obliczenia zostały podzielone na małe, jednozadaniowe metody.

Scentralizowane formatowanie
Zamiast rozrzuconych po kodzie instrukcji print() z formatowaniem, wyniki są zbierane w uporządkowanym słowniku i formatowane w jednym miejscu przez klasę Drukarka.
