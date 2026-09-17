import pytest
from src.ingestion.chunker import DocumentChunker
from src.ingestion.metadata_tagger import MetadataTagger
from src.retrieval.hybrid_search import HybridSearchEngine

def test_chunker():
    chunker = DocumentChunker(chunk_size=10, chunk_overlap=2)
    text = "one two three four five six seven eight nine ten eleven twelve thirteen"
    chunks = chunker.chunk_text(text)
    assert len(chunks) >= 2
    assert chunks[0]["metadata"]["chunk_index"] == 0

def test_metadata_tagger():
    tagger = MetadataTagger()
    meta = tagger.extract_metadata("hipaa_compliance.md", "# Security\nData must be encrypted.")
    assert "compliance" in meta["tags"]
    assert meta["domain"] == "regulatory"

def test_hybrid_search():
    docs = [
        {"content": "Delta Lake provides ACID transactions.", "metadata": {}},
        {"content": "Machine learning model deployment with FastAPI.", "metadata": {}}
    ]
    engine = HybridSearchEngine(docs)
    res = engine.search("ACID transactions", top_k=1)
    assert len(res) == 1
    assert "Delta Lake" in res[0]["content"]
