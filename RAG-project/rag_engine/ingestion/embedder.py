from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def setup_embedding(model_name: str):
    Settings.embed_model = HuggingFaceEmbedding(model_name=model_name)