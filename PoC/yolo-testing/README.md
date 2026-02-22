# Crear entorno virtual
python3 -m venv venv
# Activar entorno
source venv/bin/activate

# Instalar librerías 
pip install --upgrade pip
pip install ultralytics lapx
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

# Ejecutar modelos
python3 source/detect_objects.py
python3 source/pose_estimation.py

Para ejecutar se necesita tener un archivo llamado "football_match.mp4" en el directorio media
