"""Module: 06_answer_with_llm
Description: Сравнить ответы OpenAI API на одном запросе с разным контекстом из Qdrant.
"""

from collections.abc import Sequence

from qdrant_client.http.models import ScoredPoint

from config.variables import OPENAI_MODEL, QUERY_TEXT
from src.lib.filters import shop_returns_current_filter
from src.lib.openai_client import answer_from_context
from lib.qdrant_client import search_knowledge
from src.utils.formatting import format_context, print_hits


def print_answer(title: str, hits: Sequence[ScoredPoint]) -> None:
    """Показать найденный контекст и ответ модели OpenAI."""
    print_hits(title, hits)
    print(f"модель: {OPENAI_MODEL}")
    print(answer_from_context(QUERY_TEXT, format_context(hits)))
    print()


def compare_answers() -> None:
    """Сравнить генерацию без фильтра и с фильтром актуальных возвратов."""
    print(f"query: {QUERY_TEXT}")
    print_answer("без фильтра", search_knowledge(QUERY_TEXT))
    print_answer(
        "фильтр shop + returns + year >= 2025",
        search_knowledge(QUERY_TEXT, shop_returns_current_filter()),
    )


if __name__ == "__main__":
    compare_answers()
