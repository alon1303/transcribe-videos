from pydantic import BaseModel
class Subtitle(BaseModel):
    id:int
    startTime:float
    endTime:float
    startFrame:int
    endFrame:int
    text:str