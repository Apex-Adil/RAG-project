from rag_engine.bootstrap import initialize

initialize()

from rag_engine.vectorstore.retriever import get_retriever
from rag_engine.llm.chain import RAGChain

retriever = get_retriever()
chain = RAGChain(retriever)

while True:
    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = chain.query(question)

    print("\n", answer, "\n")