import os

import reflex as rx


class VideoState(rx.State):
    video_actual: str = ""

    @rx.var
    def biblioteca(self) -> dict[str, list[str]]:
        base_path = "assets/videos"
        diccionario = {}
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
                        diccionario[carpeta] = sorted(videos)
        return diccionario

    def seleccionar_video(self, ruta: str):
        self.video_actual = ruta
