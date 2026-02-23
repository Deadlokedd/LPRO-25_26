## Estructura del proyecto

```
modelos_cv/
├── media/
|   ├── raw/                 # Dataset original
|   |   ├── images/          
|   |   └── videos/          
|   └── results/             # Resultados generados
└── src/
    ├── main.py              # Detección + pose por jugador
    ├── config.py            # Configuración de rutas, modelos y dibujo
    ├── utils/
    │   ├── detector.py      # Función de recorte
    │   ├── visualizer.py    # Dibujo de esqueleto y frames globales
    │   └── io_handler.py    # Manejo de directorios y guardado
    └── experiments/
        ├── global_image_pose.py  # Pose global sobre imágenes
        ├── video_objects.py      # Tracking de objetos en vídeo
        └── video_pose.py         # Pose en vídeo

```

## Instalación

```bash
# Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install ultralytics lapx
```

## Uso
Enfoque top-down: detecta jugadores en la imagen, recorta cada uno y aplica estimación de pose individual:

```bash
python3 src/main.py
```

**Salida:**
- `media/results/global_detection/` — Imágenes con bounding boxes de todos los jugadores
- `media/results/crops_pose/matchX/` — Crop de cada jugador con esqueleto dibujado

### Experimentos

```bash
# Pose global sobre todas las imágenes
python3 src/experiments/global_image_pose.py

# Tracking de objetos en vídeo (personas + balón)
python3 src/experiments/video_objects.py

# Estimación de pose en vídeo
python3 src/experiments/video_pose.py
```
