from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    api_service_title: str ="Financial Agentic RAG"
    api_version: str ="0.0.1"
    api_host: str = "0.0.0.0"  #1
    api_port: int = 8080 
    api_workers: int = 4
    environment: str = "development"
    debug: bool = False

    # Ollama and agent 
    ollama_base_url: str = "http://localhost:11434"
    agent_llm_model: str = "qwen2.5:latest"
    agent_temperature: float = 0.1
    agent_max_tokens: int = 4096

    vector_db_type: str
    chromadb_persist_directory: str
    chromadb_collection_name: str

    # Redis
    redis_url: str = "redis://localhost:6379"
    redis_job_ttl: int = 3600

    # RAG
    rag_chunk_size: int
    rag_chunk_overlap: int
    rag_top_k: int = 5
    rag_similarity_threshold: float = 0.7
    rag_embedding_model: str = "nomic-embed-text"

    agent_llm_model: str = "llama3"
    agent_temperature: float = 0.0
    agent_max_tokens: int = 4096
    agent_max_iterations: int = 10

    # ChromaDB (HTTP server)
    chromadb_collection_name: str = "financial_docs"
    chromadb_host: str = "localhost"
    chromadb_port: int = 8000
    

   # Logging
    obs_log_level: str = "INFO"
    obs_log_format: str = "text"

     # Alpha Vantage
    alpha_vantage_api_key: str = ""
    alpha_vantage_source: str = "https://www.alphavantage.co/query?"

    # MCP server
    mcp_host: str = "localhost"
    mcp_port: int = 8089

    model_config = SettingsConfigDict(env_file=".env" , env_file_encoding="utf-8" , extra="ignore")


def get_settings()->Settings:
    return Settings()