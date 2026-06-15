from llama_index.core import SimpleDirectoryReader
from pathlib import Path

SUPPORTED_EXT = [".txt", ".pdf", ".md", ".docx"]

def load_documents(data_dir: str):
    input_dir = Path(data_dir)

    if not input_dir.exists():
        raise ValueError(f"[ERROR] Data directory not found: {data_dir}")

    files = [
        str(f) for f in input_dir.rglob("*")
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXT
    ]

    print(f"[INFO] Found {len(files)} supported files")

    if not files:
        raise ValueError(
            f"[ERROR] No supported files found in {data_dir}\n"
            f"Supported types: {SUPPORTED_EXT}"
        )

    reader = SimpleDirectoryReader(
        input_files=files,
        filename_as_id=True
    )

    documents = reader.load_data()

    return documents