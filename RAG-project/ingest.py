from rag_engine.bootstrap import initialize
from rag_engine.ingestion.pipeline import build_index
from rag_engine.config import DATA_PATH, EMBED_MODEL, LLM_MODEL

initialize()

print("[INFO] Starting ingestion...")

build_index(
    DATA_PATH,
    EMBED_MODEL,
    LLM_MODEL
)

print("[INFO] Ingestion complete.")