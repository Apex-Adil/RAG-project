from llama_index.core import Settings
class RAGChain:
    def __init__(self, retriever):
        self.retriever = retriever

    def query(self, question):
        nodes = self.retriever.retrieve(question)

        context = "\n\n".join(
            node.text for node in nodes
        )

        prompt = f"""
        You are a friendly AI assistant.

Rules:
1. If the user is greeting you (hi, hello, hey, good morning, etc.), respond naturally.
2. If the user asks who you are, introduce yourself as an AI assistant and nothing else.
3. For questions that require knowledge, Use ONLY the provided context..
4. If the answer is not found in the context, say:
   "I don't know based on the provided documents."
        Context:
        {context}

        Question:
        {question}
        """

        response = Settings.llm.complete(prompt)

        return response.text