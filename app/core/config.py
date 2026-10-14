from functools import lru_cache
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    app_name: str = "Enterprise IT Support Agentic RAG Copilot"
    app_env: str = "development"
    # 100% free: Google AI Studio keys (no card) cover LLM + embeddings.
    # Get them at https://aistudio.google.com/apikey
    # Multiple keys = comma-separated, auto-rotated to dodge rate limits.
    # Example: GOOGLE_API_KEYS=key1,key2,key3
    google_api_key: str = ""
    google_api_keys: str = ""
    gemini_model: str = "gemini-flash-lite-latest"
    embedding_model: str = "models/gemini-embedding-001"
    # Optional 2nd free provider as fallback (https://console.groq.com, no card).
    # Gemini quota sesh hole auto Groq e jabe.
    groq_api_key: str = ""
    groq_model: str = "openai/gpt-oss-20b"
    faiss_index_dir: str = str(BASE_DIR / "data" / "faiss_index")
    top_k: int = 4
    max_retries: int = 1
    admin_api_key: str = "change-me"
    audit_db_path: str = str(BASE_DIR / "data" / "audit.db")
    upload_dir: str = str(BASE_DIR / "uploads")
    sample_kb_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"), extra="ignore")




@lru_cache
def get_settings() -> Settings:
    return Settings()
