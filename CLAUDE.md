# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PCEP-PREP-MEAL is a **static HTML/CSS/JS** learning platform for the Python Institute PCEP certification. No build step, no framework, no backend — all content is embedded directly in HTML files.

Live site: https://jaywee92.github.io/PCEP-PREP-MEAL/

## Running Locally

```bash
python3 -m http.server 8000
# Open http://127.0.0.1:8000/
```

No install step required. All files are standalone HTML.

## Deployment

Pushing to `main` triggers `.github/workflows/pages.yml`, which copies all HTML files directly to GitHub Pages. No build step — changes go live immediately after push.

## Architecture

### File Structure

| File | Role |
|---|---|
| `index.html` | Landing page with module navigation cards |
| `module1–4.html` | Learning modules (Theory, Cheatsheet, Mistakes, Flashcards, Quiz tabs) |
| `exam-simulation.html` | Full 30-question timed exam (~442KB, contains all question data) |

### Key Patterns

**All data is embedded** — no fetch(), no external APIs. Questions live in `<script>` tags as JS arrays/objects inside each HTML file.

**Module pages** share a common tab structure: Theory → Cheatsheet → Common Mistakes → Pitfalls → Flashcards → Quiz. Tabs are lazy-initialized on first click.

**Exam simulation** uses a single `state` object for all session state (current question, timer, answers, hints used, utility panel). Questions are shuffled and options are randomized on each session start via `prepareQuestionForSession()`.

**No CSS framework** — custom design system using CSS Custom Properties (dark theme, defined in `:root`). Font stack: Space Grotesk + IBM Plex Mono via Google Fonts.

### Question Data Format

Module quiz questions:
```javascript
{ q: "...", options: ["A","B","C","D"], correct: 0, explanation: "..." }
```

Exam bank questions (in `exam-simulation.html`, `QUESTIONS_BANK` object):
```javascript
{
  id: "m1_251", module: 1,
  prompt: "...", code: "...",        // code is optional
  options: ["...","...","...","..."],
  answer: 2,                         // primary correct index
  answers: [2],                      // array (supports multi-select: [1,3])
  correct_answer: "C",
  hint: "...", explanation: "...",
  difficulty: "easy|medium|hard", source: "..."
}
```

Multi-select questions use `answers: [1, 3]` (multiple indices). Options are shuffled per session and answer indices remapped accordingly.

### Flashcard Format

```javascript
{ q: "Question text", a: "Answer text" }
```

### CSS Design System Variables

Core variables in `:root`:
- `--bg`, `--surface`, `--border`, `--text`, `--muted`
- `--ok` (success green), `--bad` (error red), `--warn` (warning orange)
- `--m1` through `--m5` for per-module accent colors
- `--code-bg` for code blocks

### Navigation

File-based relative links only (`href="module1.html"`, `href="index.html"`). No SPA routing.

## Content Scope

| Module | Topic | PCEP Exam Weight |
|---|---|---|
| Module 1 | Fundamentals, syntax, types, I/O | 18% |
| Module 2 | Control flow, loops, boolean logic | 29% |
| Module 3 | Strings, lists, tuples, dicts | 25% |
| Module 4 | Functions, scope, exceptions | 28% |

## What to Watch Out For

- `exam-simulation.html` is ~442KB — edits to the question bank here are high-impact.
- Option shuffling is applied at session start; always store correct answers as **indices into the original unshuffled array**, not the display position.
- There is no localStorage persistence — quiz state resets on page reload. Any persistence feature must be added explicitly.
- All 6 HTML files duplicate the full CSS block. Style changes that should apply everywhere must be applied to each file.
