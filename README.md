# 🎨 VibeBot

VibeBot is a full-stack AI powered app that transforms a color into a unique mood. It gives you a vibe score, a Spotify playlist, a mood emoji, a custom gradient background, a fortune cookie message, and even an AI explanation. It’s like a fortune teller, mood board, and playlist curator all in one.

---

## 🌈 Features

- 🎯 **Color-based Mood Classification** — Pick a color and get a vibe score with a matching mood.
- 🎧 **Spotify Playlist Generator** — Mood-matched playlist suggestions.
- ✨ **Flavor Text & Fortune Cookie** — AI-generated descriptions and advice.
- 🧠 **Mood Explanation** — See how your color's hue, saturation, and brightness affect mood.
- 🎤 **Voice Assistant** — Mood is read aloud using browser speech synthesis.
- 📈 **NumPy-powered Classifier** — Vector math finds the closest mood using RGB + HSL.
- 🎨 **Dynamic Gradients** — The background changes based on your mood.

---

## 🛠️ Tech Stack

| Layer      | Tech                   |
|------------|------------------------|
| Frontend   | React + TypeScript     |
| Backend    | FastAPI                |
| AI Logic   | NumPy + Custom Logic   |
| Styling    | CSS                    |
| Voice      | Browser Web Speech API |
| Hosting    | Localhost (Dev)        |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Node.js + npm
- Python 3.9+
- `pip`, `virtualenv`, or `venv`
- (Optional) Spotify account to test playlists

---

### 📦 Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

This starts the Vite dev server at `http://localhost:5173`

---

### ⚙️ Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

The FastAPI server will run at `http://localhost:8000`

---

## 📂 Project Structure

```
VibeBot/
├── backend/
│   ├── main.py                # FastAPI app
│   ├── vibe_logic.py          # Mood classifier logic with NumPy
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── App.tsx            # Main React component
│   ├── App.css                # Global styles
│   └── index.html
└── README.md
```

---

## 🧠 Mood Classification

The backend maps color vectors (hue, saturation, lightness + RGB values) to predefined mood centroids using NumPy’s `linalg.norm`. The closest match is returned with associated metadata like:

- Emoji
- Gradient
- Playlist
- Flavor text
- Fortune
- Explanation

---

## 🗣 Voice Assistant

When you click **"🔊 Read My Mood"**, your browser will read the current vibe aloud using the [SpeechSynthesis API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis).

---

## 💡 Inspiration



---

## 📜 License

MIT

