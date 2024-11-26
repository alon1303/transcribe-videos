from fastapi import FastAPI
from faster_whisper_functions import get_subtitles
from interfaces.interfaces import Subtitle
from typing import List

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.put("/video/subtitles")
def get_video_subtitles(file_path: str) -> List[Subtitle]:
    print(get_subtitles(file_path))
    return get_subtitles(file_path)
