import reflex as rx
from .state import VideoState

def video_card(ruta_video: rx.Var[str]):
    # Extraemos el nombre para mostrarlo en la tarjeta
    nombre_archivo = ruta_video.split("/")[-1]
    
    return rx.card(
        rx.vstack(
            rx.icon("play", size=40, color="#3B6840"),
            rx.text(nombre_archivo, size="1", weight="bold", color="#e0e0e0", truncate=True),
            align="center",
            spacing="2",
        ),
        on_click=VideoState.seleccionar_video(ruta_video),
        cursor="pointer",
        width="160px",
        background_color="#1a1a1a",
        border="1px solid transparent",
        _hover={
            "transform": "scale(1.05)", 
            "transition": "0.3s ease",
            "border": "1px solid #3B6840",
            "box_shadow": "0px 4px 15px rgba(59, 104, 64, 0.4)"
        },
    )

def fila_categoria(item):
    # item[0] es la clave (nombre carpeta), item[1] es el valor (lista videos)
    nombre_cat = item[0]
    lista_vids = item[1]
    
    return rx.vstack(
        rx.heading(nombre_cat, size="5", margin_left="1em", color="#3B6840"),
        rx.scroll_area(
            rx.hstack(
                rx.foreach(lista_vids, video_card),
                spacing="4",
                padding="1em",
            ),
            scrollbars="horizontal",
            style={"width": "100%"},
        ),
        width="100%",
        align_items="start",
    )