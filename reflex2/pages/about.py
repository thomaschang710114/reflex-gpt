import reflex as rx

from .. import ui


def about_us_page() -> rx.Component:
    # About Page
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("About", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )
