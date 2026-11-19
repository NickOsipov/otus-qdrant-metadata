"""Module: config
Description: Константы Qdrant, эмбеддингов и LLM через OpenAI API.
"""

import os

from dotenv import load_dotenv
from qdrant_client.http import models

load_dotenv()

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = "orbit_knowledge"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
VECTOR_SIZE = 384
DISTANCE = models.Distance.COSINE
SEARCH_LIMIT = 3
QUERY_TEXT = "как оформить возврат"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
