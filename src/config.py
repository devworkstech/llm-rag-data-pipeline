import os
from pydantic import BaseModel

class PipelineSettings(BaseModel):
    chunk_size: int = 512
    chunk_overlap: int = 50
    vector_dim: int = 384
    top_k: int = 5
    collection_name: str = "enterprise_knowledge_base"
    pinecone_environment: str = os.getenv("PINECONE_ENV", "us-east-1-aws")

settings = PipelineSettings()
