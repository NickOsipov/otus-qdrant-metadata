"""Module: formatting
Description: Печать выдачи Qdrant и сборка текста контекста для LLM.
"""

from collections.abc import Sequence

from qdrant_client.http.models import ScoredPoint


def print_hits(title: str, hits: Sequence[ScoredPoint]) -> None:
    """Напечатать топ выдачи без сырых векторов."""
    print(title)
    if not hits:
        print("  пусто")
        return
    for index, hit in enumerate(hits, start=1):
        payload = hit.payload or {}
        score = round(float(hit.score), 4)
        print(
            f"  {index}. score={score} id={hit.id} "
            f"[{payload.get('department')}/{payload.get('doc_type')}/{payload.get('year')}] "
            f"{payload.get('title')}"
        )


def format_context(hits: Sequence[ScoredPoint]) -> str:
    """Собрать текст фрагментов для промпта модели."""
    if not hits:
        return "Документы не найдены."
    chunks: list[str] = []
    for hit in hits:
        payload = hit.payload or {}
        title = payload.get("title", "")
        text = payload.get("text", "")
        meta = (
            f"{payload.get('department')}/{payload.get('doc_type')}/"
            f"{payload.get('year')}"
        )
        chunks.append(f"[{meta}] {title}\n{text}")
    return "\n\n".join(chunks)
