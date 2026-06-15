from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext, VectorStoreIndex
import chromadb
import os

PERSIST_DIR = "vector_db"
COLLECTION_NAME = "rag_collection"


def create_index(nodes):
    print("[DEBUG] Entered create_index")
    print(f"[DEBUG] Nodes received: {len(nodes)}")

    os.makedirs(PERSIST_DIR, exist_ok=True)

    client = chromadb.PersistentClient(path=PERSIST_DIR)

    collection = client.get_or_create_collection(
        COLLECTION_NAME
    )

    print(f"[DEBUG] Collection: {collection.name}")
    print(f"[DEBUG] Count before: {collection.count()}")

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    index = VectorStoreIndex(
        nodes,
        storage_context=storage_context
    )

    print(f"[DEBUG] Count after: {collection.count()}")

    return index


def load_index():
    client = chromadb.PersistentClient(path=PERSIST_DIR)

    collection = client.get_collection(
        COLLECTION_NAME
    )

    print(f"[DEBUG] Collection: {collection.name}")
    print(f"[DEBUG] Stored vectors: {collection.count()}")

    vector_store = ChromaVectorStore(
        chroma_collection=collection
    )

    storage_context = StorageContext.from_defaults(
        vector_store=vector_store
    )

    return VectorStoreIndex.from_vector_store(
        vector_store=vector_store,
        storage_context=storage_context
    )