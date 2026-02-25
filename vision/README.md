# Vision

Pipeline de estimación de pose en el frame global, basado en MMPose.

<!-- ## Estructura

```
vision/
├── pyproject.toml                     # Paquete instalable con pip
├── scripts/
│   └── setup.sh                       # Creación de venv + instalación
├── models/                            # Pesos de modelos (en .gitignore)
│   └── RealESRGAN_x2plus.pth
├── src/                               # Paquete Python principal
│   ├── __init__.py
│   ├── config.py                      # Parámetros de modelo de pose y Super-Resolution
│   ├── paths.py                       # Rutas I/O (solo para CLI)
│   ├── pipeline.py                    # Lógica principal usando MMPose
│   ├── main.py                        # Script CLI
│   └── utils/
│       ├── super_resolution.py        # Super-resolución con Real-ESRGAN
│       └── io_handler.py              # I/O de archivos y directorios
└── experiments/                       # Scripts de pruebas
    ├── img_pose_estimation.py
    ├── video_player_tracking.py
    ├── video_pose_estimation.py
    └── gpu_info.py
``` -->

## Instalación

### Requisitos previos

- Python ≥ 3.10
- GPU con CUDA

### Crear entorno e instalar dependencias

```bash
cd vision
bash scripts/setup.sh # Si el usuario (Windows/Linux) no tiene GPU, añadir flag --cpu
source .venv/bin/activate
```

El script `setup.sh` crea el entorno virtual e instala el paquete con sus dependencias.

## Uso

### CLI

```bash
python -m src.main
```

Las imágenes de entrada se leen de `data/raw/images/` (formato `match*_0.jpg`)
y los resultados se guardan en `data/results/`.

### Experimentos

```bash
python -m experiments.img_pose_estimation
python -m experiments.video_player_tracking
python -m experiments.video_pose_estimation
```
