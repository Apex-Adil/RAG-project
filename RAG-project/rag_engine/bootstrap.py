from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

from rag_engine.config import EMBED_MODEL, LLM_MODEL
from rag_engine.ingestion.embedder import setup_embedding


def initialize():
    setup_embedding(EMBED_MODEL)

    Settings.llm = Ollama(
        model=LLM_MODEL,
        request_timeout=360.0
    )