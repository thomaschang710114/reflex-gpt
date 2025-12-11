import reflex as rx


def navbar(child, *args, **kwargs) -> rx.Component:
    return rx.heading(
        child, *args, **kwargs
    )
