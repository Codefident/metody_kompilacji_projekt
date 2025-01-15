# Metody i algorytmy kompilacji - projekt #
Konwerter języka Python do języka Javascript

- Założenia programu
  - Program zczytuje kod w języku Python i konwertuje go na język Javascript zapisany w pliku wynikowym
  - Rodzaj translatora: kompilator (przekształca od razu cały kod)
  - Wynik działania programu:
    - Poprawny kod: wypisanie drzewa z tokenami i regułami oraz zapisanie przetworzonego kodu w pliku wynikowym
    - Niepoprawny kod: wypisanie komunikatu błędu wraz ze wskazaniem błędnego fragmentu kodu
  - Język implementacji: Python
  - Skaner oraz parser wygenerowane przy użyciu narzędzia Lark

- [Tokeny](https://github.com/Codefident/metody_kompilacji_projekt/blob/main/tokens.md)
- Gramatyka
  - Format: EBNF
  - [Link do gramatyki](https://github.com/Codefident/metody_kompilacji_projekt/blob/main/python_grammar.lark)

- Generator skanera/parsera: Lark


## Instrukcja instalacji i użycia programu ##

- instalacja wymaganych bibliotek: `pip install -r requirements.txt`
- użycie programu: `py main.py [ścieżka do pliku z kodem Pythona, który chcemy przetworzyć]`
- przetworzony kod znajduje się w pliku `output.js`
- testy: `py test.py`

## Przykłady ##
**TODO**
