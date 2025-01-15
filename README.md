# Metody i algorytmy kompilacji - projekt

## Konwerter języka Python do języka Javascript

- Założenia programu
  - Program zczytuje kod w języku *Python* i konwertuje go na język *Javascript* zapisany w pliku wynikowym
  - Rodzaj translatora: **kompilator** (przekształca od razu cały kod)
  - Wynik działania programu:
    - Poprawny kod: wypisanie drzewa z tokenami i regułami oraz zapisanie przetworzonego kodu w pliku wynikowym
    - Niepoprawny kod: wypisanie komunikatu błędu wraz ze wskazaniem błędnego fragmentu kodu
  - Język implementacji: **Python 3.13.0**
  - Generator skanera/parsera: **Lark** (1.2.2)

- [Tokeny](https://github.com/Codefident/metody_kompilacji_projekt/blob/main/tokens.md)
- Gramatyka
  - Format: **EBNF**
  - [Link do gramatyki](https://github.com/Codefident/metody_kompilacji_projekt/blob/main/python_grammar.lark)

- Generator skanera/parsera: **Lark** (1.2.2)

- Generator kodu: dostosowany do gramatyki **Transformer** pochodzący z biblioteki **Lark**

## Dodatkowe informacje

Generator jest w stanie przekształcić instrukcję `for i in range(2, 10, 2)` na *for* w stylu *C++* a więc `for (let i = 2, i < 10, i += 2)`. Mimo to na początku pliku wynikowego generator dodaje napisane w *Javascript* funkcje `range()` oraz `len()` działające analogicznie do tych w *Python*. Można je zobaczyć w jednym z przykładów poniżej.

## Instrukcja instalacji i użycia programu

- instalacja wymaganych bibliotek: `pip install -r requirements.txt`
- użycie programu: `py main.py [ścieżka do pliku z kodem Pythona, który chcemy przetworzyć]`
- przetworzony kod znajduje się w pliku `output.js`
- testy: `py test.py`

## Przykłady

### Poprawny kod

Dla `pos_2.py`:

```python
my_list = []

for i in range(5):
    my_list.append(i * 3)

for elem in my_list:
    print(elem)
```

Drzewo wyprowadzenia (w konsoli):

```console
Tree:
start
  assign_stmt
    assign
      assign_target     my_list
      expr
        atom_expr
          atom
            list_expr
  for_stmt
    for
    i
    in
    expr
      atom_expr
        func_call
          atom_expr
            atom        range
          arguments
            expr        5
    block
      expr
        atom_expr
          func_call
            atom_expr
              dot_access
                atom_expr
                  atom  my_list
                append
            arguments
              mul
                expr
                  atom_expr
                    atom        i
                expr    3
  for_stmt
    for
    elem
    in
    expr
      atom_expr
        atom    my_list
    block
      expr
        atom_expr
          func_call
            atom_expr
              atom      print
            arguments
              expr
                atom_expr
                  atom  elem
```

Plik wynikowy `output.js`

```js
let range = (start, stop, step) => {
    if (stop === undefined) {
        stop = start;
        start = 0;
    }

    if (step === undefined)
        step = 1;
    else if (step == 0)
        throw new Error("step cannot be 0");

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop))
        return [];

    let result = [];
    for (let i = start; step > 0 ? i < stop : i > stop; i += step)
        result.push(i);
    return result;
}

let len = (obj) => {
    if (typeof obj === "string" || Array.isArray(obj))
        return obj.length
    if (typeof obj === "object")
        return Object.keys(obj).length
    return 0
}

// user code
let my_list = [];
for (let i = 0; i < 5; i++) {
my_list.push((i * 3))
}
for (let elem of my_list) {
console.log(elem)
}
```

### Niepoprawny kod

Dla `neg_1.py`

```py
a = 3
b = "abc"
break = 3
```

```console
Unexpected token: =
In line 3, column 7

break = 3
      ^

Expected one of the following:
 {'_NEWLINE', 'SEMICOLON'} 

Sorry, couldn't parse .\examples\negative\neg_1.py
```
