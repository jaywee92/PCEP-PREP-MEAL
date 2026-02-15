# PCEP-PREP-MEAL - PCEP Question Bank (1000 Fragen)

## Übersicht

Dieses Projekt enthält eine vollständige Fragendatenbank mit **1000 realistischen PCEP-Prüfungsfragen** für **PCEP-PREP-MEAL**, basierend auf dem offiziellen Syllabus.

## Dateistruktur

```
questions-bank-1000.json
├── module1: 250 Fragen (Computer Programming and Python Fundamentals)
├── module2: 289 Fragen (Control Flow)
├── module3: 249 Fragen (Data Collections)
└── module4: 212 Fragen (Functions and Exceptions)
```

## Module & Inhalte

### Module 1: Computer Programming and Python Fundamentals (18% der Prüfung = 250 Fragen)

- **Grundkonzepte der Programmierung**: Variablen, Datentypen, Operatoren
- **Python-Besonderheiten**: Division (int vs float), True Division, Floor Division
- **Type Casting & Conversion**: int(), float(), str(), bool()
- **Literals**: Boolean, Integer, Float, String
- **Operatoren**: Arithmetik, Vergleich, Logisch, Bitweise
- **Operator Precedence**: Exponentiation > Multiplication/Division > Addition/Subtraction
- **Python Keywords & Reserved Words**: Groß-/Kleinschreibung, gültige Bezeichner
- **Built-in Functions**: input(), print(), len(), type(), range()
- **String-Operationen**: Indexing, Slicing, Methoden (upper(), lower(), split(), join(), etc.)

**Schwierigkeitsverhältnis:**
- Easy: 34.8%
- Medium: 54.0%
- Hard: 11.2%

### Module 2: Control Flow (29% der Prüfung = 289 Fragen)

- **Bedingte Anweisungen**: if, elif, else
- **Boolean Logic**: and, or, not
- **Wahrheitswertige Werte**: Falsy (0, '', [], None) und Truthy Werte
- **Schleifen**: while, for, break, continue
- **range() Funktion**: range(n), range(start, stop, step), negative steps
- **Loop else Clause**: Besonderheit der Python-Schleifen
- **Ternary/Conditional Expressions**: value if condition else other_value
- **Nested Loops & Control Flow**

**Schwierigkeitsverhältnis:**
- Easy: 53.4%
- Medium: 38.6%
- Hard: 7.9%

### Module 3: Data Collections (25% der Prüfung = 249 Fragen)

- **Strings**: Indexing, Slicing, Immutability, Methoden
- **Lists**: Creation, Modification, Methods (append, extend, insert, remove, pop, sort, reverse)
- **Tuples**: Immutability, Single-element Tuple (1,), Unpacking
- **Dictionaries**: Keys, Values, Items, Methods (get, keys, values, items, pop, update)
- **Collection Membership**: in operator, not in
- **Copying vs References**: y = x vs y = x[:]
- **Built-in Collection Methods**: len(), sorted(), list comprehensions

**Schwierigkeitsverhältnis:**
- Easy: 46.8%
- Medium: 42.0%
- Hard: 11.2%

### Module 4: Functions and Exceptions (28% der Prüfung = 212 Fragen)

- **Function Definition & Calls**: def, return, parameters, arguments
- **Parameter Types**: Positional, Keyword, Default, *args, **kwargs
- **Function Scope**: Local vs Global, global keyword
- **Lambda Functions**: Anonymous functions for simple operations
- **Built-in Functions**: len(), type(), range(), enumerate(), zip(), min(), max(), sum(), sorted()
- **Exception Handling**: try, except, else, finally
- **Common Exceptions**: ValueError, TypeError, IndexError, KeyError, ZeroDivisionError, NameError, SyntaxError
- **Raising Exceptions**: raise statement

**Schwierigkeitsverhältnis:**
- Easy: 49.5%
- Medium: 43.8%
- Hard: 6.7%

## Fragenformat

Jede Frage hat folgende Struktur:

```json
{
  "id": "m1_001",
  "prompt": "What is the output?",
  "code": "x = 10 // 3\nprint(x)",
  "options": [
    "3",
    "3.33",
    "3.0",
    "Error"
  ],
  "answer": 0,
  "hint": "Floor division returns integer",
  "explanation": "The // operator performs floor division, which returns the integer quotient without the remainder. 10 // 3 = 3.",
  "difficulty": "easy"
}
```

### Fragenfelder

- **id**: Eindeutige Frage-ID (mX_YYY format)
- **prompt**: Die Frage/Anweisung
- **code**: Python-Code zur Analyse (falls zutreffend)
- **options**: 3-4 Antwortmöglichkeiten
- **answer**: Index der richtigen Antwort (0-3)
- **hint**: Kurzer Hinweis (5-10 Wörter)
- **explanation**: Ausführliche Erklärung (2-3 Sätze)
- **difficulty**: easy, medium, oder hard

## Fragentypen (Verteilung)

### Code Output (60%)
**Beispiel:** "What is the output?"
- Zeigt Python-Code
- Fragt nach der Ausgabe
- Testet praktisches Verständnis
- Fokus auf Syntax und Semantik

### Conceptual (25%)
**Beispiel:** "Which statement is correct?"
- Theoretische Fragen
- Konzeptverständnis
- Best Practices
- Python-Besonderheiten

### Error Detection (10%)
**Beispiel:** "What error occurs?"
- Fehlererkennungsfähigkeiten
- Exception Types
- Häufige Fallstricke
- Code Validation

### Best Practice (5%)
**Beispiel:** "What is the best approach?"
- PEP 8 Richtlinien
- Code-Stil
- Pythonic Idioms
- Performance & Lesbarkeit

## Schwierigkeitsgrade

### Easy (40-50%)
- Grundlegende Syntax
- Einfache Operationen
- Direkte Konzeptfragen
- Einzelne Operatoren

### Medium (40-50%)
- Kombinierte Konzepte
- Mehrstufige Operationen
- Operator Precedence
- Nested Structures

### Hard (10-15%)
- Edge Cases
- Tricky Situationen
- Komplexe Interaktionen
- Fallstricke & Stolpersteine

## Exam Traps (eingebaute Prüfungsfallen)

Die Fragen enthalten bewusst Prüfungsfallen für häufige Fehler:

### Module 1
- ✓ Division returns float: `10/2 = 5.0`
- ✓ Floor division mit Negativ: `-7//2 = -4`
- ✓ int() truncates, doesn't round: `int(3.9) = 3`
- ✓ Operator precedence: `-2**2 = -4`
- ✓ String immutability
- ✓ Boolean als Integer: `True == 1`, `False == 0`

### Module 2
- ✓ Loop else clause skips bei break
- ✓ range(n) excludes n
- ✓ Falsy values: 0, '', [], None
- ✓ Ternary expression syntax

### Module 3
- ✓ String immutability: `x[0] = 'H'` → TypeError
- ✓ List references vs copies: `b = a` vs `b = a[:]`
- ✓ sort() returns None
- ✓ sorted() returns new list
- ✓ Tuple single element: `(1,)` nicht `(1)`
- ✓ Dictionary `in` checks keys, not values
- ✓ find() returns -1, index() raises ValueError

### Module 4
- ✓ Mutable default arguments trap
- ✓ append() vs extend()
- ✓ Return ohne Wert: returns None
- ✓ *args creates tuple, **kwargs creates dict
- ✓ finally always executes
- ✓ Function scope: local vs global

## Verwendung

### JSON Laden (Python)

```python
import json

with open('questions-bank-1000.json', 'r') as f:
    data = json.load(f)

# Alle Module
for module_name in data:
    questions = data[module_name]
    print(f"{module_name}: {len(questions)} questions")

# Spezifisches Modul
module1 = data['module1']
for question in module1[:5]:
    print(f"ID: {question['id']}")
    print(f"Code: {question['code']}")
    print(f"Options: {question['options']}")
    print(f"Answer index: {question['answer']}")
```

### Prüfungssimulation

```python
import json
import random

with open('questions-bank-1000.json', 'r') as f:
    data = json.load(f)

# Alle Fragen aus allen Modulen
all_questions = []
for module in data.values():
    all_questions.extend(module)

# Zufällige Prüfung mit 50 Fragen
exam = random.sample(all_questions, 50)
score = 0

for q in exam:
    print(f"\n{q['id']}: {q['prompt']}")
    if 'code' in q and q['code']:
        print(f"Code: {q['code']}")
    for i, opt in enumerate(q['options']):
        print(f"  {i+1}. {opt}")
    
    user_answer = int(input("Your answer (0-3): "))
    if user_answer == q['answer']:
        score += 1
        print("✓ Correct!")
    else:
        print(f"✗ Incorrect. Correct answer: {q['options'][q['answer']]}")
        print(f"Explanation: {q['explanation']}")

print(f"\nFinal Score: {score}/{len(exam)} ({score/len(exam)*100:.1f}%)")
```

## Statistiken

| Metrik | Wert |
|--------|------|
| Gesamtfragen | 1000 |
| Module | 4 |
| Code Output Fragen | ~600 |
| Conceptual Fragen | ~250 |
| Error Detection Fragen | ~100 |
| Best Practice Fragen | ~50 |
| Average Difficulty Easy | 45% |
| Average Difficulty Medium | 45% |
| Average Difficulty Hard | 10% |
| File Size | ~330 KB |

## Fragen-ID Schema

- **m1_XXX**: Module 1 (m1_001 bis m1_250)
- **m2_XXX**: Module 2 (m2_001 bis m2_289)
- **m3_XXX**: Module 3 (m3_001 bis m3_249)
- **m4_XXX**: Module 4 (m4_001 bis m4_212)

## Offizielle PCEP-40-01 Syllabus

Diese Fragendatenbank basiert auf:

- **Prüfung**: Python Institute - Certified Entry-Level Python Programmer (PCEP-40-01)
- **Gültig ab**: 2024
- **Bestehensquote**: 70% (65+ von 70 Punkten)
- **Zeit**: 90 Minuten
- **Fragen**: 40 Fragen

## Best Practices für die Prüfungsvorbereitung

1. **Systematisch durcharbeiten**: Beginne mit Modul 1, arbeite dich durch alle Module
2. **Code ausführen**: Kopiere Code-Beispiele und führe sie lokal aus
3. **Erklärungen lesen**: Verstehe nicht nur das "was", sondern auch das "warum"
4. **Schwierige Fragen wiederholen**: Focus auf hard-level Fragen für Perfektionierung
5. **Timed Practice**: Übe unter Zeitdruck (2 Minuten pro Frage)
6. **Module kombinieren**: Erstelle Mixed-Exams mit Fragen aus allen Modulen

## Tipps zu häufigen Fallstricken

### Division und Floor Division
```python
10 / 3   # 3.333... (float)
10 // 3  # 3 (integer)
-7 // 2  # -4 (rundet ab, nicht zu 0!)
```

### String Immutability
```python
s = "hello"
s[0] = "H"  # TypeError! Strings sind unveränderlich
```

### List vs Copy
```python
a = [1, 2, 3]
b = a        # b referenziert a
a.append(4)  # a und b sind beide [1, 2, 3, 4]

c = a[:]     # c ist eine Kopie
a.append(5)  # a ist [1, 2, 3, 4, 5], c ist [1, 2, 3, 4]
```

### Sort vs Sorted
```python
x = [3, 1, 2]
x.sort()           # x ist nun [1, 2, 3], sort() gibt None zurück
y = sorted([3, 1]) # y ist [1, 3], sorted() gibt neue Liste zurück
```

### Tuple Single Element
```python
x = (1)    # Das ist ein int, nicht ein tuple!
y = (1,)   # Das ist ein tuple mit einem Element
```

### Loop Else
```python
for i in range(5):
    if i == 3:
        break
else:
    print("Completed")  # Diese Zeile wird NICHT ausgeführt wegen break
```

### Mutable Default Arguments
```python
def f(x=[]):        # FALSCH: list wird nur einmal erstellt
    x.append(1)
    return x
f()  # [1]
f()  # [1, 1]  <-- Problem!

def g(x=None):      # RICHTIG
    if x is None:
        x = []
    x.append(1)
    return x
g()  # [1]
g()  # [1]
```

## Kontakt & Support

Diese Fragendatenbank wurde basierend auf:
- Offizielles PCEP-40-01 Syllabus
- Python 3.10+ Standard
- PEP 8 Style Guide
- Häufige Prüfungsfallen und Best Practices

---

**Letzte Aktualisierung**: 2024
**Version**: 1.0
**Status**: Vollständig (1000 Fragen)
