"""Module: embeddings
Description: Кодирование документов и запросов моделью paraphrase-multilingual-MiniLM-L12-v2.
"""

from fastembed import TextEmbedding

from config.variables import EMBEDDING_MODEL

_MODEL: TextEmbedding | None = None


def get_model() -> TextEmbedding:
    """Вернуть общую модель эмбеддингов для скриптов занятия."""
    global _MODEL
    if _MODEL is None:
        _MODEL = TextEmbedding(model_name=EMBEDDING_MODEL)
    return _MODEL


def embed_passages(texts: list[str]) -> list[list[float]]:
    """Построить векторы документов. Префиксы не нужны, модель их не использует."""
    return [vector.tolist() for vector in get_model().embed(texts)]


def embed_query(text: str) -> list[float]:
    """Построить вектор поискового запроса тем же способом, что и документы."""
    vectors = list(get_model().embed([text]))
    return vectors[0].tolist()
