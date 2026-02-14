# PCEP Question Bank - Index & Quick Start

## Quick Start Guide

### 1. Die Hauptdatei
```
questions-bank-1000.json (276 KB)
```
Diese JSON-Datei enthält alle 1000 PCEP-Fragen strukturiert in 4 Modulen.

### 2. Dateien in diesem Verzeichnis

| Datei | Größe | Beschreibung |
|-------|-------|-------------|
| **questions-bank-1000.json** | 276 KB | Hauptdatei mit 1000 Fragen |
| **QUESTIONS-BANK-README.md** | 7 KB | Detaillierte Dokumentation |
| **SUMMARY.md** | 6 KB | Zusammenfassung & Übersicht |
| **quiz_tool.py** | 7 KB | Interaktives Quiz-Werkzeug |
| **INDEX.md** | Diese Datei | Navigation & Quick Start |

---

## Schneller Einstieg mit Python

### 1. Fragen laden
```python
import json

with open('questions-bank-1000.json', 'r') as f:
    questions = json.load(f)

print(f"Geladen: {sum(len(q) for q in questions.values())} Fragen")
```

### 2. Eine zufällige Frage
```python
import random

all_questions = [q for qs in questions.values() for q in qs]
question = random.choice(all_questions)

print(f"Frage: {question['prompt']}")
print(f"Code: {question['code']}")
print(f"Optionen: {question['options']}")
print(f"Schwierigkeit: {question['difficulty']}")
```

### 3. Nach Modul filtern
```python
# Nur Module 1 Fragen (Fundamentals)
module1_questions = questions['module1']
print(f"Module 1: {len(module1_questions)} Fragen")

# Nur schwere Fragen
hard_questions = [q for qs in questions.values() for q in qs 
                  if q['difficulty'] == 'hard']
print(f"Schwer: {len(hard_questions)} Fragen")
```

### 4. Quiz-Tool nutzen
```bash
python3 quiz_tool.py
```

---

## Modulübersicht

### Module 1: Fundamentals (250 Fragen)
Grundlagen von Python:
- Variables, Types, Operators
- Literals, Type Conversion
- Input/Output

**Empfohlene Dauer:** 2-3 Tage

### Module 2: Control Flow (290 Fragen)
Kontrollstrukturen:
- if/elif/else
- while, for Loops
- break, continue

**Empfohlene Dauer:** 2-3 Tage

### Module 3: Data Collections (250 Fragen)
Datenstrukturen:
- Strings, Lists
- Tuples, Dictionaries

**Empfohlene Dauer:** 2-3 Tage

### Module 4: Functions & Exceptions (210 Fragen)
Fortgeschrittene Konzepte:
- Funktionen, Lambda
- Exception Handling

**Empfohlene Dauer:** 2 Tage

---

## Frage-Format verstehen

```json
{
  "id": "mo0001",                    // Eindeutige ID
  "prompt": "What is the output?",   // Frage-Text
  "code": "print(5 + 3 * 2)",        // Code zum Analysieren
  "options": [                        // 4 Multiple Choice Optionen
    "11",
    "16",
    "26",
    "Error"
  ],
  "answer": 0,                        // Index der korrekten Antwort
  "hint": "Operator precedence",      // Lernhilfe
  "explanation": "Multiplication...",  // Detaillierte Erklärung
  "difficulty": "easy"                // easy, medium, hard
}
```

---

## Verwendungsbeispiele

### Beispiel 1: Quiz durchführen
```python
def run_quiz(questions, count=10):
    import random
    quiz_questions = random.sample(
        [q for qs in questions.values() for q in qs], 
        count
    )
    
    correct = 0
    for i, q in enumerate(quiz_questions, 1):
        print(f"\n{i}. {q['prompt']}")
        for idx, opt in enumerate(q['options']):
            print(f"   [{idx}] {opt}")
        
        answer = int(input("Deine Antwort: "))
        if answer == q['answer']:
            correct += 1
            print("✓ Richtig!")
        else:
            print(f"✗ Falsch. Richtig: {q['options'][q['answer']]}")
    
    print(f"\nErgebnis: {correct}/{count}")

run_quiz(questions)
```

### Beispiel 2: Statistiken
```python
# Schwierigkeitsverteilung
all_q = [q for qs in questions.values() for q in qs]
for level in ['easy', 'medium', 'hard']:
    count = sum(1 for q in all_q if q['difficulty'] == level)
    print(f"{level}: {count} ({count*100/len(all_q):.1f}%)")

# Pro Modul
for module, qs in questions.items():
    print(f"{module}: {len(qs)} Fragen")
```

### Beispiel 3: Export als CSV
```python
import csv

with open('questions.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Modul', 'Frage', 'Schwierigkeit', 'Antwort'])
    
    for module, qs in questions.items():
        for q in qs:
            writer.writerow([
                q['id'],
                module,
                q['prompt'],
                q['difficulty'],
                q['options'][q['answer']]
            ])
```

---

## Häufige Fragen

### Kann ich die Fragen in meine App integrieren?
Ja! Die JSON-Datei ist vollständig strukturiert und kann überall verwendet werden.

### In welcher Reihenfolge sollte ich lernen?
Module 1 → 2 → 3 → 4

### Wieviel Zeit für alle Fragen?
- Easy: 1-2 Min pro Frage
- Medium: 2-3 Min pro Frage
- Hard: 3-5 Min pro Frage
- **Gesamt: ~50-80 Stunden**

### Gibt es noch weitere Ressourcen?
Siehe QUESTIONS-BANK-README.md für detaillierte Information.

---

## Validierungs-Checkliste

✓ 1000 Fragen total
✓ 4 Module strukturiert
✓ Alle erforderlichen Felder vorhanden
✓ Gültige Answer-Indizes
✓ Exakt 4 Optionen pro Frage
✓ Schwierigkeitsgrade gesetzt
✓ Hints und Explanations enthalten
✓ UTF-8 Encoding
✓ Vollständig getestet

---

## Nächste Schritte

1. **QUESTIONS-BANK-README.md** lesen für detaillierte Information
2. **quiz_tool.py** ausführen für interaktives Lernen
3. **Python-Skripte** schreiben zur Quiz-Integration
4. **Systematisch** durch die Module gehen

---

## Kontakt & Support

**Format:** JSON  
**Größe:** 276 KB  
**Fragen:** 1000  
**Module:** 4  
**Status:** Produktionsreif

---

**Viel Erfolg beim Lernen für die PCEP-Zertifizierung!**

*Erstellt: 14. Februar 2026*  
*Version: 1.0*

