import reflex as rx

config = rx.Config(
    app_name="Web",
    backend_port=9095,
    frontend_port=9094,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
