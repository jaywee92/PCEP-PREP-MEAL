# PCEP Question Bank - 1000 Questions

## Übersicht

Diese JSON-Datei enthält **1000 PCEP (Certified Entry-Level Python Programmer) relevante Multiple-Choice Fragen**, organisiert nach den 4 Lernmodulen.

### Datei
- **Datei**: `questions-bank-1000.json`
- **Größe**: ~276 KB
- **Format**: JSON mit UTF-8 Encoding
- **Struktur**: 4 Module mit je mehreren Fragen

---

## Modulverteilung

| Modul | Thema | Fragen | Anteil |
|-------|-------|--------|--------|
| **module1** | Fundamentals (Basics, Operatoren, I/O) | 250 | 25% |
| **module2** | Control Flow (if/else, Loops, Break/Continue) | 289 | 28.9% |
| **module3** | Data Collections (Strings, Lists, Dicts, Tuples) | 249 | 24.9% |
| **module4** | Functions & Exceptions (Def, Lambda, Try/Except) | 212 | 21.2% |
| **TOTAL** | | **1000** | **100%** |

---

## Schwierigkeitsverteilung

```
Easy:   513 Fragen (51.3%) - Grundkonzepte verstehen
Medium: 330 Fragen (33.0%) - Anwendungsfähigkeit
Hard:   157 Fragen (15.7%) - Tiefes Verständnis
```

---

## Frage-Format (JSON)

### Struktur einer Frage

```json
{
  "id": "mo0001",
  "prompt": "What is the output?",
  "code": "print(5 + 3 * 2)",
  "options": ["11", "16", "26", "Error"],
  "answer": 0,
  "hint": "Operator precedence",
  "explanation": "Multiplication before addition: 5 + (3 * 2) = 11",
  "difficulty": "easy"
}
```

### Feldbereschreibung

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `id` | String | Eindeutige ID (z.B. "mo0001") |
| `prompt` | String | Frage-Text (oft "What is the output?") |
| `code` | String | Python-Code zum Ausführen/Analysieren |
| `options` | Array[String] | 4 mögliche Antworten (Options) |
| `answer` | Integer | Index der korrekten Antwort (0-3) |
| `hint` | String | Hinweis zur Lösung |
| `explanation` | String | Detaillierte Erklärung der richtigen Antwort |
| `difficulty` | String | "easy", "medium" oder "hard" |

---

## Themen-Coverage

### Module 1: Fundamentals (250 Fragen)

**Unterthemen:**
- Computer Programming Basics (50)
- Python 2 vs 3 (20)
- Literals: int, float, str, bool (40)
- Variables & Naming (30)
- Operators: arithmetic, comparison, logical, bitwise (60)
- Type Conversion (30)
- input()/print() (20)

**Beispiel-Fragen:**
- Operator-Priorität verstehen
- Variable-Typen und Konvertierung
- Literale in verschiedenen Formaten (hex, binary, octal)
- Logical und Bitwise Operatoren
- I/O mit print() und input()

### Module 2: Control Flow (289 Fragen)

**Unterthemen:**
- if/elif/else (70)
- Boolean Logic & Truthiness (50)
- while Loops (40)
- for Loops & range() (60)
- break/continue (30)
- else Clause in Loops (20)
- Nested Loops (20)

**Beispiel-Fragen:**
- Conditional Logic verstehen
- Loop-Kontrolle mit break/continue
- Nested Loop-Ausgaben vorhersagen
- for vs while Loops
- Truthiness-Werte (Falsy/Truthy)

### Module 3: Data Collections (249 Fragen)

**Unterthemen:**
- String Methods & Operations (70)
- String Slicing (30)
- List Methods (70)
- List Slicing & Copying (30)
- Tuples (30)
- Dictionaries (20)

**Beispiel-Fragen:**
- String-Methoden (.upper(), .split(), etc.)
- List-Manipulation (.append(), .insert(), etc.)
- Slicing und Indexing
- Tuple vs List (Immutability)
- Dictionary-Zugriff und Operationen
- Referenzen vs Shallow Copies

### Module 4: Functions & Exceptions (212 Fragen)

**Unterthemen:**
- Function Definition (40)
- Parameters: positional, default, *args, **kwargs (60)
- Return Values (30)
- Lambda (20)
- Scope: local, global, nonlocal (30)
- Exception Handling: try/except/else/finally (30)

**Beispiel-Fragen:**
- Funktionsdefinition und -aufrufe
- Parameter-Verwaltung (*args, **kwargs)
- Return-Werte
- Scope und Variablen-Sichtbarkeit
- Exception-Handling mit try/except/finally
- Lambda-Funktionen und Map/Filter

---

## Fragentypen

Die Fragen verwenden folgende Typen:

1. **Code Output Questions (60%)**
   - "What is the output?" - Vorhersagen der Ausgabe
   - Beispiel: `print(5 + 3 * 2)` → "11"

2. **Conceptual Questions (25%)**
   - "Which statement is correct?"
   - Theo retische Verständnisfragen

3. **Error Detection (10%)**
   - "What error occurs?"
   - Fehler erkennen und identifizieren

4. **Best Practice (5%)**
   - "What is the best approach?"
   - Coding Standards und Best Practices

---

## JSON-Datei Laden (Python)

```python
import json

# Datei laden
with open('questions-bank-1000.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Alle Module durchlaufen
for module_name, questions_list in questions.items():
    print(f"{module_name}: {len(questions_list)} Fragen")

# Spezifische Frage zugreifen
first_question = questions['module1'][0]
print(f"Frage: {first_question['prompt']}")
print(f"Code: {first_question['code']}")
print(f"Optionen: {first_question['options']}")
print(f"Korrekte Antwort: {first_question['options'][first_question['answer']]}")
```

---

## Validierung der Datei

Alle Fragen wurden validiert auf:
- ✓ Korrekte JSON-Struktur
- ✓ Alle erforderlichen Felder vorhanden
- ✓ Answer-Index gültig (0-3)
- ✓ Genau 4 Optionen pro Frage
- ✓ Schwierigkeitsgrade korrekt gesetzt
- ✓ Keine doppelten IDs

---

## Lernpfad

**Empfohlene Reihenfolge:**

1. **Module 1 starten** - Grundlagen verstehen
   - Dauer: 2-3 Tage
   - Fokus: Basics, Typen, Operatoren

2. **Module 2 fortfahren** - Kontrollfluss
   - Dauer: 2-3 Tage
   - Fokus: if/else, Loops, Break/Continue

3. **Module 3 üben** - Datenstrukturen
   - Dauer: 2-3 Tage
   - Fokus: Strings, Listen, Tuples, Dicts

4. **Module 4 abschließen** - Funktionen & Fehlerbehandlung
   - Dauer: 2 Tage
   - Fokus: Funktionen, Lambda, Exceptions

**Gesamtdauer: ~9-11 Tage intensives Lernen**

---

## Tipps zum Lernen

1. **Schwierigkeitsprogression**: Easy → Medium → Hard
2. **Code ausführen**: Alle Code-Beispiele lokal ausführen
3. **Erklärungen lesen**: Nach Beantwortung Erklärung studieren
4. **Hints nutzen**: Bei schwierigen Fragen erst Hint lesen
5. **Fehler analysieren**: Falsche Antworten verstehen, nicht nur merken

---

## Dateistruktur Beispiel

```json
{
  "module1": [
    {
      "id": "mo0001",
      "prompt": "What is the output?",
      "code": "print(5 + 3 * 2)",
      "options": ["11", "16", "26", "Error"],
      "answer": 0,
      "hint": "Operator precedence",
      "explanation": "Multiplication before addition: 5 + (3 * 2) = 11",
      "difficulty": "easy"
    },
    ...
  ],
  "module2": [...],
  "module3": [...],
  "module4": [...]
}
```

---

## Statistik

- **Gesamtfragen**: 1000
- **Module**: 4
- **Schwierigkeitsgrade**: 3 (Easy, Medium, Hard)
- **Fragentypen**: ~4 Haupt-Typen
- **Code-Beispiele**: >400 mit echtem Python-Code
- **JSON-Größe**: ~276 KB

---

## Lizenz & Nutzung

Diese Fragenbank ist für Lernzwecke gedacht.

**Verwendung in Anwendungen:**
```python
# Quiz-App
# LMS-Integration
# Selbsttest-Plattformen
# Lerngruppen-Material
```

---

**Letztes Update**: 14. Februar 2026  
**Version**: 1.0  
**Status**: Vollständig validiert

