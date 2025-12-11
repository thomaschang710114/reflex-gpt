import reflex as rx

from .navbar import navbar
from .footer import footer


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar(),
        rx.fragment(
            *args,
            **kwargs,
        ),
        footer()
    )
