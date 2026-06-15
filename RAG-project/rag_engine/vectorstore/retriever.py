from rag_engine.vectorstore.store import load_index


def get_retriever():

    index = load_index()

    return index.as_retriever(
        similarity_top_k=4
    )