import reflex as rx

from .navbar import navbar


def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar('Navbar'),
        *args, **kwargs
    )
