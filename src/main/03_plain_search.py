"""Module: 03_plain_search
Description: Поиск по сходству без фильтра по метаданным.
"""

from config.variables import QUERY_TEXT
from src.lib.qdrant_utils import search_knowledge
from src.utils.formatting import print_hits


def search_without_filter() -> None:
    """Напечатать ближайшие документы только по вектору запроса."""
    print(f"query: {QUERY_TEXT}")
    print_hits("без фильтра", search_knowledge(QUERY_TEXT))


if __name__ == "__main__":
    search_without_filter()
