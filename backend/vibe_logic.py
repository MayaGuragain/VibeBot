import numpy as np
import random

mood_centroids = {
    "fiery":       [0.9, 5,   90, 60, 1.0, 0.3, 0.3],
    "cozy":        [0.7, 30,  60, 40, 0.9, 0.6, 0.3],
    "zesty":       [0.85, 45, 85, 65, 1.0, 0.9, 0.2],
    "hopeful":     [0.8, 70,  70, 75, 0.9, 1.0, 0.5],
    "chill":       [0.6, 120, 45, 60, 0.5, 1.0, 0.7],
    "serene":      [0.55, 180, 40, 80, 0.3, 0.8, 1.0],
    "dreamy":      [0.75, 250, 40, 70, 0.6, 0.4, 1.0],
    "electric":    [0.95, 290, 100, 70, 0.8, 0.4, 1.0],
    "creative":    [0.8, 315, 80, 75, 1.0, 0.4, 1.0],
    "brooding":    [0.4, 220, 30, 25, 0.2, 0.2, 0.4],
    "peaceful":    [0.6, 90,  40, 65, 0.6, 1.0, 0.6],
    "mystical":    [0.65, 270, 50, 55, 0.5, 0.3, 0.7],
    "radiant":     [0.85, 50,  95, 80, 1.0, 0.8, 0.3],
    "playful":     [0.75, 100, 80, 75, 0.9, 1.0, 0.4],
    "bold":        [0.9, 10,  100, 70, 1.0, 0.2, 0.2],
    "melancholy":  [0.4, 200, 30, 30, 0.3, 0.3, 0.5],
    "undefined":   [0.5, 180, 50, 50, 0.5, 0.5, 0.5]
}

mood_data = {
    "fiery": {
        "emoji": "🔥",
        "gradient": "linear-gradient(to right, #ff416c, #ff4b2b)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn",
            "https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO"
        ],
        "flavor": [
            "You’re unstoppable today.",
            "The world can't handle your heat.",
            "Your energy burns bright and fierce."
        ],
        "fortune": "Go all in, fire favors the bold."
    },
    "cozy": {
        "emoji": "🛋️",
        "gradient": "linear-gradient(to right, #ffecd2, #fcb69f)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVqfgj8NZEpS",
            "https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv"
        ],
        "flavor": [
            "Wrapped in warmth and comfort.",
            "A perfect day for blankets and calm.",
            "Soft vibes and sweet relaxation."
        ],
        "fortune": "Slow down, comfort is calling."
    },
    "zesty": {
        "emoji": "🍊",
        "gradient": "linear-gradient(to right, #f7971e, #ffd200)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DXaXB8fQg7xif",
            "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"
        ],
        "flavor": [
            "Fresh vibes with a citrus kick.",
            "Energized and ready to zest.",
            "A splash of zest to brighten your day."
        ],
        "fortune": "Seize the zest in every moment."
    },
    "hopeful": {
        "emoji": "🌅",
        "gradient": "linear-gradient(to right, #fceabb, #f8b500)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU",
            "https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7"
        ],
        "flavor": [
            "Bright horizons ahead.",
            "Open heart and open skies.",
            "The future looks bright and promising."
        ],
        "fortune": "New beginnings are near."
    },
    "chill": {
        "emoji": "🧊",
        "gradient": "linear-gradient(to right, #83a4d4, #b6fbff)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DWZqd5JICZI0u",
            "https://open.spotify.com/playlist/37i9dQZF1DX889U0CL85jj"
        ],
        "flavor": [
            "Low-key legend vibes.",
            "Cool breeze, calm energy.",
            "Relax, breathe, and let it flow."
        ],
        "fortune": "Silence says more than words today."
    },
    "serene": {
        "emoji": "🌿",
        "gradient": "linear-gradient(to right, #a8edea, #fed6e3)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx",
            "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY"
        ],
        "flavor": [
            "Peace flows gently.",
            "Balance and tranquility surround you.",
            "Calm waters run deep."
        ],
        "fortune": "Find calm in every breath."
    },
    "dreamy": {
        "emoji": "🌙",
        "gradient": "linear-gradient(to right, #8e2de2, #4a00e0)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO",
            "https://open.spotify.com/playlist/37i9dQZF1DXa1f2Uy2T5Wu"
        ],
        "flavor": [
            "Soft skies and open minds.",
            "Your mind is floating in lavender light.",
            "Lost in a reverie of colors and sounds."
        ],
        "fortune": "Keep chasing the idea you had last night."
    },
    "electric": {
        "emoji": "⚡",
        "gradient": "linear-gradient(to right, #4e54c8, #8f94fb)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX1rVvRgjX59F",
            "https://open.spotify.com/playlist/37i9dQZF1DX9F9XzIMb5jT"
        ],
        "flavor": [
            "Buzzing with excitement.",
            "Energy that can’t be contained.",
            "Sparkling with electric vibes."
        ],
        "fortune": "Charge forward with confidence."
    },
    "creative": {
        "emoji": "🎨",
        "gradient": "linear-gradient(to right, #f7971e, #ffd200)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX8uXCJ0dZF8B",
            "https://open.spotify.com/playlist/37i9dQZF1DX9sIqqvKsjG8"
        ],
        "flavor": [
            "Ideas flowing freely.",
            "Your creativity lights the way.",
            "Crafting wonders from colors and sounds."
        ],
        "fortune": "Let inspiration guide your day."
    },
    "brooding": {
        "emoji": "🌑",
        "gradient": "linear-gradient(to right, #434343, #000000)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"
        ],
        "flavor": [
            "Deep thoughts and quiet moments.",
            "Reflective and mysterious.",
            "A shadowed space for introspection."
        ],
        "fortune": "Sometimes shadows bring clarity."
    },
    "peaceful": {
        "emoji": "☁️",
        "gradient": "linear-gradient(to right, #e0eafc, #cfdef3)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx",
            "https://open.spotify.com/playlist/37i9dQZF1DXcF6B6QPhFDv"
        ],
        "flavor": [
            "Calm and collected.",
            "A gentle breeze through your day.",
            "Quiet moments to reset and recharge."
        ],
        "fortune": "Peace begins within."
    },
    "mystical": {
        "emoji": "🔮",
        "gradient": "linear-gradient(to right, #bdc3c7, #2c3e50)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX9sIqqvKsjG8",
            "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU"
        ],
        "flavor": [
            "Enchanted and mysterious.",
            "Inviting curiosity and wonder.",
            "A veil of magic surrounds you."
        ],
        "fortune": "Magic is real if you believe."
    },
    "radiant": {
        "emoji": "☀️",
        "gradient": "linear-gradient(to right, #fceabb, #f8b500)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU",
            "https://open.spotify.com/playlist/37i9dQZF1DX889U0CL85jj"
        ],
        "flavor": [
            "Bright and shining.",
            "Positive warmth fills your space.",
            "Glowing with natural brilliance."
        ],
        "fortune": "Shine your light brightly today."
    },
    "playful": {
        "emoji": "🤸‍♂️",
        "gradient": "linear-gradient(to right, #89f7fe, #66a6ff)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX5trt9i14X7j",
            "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"
        ],
        "flavor": [
            "Joyful and light-hearted.",
            "Fun is just around the corner.",
            "Embrace the delight of the moment."
        ],
        "fortune": "Let laughter lead the way."
    },
    "bold": {
        "emoji": "🦁",
        "gradient": "linear-gradient(to right, #ff512f, #dd2476)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP",
            "https://open.spotify.com/playlist/37i9dQZF1DX0BcQWzuB7ZO"
        ],
        "flavor": [
            "Courageous and strong.",
            "Ready to take on any challenge.",
            "Fearless spirit in full force."
        ],
        "fortune": "Bold moves bring great rewards."
    },
    "melancholy": {
        "emoji": "💧",
        "gradient": "linear-gradient(to right, #485563, #29323c)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
            "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
        ],
        "flavor": [
            "Thoughtful with a bittersweet edge.",
            "Reflecting on deeper feelings.",
            "A soft sadness with beauty in it."
        ],
        "fortune": "Even rain nourishes the soul."
    },
    "undefined": {
        "emoji": "❓",
        "gradient": "linear-gradient(to right, #bdc3c7, #2c3e50)",
        "playlists": [
            "https://open.spotify.com/playlist/37i9dQZF1DX9sIqqvKsjG8",
            "https://open.spotify.com/playlist/37i9dQZF1DX0UrRvztWcAU"
        ],
        "flavor": [
            "You’re a mystery in motion.",
            "Undefined but unforgettable.",
            "A unique vibe all your own."
        ],
        "fortune": "Sometimes, not knowing is the power."
    }
}

def hex_to_rgb(hex_color: str):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return r, g, b

def rgb_to_hsl(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    max_c, min_c = max(r, g, b), min(r, g, b)
    l = (max_c + min_c) / 2
    if max_c == min_c:
        return 0, 0, int(l * 100)
    d = max_c - min_c
    s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)
    if max_c == r:
        h = ((g - b) / d + (6 if g < b else 0)) % 6
    elif max_c == g:
        h = ((b - r) / d + 2)
    else:
        h = ((r - g) / d + 4)
    return int(h * 60), int(s * 100), int(l * 100)

def calculate_vibe(hex_color: str):
    r, g, b = hex_to_rgb(hex_color)
    hue, sat, light = rgb_to_hsl(r, g, b)
    vibe_score = round((sat + light) / 200, 2)

    rgb_vector = np.array([
        vibe_score,
        hue,
        sat,
        light,
        r / 255,
        g / 255,
        b / 255
    ])

    min_dist = float('inf')
    best_mood = "undefined"

    for mood, centroid in mood_centroids.items():
        centroid_vec = np.array(centroid)
        dist = np.linalg.norm(rgb_vector - centroid_vec)
        if dist < min_dist:
            min_dist = dist
            best_mood = mood

    mood_info = mood_data.get(best_mood, mood_data["undefined"])

    mood_descriptions = {
        "fiery": "full of passion and unstoppable energy that lights up your surroundings",
        "cozy": "warm, comforting, and wrapped in a gentle embrace of calm",
        "zesty": "fresh, lively, and bursting with vibrant energy",
        "hopeful": "optimistic and looking toward bright new beginnings",
        "chill": "relaxed and calm with a cool, effortless vibe",
        "serene": "peaceful and balanced, like a quiet still lake",
        "dreamy": "soft, imaginative, and floating gently through thoughts",
        "electric": "charged with intensity and buzzing with excitement",
        "creative": "inventive and expressive, painting your world with ideas",
        "brooding": "deep and reflective, filled with thoughtful shadows",
        "peaceful": "calm and harmonious, bringing comfort and ease",
        "mystical": "enchanted and mysterious, inviting curiosity and wonder",
        "radiant": "bright and shining with positive warmth",
        "playful": "light-hearted and joyful, full of fun and laughter",
        "bold": "courageous and unapologetic, ready to take on anything",
        "melancholy": "wistful and thoughtful, with a bittersweet edge",
        "undefined": "unique and mysterious, not fitting into any one category"
    }

    mood_desc = mood_descriptions.get(best_mood, "unique and intriguing")

    explanation = (
        f"This color has a hue of {hue} degrees, saturation of {sat} percent, "
        f"and lightness of {light} percent. Its vibe score is {vibe_score}. "
        f"This places it closest to the '{best_mood}' mood category, which is {mood_desc}."
    )

    return {
        "color": hex_color,
        "vibe_score": vibe_score,
        "mood": best_mood,
        "emoji": mood_info["emoji"],
        "gradient": mood_info["gradient"],
        "playlist": random.choice(mood_info["playlists"]),
        "flavor_text": random.choice(mood_info["flavor"]),
        "fortune": mood_info["fortune"],
        "explanation": explanation
    }
