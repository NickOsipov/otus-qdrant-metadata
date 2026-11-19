"""Module: 04_filtered_search
Description: Поиск по сходству с фильтром shop/returns/year.
"""

from config.variables import QUERY_TEXT
from src.lib.filters import shop_returns_current_filter
from lib.qdrant import search_knowledge
from src.utils.formatting import print_hits


def search_with_filter() -> None:
    """Напечатать ближайшие документы среди актуальных правил возврата."""
    print(f"query: {QUERY_TEXT}")
    print_hits(
        "фильтр shop + returns + year >= 2025",
        search_knowledge(QUERY_TEXT, shop_returns_current_filter()),
    )


if __name__ == "__main__":
    search_with_filter()
