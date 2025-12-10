import reflex as rx

config = rx.Config(
    app_name="reflex2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)