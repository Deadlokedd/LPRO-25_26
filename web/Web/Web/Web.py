import reflex as rx
from .state import VideoState
from .components import fila_categoria

estilos_base = {
    "background_color": "#0a0a0a",
    "color": "#e0e0e0",
    "font_family": "system-ui, sans-serif",
}

def index() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.vstack(
                rx.heading("VAR", size="8", color="white"),
                rx.cond(
                    VideoState.video_actual != "",
                    rx.video(
                        src=VideoState.video_actual, 
                        width="850px", 
                        height="auto", 
                        controls=True, 
                        key=VideoState.video_actual
                    ),
                    rx.box(
                        rx.text("Selecciona un video de la biblioteca", color="white", opacity="0.7"),
                        width="850px", height="480px", 
                        background="rgba(0,0,0,0.4)",
                        display="flex", align_items="center", justify_content="center", 
                        border_radius="xl",
                        border="1px solid #3B6840"
                    )
                ),
                padding="2em",
                width="100%",
                align="center",
            ),
            width="100%",
        ),
        rx.container(
            rx.vstack(
                # Ahora iteramos sobre el diccionario de estado directo
                rx.foreach(VideoState.biblioteca, fila_categoria),
                width="100%",
                spacing="6",
            ),
            size="4",
            padding_y="3em",
        ),
        width="100%",
        spacing="0",
        min_height="100vh"
    )

app = rx.App(
    style=estilos_base,
    theme=rx.theme(
        appearance="dark", 
        accent_color="grass",
        radius="medium"
    )
)

# Línea corregida: Se añade el evento on_load para disparar el watchdog
app.add_page(index, on_load=VideoState.setup_watchdog)