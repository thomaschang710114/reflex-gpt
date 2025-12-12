import reflex as rx

from reflex2 import ui

from .state import ChatMessage, ChatState
from .form import chat_form


message_style = dict(
    display="inline-block",
    padding="1em",
    border_radius="8px",
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"]
)


def message_box(chat_message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(chat_message.is_bot, rx.color("mauve", 4), rx.color('blue', 4)),
                color=rx.cond(chat_message.is_bot, rx.color("mauve", 12), rx.color('blue', 12)),
                **message_style,
            ),
            text_align=rx.cond(chat_message.is_bot, "left", "right"),
            margin_top="1em",
        ),
        width="100%",
    )


def chat_page() -> rx.Component:
    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat", size="9"),
            # rx.box(
            #     rx.foreach(ChatState.messages, message_box),
            #     width="100%"
            # ),
            # 使用 scroll_area 包覆訊息列表
            rx.scroll_area(
                rx.vstack(
                    rx.foreach(ChatState.messages, message_box),
                    # 埋入隱形的錨點 (Anchor)
                    rx.box(id="chat_bottom"),
                    width="100%",
                    spacing="4",
                ),
                # 限制高度，內容超過時才會出現捲軸
                # 這裡設為視窗高度的 65%
                h="65vh",
                width="100%",
                scrollbars="vertical",
            ),
            chat_form(),
            margin="3rem auto",
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )
