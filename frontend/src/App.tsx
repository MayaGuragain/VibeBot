import { useState, useEffect } from 'react'
import axios from 'axios'
import './App.css'

interface VibeResult {
  color: string
  vibe_score: number
  mood: string
  playlist: string
  emoji: string
  gradient: string
  fortune: string
  flavor_text: string
  explanation: string
}

function App() {
  const [color, setColor] = useState('#ff8800')
  const [result, setResult] = useState<VibeResult | null>(null)
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    speechSynthesis.getVoices()
    if (speechSynthesis.onvoiceschanged !== undefined) {
      speechSynthesis.onvoiceschanged = () => {
        speechSynthesis.getVoices()
      }
    }
  }, [])

  const getVibe = async () => {
    setLoading(true)
    try {
      const response = await axios.post('http://localhost:8000/api/vibe', { color })
      setResult(response.data)
    } catch (error) {
      console.error('Error fetching vibe:', error)
    }
    setLoading(false)
  }

  const speakMood = () => {
    if (!result) return

    const moodText = `Your vibe is ${result.mood}. Score ${result.vibe_score}. ${result.flavor_text}. Fortune: ${result.fortune}`
    const utterance = new SpeechSynthesisUtterance(moodText)
    utterance.lang = 'en-US'

    speechSynthesis.cancel()

    const speak = () => {
      const voices = speechSynthesis.getVoices()
      if (voices.length > 0) {
        const selectedVoice = voices.find(v => v.lang === 'en-US') || voices[0]
        utterance.voice = selectedVoice
        speechSynthesis.speak(utterance)
      } else {
        setTimeout(speak, 100)
      }
    }

    speak()
  }

  return (
    <div
      className="container"
      style={{ background: result?.gradient || '#f0f0f0' }}
    >
      <h1 className="title">🎨 Color Vibes</h1>

      <input
        type="color"
        value={color}
        onChange={(e) => setColor(e.target.value)}
        className="color-input"
        aria-label="Pick a color"
      />

      <button
        onClick={getVibe}
        disabled={loading}
        className="button"
      >
        {loading ? 'Vibing...' : 'Get Mood'}
      </button>

      {result && (
        <div className="result-card">
          <h2 className="result-title">
            {result.emoji} {result.mood.charAt(0).toUpperCase() + result.mood.slice(1)}
          </h2>

          <p>
            <strong>Score:</strong> {result.vibe_score}
          </p>

          <p>
            <strong>Playlist:</strong>{' '}
            <a href={result.playlist} target="_blank" rel="noreferrer">
              Open on Spotify
            </a>
          </p>

          <p className="flavor-text">
            <strong>AI Vibe:</strong> {result.flavor_text}
          </p>

          <p>
            <strong>🧧 Fortune:</strong> {result.fortune}
          </p>

          <p className="explanation">
            <strong>🧠 Why this mood?</strong> {result.explanation}
          </p>

          <button
            onClick={speakMood}
            className="read-mood-button"
          >
            🔊 Read My Mood
          </button>
        </div>
      )}
    </div>
  )
}

export default App
