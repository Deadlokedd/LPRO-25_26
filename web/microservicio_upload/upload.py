from fastapi import FastAPI, File, UploadFile
import shutil
from datetime import datetime
import uvicorn
import os 

app = FastAPI()  # Creamos la instancia de la aplicación FastAPI

# Asegúrate de que exista la carpeta para guardar videos
os.makedirs("videos", exist_ok=True)

@app.post("/upload")  # Endpoint POST en /upload
async def upload_video(file: UploadFile = File(...), camera_id: str = "1"):
    # Genera un nombre de archivo único usando el ID de la cámara y la fecha/hora actual
    filename = f"{camera_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"

    # Abre un archivo nuevo en la carpeta 'videos' y escribe el contenido del archivo subido
    with open(f"videos/{filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # Copia todo el contenido del UploadFile al disco

    # Devuelve un JSON con el nombre del archivo y un estado
    return {"filename": filename, "status": "guardado"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)