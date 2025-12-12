from decouple import config
from google import genai
from google.genai import types


def get_client():
    api_key = config('GOOGLE_AI_KEY', cast=str)
    return genai.Client(api_key=api_key)


def get_llm_response(gpt_message):
    # 設定 Config (如果有 System Prompt 就在這裡加入)
    generate_config = types.GenerateContentConfig(
        system_instruction="You are an expert at creating recipes like an elite chef. Respond in markdown"
    )
    client = get_client()
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=gpt_message,
        config=generate_config
    )
    return response.text


def get_llm_response_stream(gpt_message):
    # 設定 Config (如果有 System Prompt 就在這裡加入)
    generate_config = types.GenerateContentConfig(
        system_instruction="You are an expert at creating recipes like an elite chef. Respond in markdown"
    )
    client = get_client()

    # 1. 改用 generate_content_stream
    response = client.models.generate_content_stream(
        model='gemini-2.5-flash',
        contents=gpt_message,
        config=generate_config
    )

    # 2. 使用迴圈讀取串流，收到一點就 yield 一點
    for chunk in response:
        # 有時候 chunk 可能包含 metadata 而沒有文字，所以要檢查
        if chunk.text:
            yield chunk.text
