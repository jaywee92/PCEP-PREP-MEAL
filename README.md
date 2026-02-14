# PCEP-PREP-MEAL

Interactive PCEP preparation website (HTML/CSS/JS) with:
- 4 learning modules
- quiz mode per module
- selectable number of questions
- hints, instant answer reveal, and explanation

## Run locally

Open `index.html` in a browser.

## Publish on GitHub Pages

This repository is already prepared for GitHub Pages deployment via Actions.

1. Create a new repo on GitHub named `PCEP-PREP-MEAL`.
2. Push this project to the repo:

```bash
cd /Users/jochenwahl/Projects/PCEP-PREP-MEAL
git add .
git commit -m "Initial PCEP prep website"
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/PCEP-PREP-MEAL.git
git push -u origin main
```

3. In GitHub, open:
   - `Settings` -> `Pages`
   - Under `Build and deployment`, select `Source: GitHub Actions`

4. Wait for the workflow `Deploy GitHub Pages` to finish.

Your site URL will be:

`https://<YOUR_GITHUB_USERNAME>.github.io/PCEP-PREP-MEAL/`
