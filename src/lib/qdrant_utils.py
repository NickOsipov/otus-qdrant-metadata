"""Module: qdrant_utils
Description: Подключение к Qdrant и поиск по коллекции.
"""

from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, ScoredPoint

from config.variables import COLLECTION_NAME, QDRANT_URL, SEARCH_LIMIT
from src.lib.embeddings import embed_query


def build_client() -> QdrantClient:
    """Создать клиент локального Qdrant."""
    return QdrantClient(url=QDRANT_URL)


def search_knowledge(
    query_text: str,
    query_filter: Filter | None = None,
    limit: int = SEARCH_LIMIT,
) -> list[ScoredPoint]:
    """Найти ближайшие документы с необязательным фильтром payload."""
    client = build_client()
    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=embed_query(query_text),
        query_filter=query_filter,
        limit=limit,
        with_payload=True,
    )
    return list(response.points)
