# 📚 Little Wonder — Children's Storybook

Little Wonder is a beginner-friendly Python web app that lets users create gentle children's stories from a character, theme, age group, setting, and lesson.

## Features

- Friendly Streamlit interface
- Story settings: character, theme, age group, setting, and moral
- Demo story generation that works without an API key
- Original sample storybook cover illustration
- Download the story as Markdown and cover illustration as PNG
- Ready to extend with a real AI text/image API

## Preview

The app includes an original sample illustration at `assets/storybook_cover.png`.

## Run locally

1. Install Python 3.10+ and VS Code.
2. Extract this repository and open its folder in VS Code.
3. Open **Terminal → New Terminal** and run:

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

If PowerShell does not allow environment activation, open Command Prompt and use:

```bat
.venv\Scripts\activate.bat
```

Streamlit should open the app in your browser at `http://localhost:8501`.

## Upload to GitHub without using terminal

1. Sign in to GitHub and choose **New repository**.
2. Name it `little-wonder-ai-storybook`.
3. Choose Public (if you're comfortable sharing your code) and create the repository.
4. Click **Add file → Upload files**.
5. Upload `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and the `assets` folder with its image.
6. Click **Commit changes**.

## Future AI integration

The current project intentionally runs without paid services. Demo stories use a simple template, and the included image is a sample cover rather than a generated illustration for every scene.

To add real AI-written stories and scene-specific illustrations, integrate an AI provider API. API keys should be stored in environment variables or a hosting provider's secrets settings and **never committed to GitHub**. API usage may cost money.

## Safety note

Review all generated stories and illustrations for age-appropriateness before sharing with children.
