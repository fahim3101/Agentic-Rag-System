"""100% free local vectorstore: Gemini embeddings (free API) + FAISS (local file).

No Pinecone, no OpenAI, no server. Index lives in data/faiss_index/.
"""
from pathlib import Path

from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.core.config import get_settings

settings = get_settings()


_embeddings: dict = {}
_vectorstore = None


def get_embeddings():
    """Round-robin key per call — embedding quota o ভাগ হবে।"""
    from app.core.keypool import next_google_key

    key = next_google_key()  # missing hole clear error dey
    if key not in _embeddings:
        _embeddings[key] = GoogleGenerativeAIEmbeddings(
            model=settings.embedding_model,
            google_api_key=key,
        )
    return _embeddings[key]


def _index_path() -> Path:
    return Path(settings.faiss_index_dir)


def get_vectorstore():
    """Load FAISS index from disk. Ingest first via python ingest_sample_kb.py."""
    global _vectorstore
    if _vectorstore is None:
        index_dir = _index_path()
        if not (index_dir / "index.faiss").exists():
            raise RuntimeError(
                f"FAISS index not found at {index_dir}. "
                "Run: python ingest_sample_kb.py"
            )
        _vectorstore = FAISS.load_local(
            str(index_dir), get_embeddings(), allow_dangerous_deserialization=True
        )
    return _vectorstore


def get_retriever():
    return get_vectorstore().as_retriever(search_kwargs={"k": settings.top_k})


def add_documents(chunks):
    """Create the FAISS index on first ingest, else append + save."""
    global _vectorstore
    index_dir = _index_path()
    index_dir.mkdir(parents=True, exist_ok=True)
    if (index_dir / "index.faiss").exists() and _vectorstore is None:
        _vectorstore = FAISS.load_local(
            str(index_dir), get_embeddings(), allow_dangerous_deserialization=True
        )
    if _vectorstore is None:
        _vectorstore = FAISS.from_documents(chunks, get_embeddings())
    else:
        _vectorstore.add_documents(chunks)
    _vectorstore.save_local(str(index_dir))
    return _vectorstore
