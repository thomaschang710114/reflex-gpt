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
