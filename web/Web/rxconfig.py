import reflex as rx

config = rx.Config(
    app_name="Web",
    backend_port=9091,
    frontend_port=9090,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
