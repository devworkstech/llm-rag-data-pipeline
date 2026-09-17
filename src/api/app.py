"""FastAPI Retrieval & Query Service."""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
from src.retrieval.hybrid_search import HybridSearchEngine

app = FastAPI(title="Enterprise RAG Query Service", version="1.0.0")

# Preload sample memory index
mock_index = [
    {"content": "Enterprise Lakehouse standardizes Bronze, Silver, Gold medallion architecture.", "metadata": {"domain": "architecture"}},
    {"content": "HIPAA compliance requires encryption in transit, encryption at rest, and audit trails.", "metadata": {"domain": "compliance"}},
]
engine = HybridSearchEngine(mock_index)

class QueryRequest(BaseModel):
    query: str
    top_k: int = 3

@app.get("/health")
def health_check():
    return {"status": "HEALTHY", "service": "rag-pipeline"}

@app.post("/query")
def query_knowledge_base(req: QueryRequest):
    hits = engine.search(req.query, top_k=req.top_k)
    return {"query": req.query, "results": hits}
