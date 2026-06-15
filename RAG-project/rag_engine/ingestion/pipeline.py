from llama_index.core import VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama

from rag_engine.vectorstore.store import create_index

from .loader import load_documents
from .splitter import split_documents
from .embedder import setup_embedding

def build_index(data_path, embed_model, llm_model):
    print("[INFO] Loading documents...")
    documents = load_documents(data_path)

    print("[INFO] Splitting documents...")
    nodes = split_documents(documents)

    print("[INFO] Setting embedding model...")
    setup_embedding(embed_model)

    print("[INFO] Setting LLM...")
    Settings.llm = Ollama(model=llm_model, request_timeout=360.0)
    print("[INFO] Building vector index...")

    from rag_engine.vectorstore.store import create_index

    index = create_index(nodes)

    return index