from llama_index.core.node_parser import SentenceSplitter

def split_documents(documents, chunk_size=512, chunk_overlap=50):
    splitter = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    nodes = splitter.get_nodes_from_documents(documents)

    print(f"[INFO] Created {len(nodes)} chunks")

    return nodes