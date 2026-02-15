# PCEP-PREP-MEAL

PCEP-PREP-MEAL is an interactive static website for preparing the Python Institute PCEP certification exam.

## What This Project Does

- Provides 4 structured learning modules aligned with core PCEP topics.
- Includes focused practice quizzes for each module.
- Includes an exam simulation mode with timed practice.
- Shows instant answer feedback with explanations.
- Supports hints and mixed question styles, including multi-select questions.

## Learning Modules

1. Module 1: Programming Fundamentals
2. Module 2: Control Flow
3. Module 3: Data Collections
4. Module 4: Functions and Exceptions

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

## Run Locally

```bash
python3 -m http.server 8000
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deployment

This project deploys automatically to GitHub Pages via GitHub Actions on every push to `main`.

Workflow file:
- `.github/workflows/pages.yml`

## Study Workflow Recommendation

1. Start with Module 1 and move sequentially through Module 4.
2. Use module quizzes right after each theory section.
3. Enable hints when learning new topics, then retry without hints.
4. Run exam simulation regularly under time pressure.
5. Review incorrect answers and explanations before the next attempt.

## Live Website

- [PCEP-PREP-MEAL on GitHub Pages](https://jaywee92.github.io/PCEP-PREP-MEAL/)
