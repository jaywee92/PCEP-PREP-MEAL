# PCEP-PREP-MEAL

PCEP-PREP-MEAL is a static training website for PCEP exam preparation.
It includes:

- 4 learning modules (fundamentals, control flow, data collections, functions/exceptions)
- interactive quizzes per module
- a full exam simulation with hints, instant feedback, and explanations
- randomized option order and support for single- and multi-select questions

## Live Site

- [PCEP-PREP-MEAL on GitHub Pages](https://jaywee92.github.io/PCEP-PREP-MEAL/)

## Project Structure

```text
index.html
module1.html
module2.html
module3.html
module4.html
exam-simulation.html
.github/workflows/pages.yml
```

## Local Preview

```bash
python3 -m http.server 8000
```

Then open `http://127.0.0.1:8000/`.

## Deployment

Deployment runs automatically via GitHub Actions on push to `main` using:

- `.github/workflows/pages.yml`

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
