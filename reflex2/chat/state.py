# import asyncio
import reflex as rx

from . import ai


class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    # form_data: dict = {}
    did_submit: bool = False
    messages: list[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def append_message(self, message, is_bot: bool = False):
        self.messages.append(
            ChatMessage(
                message=message,
                is_bot=is_bot
            )
        )

    def get_gpt_message(self):
        gpt_message = [
            # { # OPENAI fotmat
            #     "role": "system",
            #     "content": "You are an expert at creating recipes like an elite chef. Respond in markdown"
            # }
        ]
        for chat_message in self.messages:
            role = 'user'
            if chat_message.is_bot:
                role = 'model'
            gpt_message.append(
                # { OPENAI format
                #     'role': role,
                #     'content': chat_message.message
                # }
                {
                    "role": role,
                    "parts": [
                        {
                            "text": chat_message.message
                        }
                    ]
                }
            )
        return gpt_message

    # async def handle_submit(self, form_data: dict):
    #     # self.form_data = form_data
    #     user_message = form_data.get('message')
    #     if user_message:
    #         self.did_submit = True
    #         self.append_message(user_message, is_bot=False)
    #         yield  # 第一次 yield：畫面出現使用者的話
    #         # 準備歷史紀錄
    #         gpt_messages = self.get_gpt_message()  # history records        
    #         bot_response = ai.get_llm_response(gpt_messages)
    #         self.append_message(bot_response, is_bot=True)
    #         self.did_submit = False
    #         yield

    async def handle_submit(self, form_data: dict):
        # self.form_data = form_data
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield  # 第一次 yield：畫面出現使用者的話

            # 2. 準備歷史紀錄
            gpt_messages = self.get_gpt_message()  # history records

            # 3. 先新增一個「空的」機器人訊息 (佔位符)
            self.append_message("", is_bot=True)
            yield  # 第二次 yield：畫面出現一個空的機器人對話框

            # 4. 呼叫 AI 並接收串流
            # ai.get_llm_response 現在是一個產生器 (Generator)
            stream = ai.get_llm_response_stream(gpt_messages)
            for chunk_text in stream:
                # 5. 取出清單中「最後一則訊息」(也就是剛剛那個空的機器人訊息)
                # 將新收到的文字「累加 (+=)」上去
                self.messages[-1].message += chunk_text

                # 6. 每次累加一點點，就 yield 一次，讓前端畫面重繪
                yield rx.scroll_to("chat_bottom")

            self.did_submit = False
            yield
