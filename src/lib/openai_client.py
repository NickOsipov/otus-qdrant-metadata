"""Module: openai_client
Description: Клиент OpenAI API для генерации ответа по найденному контексту.
"""

from openai import OpenAI

from config.variables import OPENAI_API_KEY, OPENAI_MODEL

SYSTEM_PROMPT = (
    "Ты помощник магазина Орбита. Отвечай по-русски коротко. "
    "Используй только фрагменты из блока КОНТЕКСТ. "
    "Если ответа в контексте нет, так и скажи. Не выдумывай правила."
)


def build_llm_client() -> OpenAI:
    """Создать клиент OpenAI API."""
    return OpenAI(api_key=OPENAI_API_KEY)


def answer_from_context(question: str, context: str) -> str:
    """Сгенерировать ответ модели только по переданному контексту."""
    user_content = f"КОНТЕКСТ:\n{context}\n\nВОПРОС: {question}"
    completion = build_llm_client().chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
    )
    message = completion.choices[0].message.content
    if message is None:
        return ""
    return message.strip()
