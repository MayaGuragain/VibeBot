from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from vibe_logic import calculate_vibe

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ColorRequest(BaseModel):
    color: str

@app.post("/api/vibe")
def get_vibe(data: ColorRequest):
    return calculate_vibe(data.color)
