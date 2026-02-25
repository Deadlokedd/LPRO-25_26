from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import cv2
import os
import uvicorn

app = FastAPI()

# Definimos el modelo de entrada
class VideoRequest(BaseModel):
    video_path: str
    time_seconds: float

@app.post("/extract-frame")
async def extract_frame(request: VideoRequest):

    if not os.path.exists(request.video_path):
        raise HTTPException(status_code=404, detail="Video no encontrado")


    cap = cv2.VideoCapture(request.video_path)
    

    fps = cap.get(cv2.CAP_PROP_FPS)
    timestamp_ms = request.time_seconds * 1000
    

    cap.set(cv2.CAP_PROP_POS_MSEC, timestamp_ms)
    
    success, frame = cap.read()
    cap.release()

    if not success:
        raise HTTPException(status_code=400, detail="No se pudo extraer el frame en ese tiempo")


    _, buffer = cv2.imencode(".jpeg", frame)
    

    return Response(content=buffer.tobytes(), media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)