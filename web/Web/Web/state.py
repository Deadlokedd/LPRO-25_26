import reflex as rx
import os
import asyncio
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class VideoHandler(FileSystemEventHandler):
    def __init__(self, state_manager, loop):
        self.state_manager = state_manager
        self.loop = loop

    def on_any_event(self, event):
        if event.is_directory or event.src_path.endswith((".mp4", ".webm", ".mov")):
            # Lanzamos la tarea de actualización de forma segura
            self.loop.call_soon_threadsafe(
                lambda: asyncio.create_task(self.state_manager.actualizar_biblioteca())
            )

class VideoState(rx.State):
    biblioteca: dict[str, list[str]] = {}
    video_actual: str = ""

    async def actualizar_biblioteca(self):
        """Escanea el directorio y actualiza el estado de forma segura."""
        base_path = "assets/videos"
        nuevo_diccionario = {}
        
        if os.path.exists(base_path):
            for carpeta in sorted(os.listdir(base_path)):
                ruta_carpeta = os.path.join(base_path, carpeta)
                if os.path.isdir(ruta_carpeta):
                    videos = [
                        f"videos/{carpeta}/{f}" 
                        for f in os.listdir(ruta_carpeta) 
                        if f.endswith((".mp4", ".webm", ".mov"))
                    ]
                    if videos:
                        nuevo_diccionario[carpeta] = sorted(videos)
        
        # EL CAMBIO CLAVE: Usar 'async with self' para poder modificar el estado
        async with self:
            self.biblioteca = nuevo_diccionario

    @rx.event(background=True)
    async def setup_watchdog(self):
        """Inicia el observador de archivos al cargar la página."""
        # Cargamos la biblioteca inicial
        await self.actualizar_biblioteca()

        loop = asyncio.get_running_loop()
        handler = VideoHandler(self, loop)
        observer = Observer()
        
        # Asegúrate de que la carpeta 'assets/videos' existe realmente
        if not os.path.exists("assets/videos"):
            os.makedirs("assets/videos", exist_ok=True)
            
        observer.schedule(handler, path="assets/videos", recursive=True)
        observer.start()

        try:
            while True:
                await asyncio.sleep(1)
        finally:
            observer.stop()
            observer.join()

    def seleccionar_video(self, ruta: str):
        self.video_actual = ruta