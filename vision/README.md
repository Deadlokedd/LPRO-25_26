# Vision

![Image](https://github.com/user-attachments/assets/f6760e55-6f45-42f5-b4c9-e7a09e65b030)

## Estructura

```
vision/
├── pyproject.toml                     # Paquete instalable con pip
├── scripts/
│   └── setup.sh                       # Creación de venv + instalación
├── src/                               # Paquete Python principal
│   ├── __init__.py
│   ├── config.py                      # Parámetros de modelo de pose
│   ├── paths.py                       # Rutas I/O (solo para CLI)
│   ├── pipeline.py                    # Lógica principal
│   ├── main.py                        # Script CLI
│   └── utils/
│       └── io_handler.py              # I/O de archivos y directorios
└── experiments/                       # Scripts de pruebas
    └── gpu_info.py
```

## Instalación

### Requisitos previos

- Python ≥ 3.10
- GPU con CUDA

### Crear entorno e instalar dependencias

```bash
cd vision
bash scripts/setup.sh # Si el usuario (Windows/Linux) no tiene GPU, añadir flag --cpu
source .venv/bin/activate # Linux / macOS
.\.venv\Scripts\Activate.ps1 # Windows
```

El script `setup.sh` crea el entorno virtual e instala el paquete con sus dependencias.

## Uso

### CLI

```bash
python -m src.main
```

Las imágenes de entrada se leen de `data/raw/images/` (formato `match*_0.jpg`)
y los resultados se guardan en `data/results/`.
