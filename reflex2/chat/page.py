import reflex as rx

from reflex2 import ui


def chat_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )
