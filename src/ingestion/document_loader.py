
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.settings import get_settings


def load_document(file_path: str) -> str:
    """Read a UTF-8 text document and return its content."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Document not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")

    return path.read_text(encoding="utf-8")


def split_document(text: str) -> list[str]:
    """Split document text into overlapping chunks using project settings."""

    if not text.strip():
        raise ValueError("Document is empty.")

    settings = get_settings()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.rag_chunk_size,
        chunk_overlap=settings.rag_chunk_overlap,
    )

    return splitter.split_text(text)
