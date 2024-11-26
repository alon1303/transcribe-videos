from faster_whisper import WhisperModel
from interfaces.interfaces import Subtitle
from typing import List

model_size = "large-v3"
model = WhisperModel(model_size, device="cpu", compute_type="int8")


def get_subtitles(file_path: str) -> List[Subtitle]:
    try:            
        segments, info = model.transcribe(file_path, beam_size=5, language="en")
        subtitles: List[Subtitle] = []
        for segment in segments:
            subtitle: Subtitle = Subtitle(                
                id=len(subtitles),
                startTime=segment.start,
                endTime=segment.end,
                startFrame=0,
                endFrame=0,
                text=segment.text,
            )
            subtitles.append(subtitle)
        return subtitles
    except Exception as e:
        print(f"Get Subtitled Error!: {e}")
        
