# Enterprise LLM Knowledge Base RAG Data Pipeline

[![CI Pipeline](https://github.com/SoniaBlake-DataEng/llm-rag-data-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/SoniaBlake-DataEng/llm-rag-data-pipeline/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)](https://fastapi.tiangolo.com/)
[![Vector DB](https://img.shields.io/badge/Vector_DB-Pinecone_/_Chroma-blueviolet.svg)](https://www.pinecone.io/)

> **End-to-end data ingestion and embedding pipeline transforming unstructured enterprise documents into indexed vector representations with automated metadata extraction, semantic chunking, and hybrid retrieval for LLM chatbots.**

---

## 🏗️ Architecture & Data Ingestion Pipeline

```mermaid
flowchart TD
    subgraph Ingestion["Document Ingestion Layer"]
        Docs["Enterprise Docs<br/>(Markdown, PDF, Text)"] --> Parser["Document Parser & Cleaner"]
        Parser --> Chunker["Semantic / Recursive Chunker<br/>(512 tokens, 50 overlap)"]
        Chunker --> Tagger["Automated Metadata Tagger<br/>(Tags, Categories, Dates)"]
    end

    subgraph Embedding["Vector Generation & Storage"]
        Tagger --> Embedder["Dense Embedding Generator"]
        Embedder --> VectorDB[("Vector Database<br/>Pinecone / ChromaDB")]
    end

    subgraph Serving["Hybrid Retrieval & Serving Layer"]
        Query["User / LLM Prompt"] --> Hybrid["Hybrid Search Engine<br/>(Dense Vector + Sparse Keyword)"]
        VectorDB <--> Hybrid
        Hybrid --> API["FastAPI Serving Endpoint<br/>(/query, /ingest)"]
        API --> LLM["Enterprise AI Chatbot / Agent"]
    end
```

---

## 🚀 Key Technical Highlights

* **Intelligent Semantic Chunking**: Respects paragraph and sentence boundaries to avoid splitting critical context mid-sentence.
* **Rich Metadata Tagging**: Extracts author, document domain, regulatory classification, and chunk sequence indices to enable granular query filtering.
* **Hybrid Search Engine**: Fuses dense cosine similarity vector search with sparse keyword scoring to maximize retrieval recall on specialized terminology.
* **Production-Grade Serving API**: Built with FastAPI and Pydantic validation, offering sub-50ms query latency.

---

## 📂 Project Structure

```
llm-rag-data-pipeline/
├── .github/workflows/ci.yml       # CI workflow for linting & tests
├── docs/
│   └── architecture.md            # RAG pipeline design & chunking benchmarks
├── sample_docs/
│   ├── enterprise_governance.md   # Sample data platform governance doc
│   └── compliance_guide.md        # Sample HIPAA / SOC2 guide
├── src/
│   ├── __init__.py
│   ├── config.py                  # Pipeline configurations
│   ├── api/
│   │   └── app.py                 # FastAPI retrieval & query service
│   ├── ingestion/
│   │   ├── chunker.py             # Semantic document chunker
│   │   ├── metadata_tagger.py     # Metadata extractor
│   │   └── vector_indexer.py      # Embedding & index upsert engine
│   └── retrieval/
│       └── hybrid_search.py       # Dense + sparse retrieval engine
├── tests/
│   └── test_rag_pipeline.py       # Unit tests
├── scripts/
│   ├── setup_github.bat           # 1-click Windows push script
│   └── push_to_github.ps1         # PowerShell deployment script
├── docker-compose.yml             # Local service orchestration
├── requirements.txt               # Dependencies
└── .gitignore
```

---

## ⚡ Quickstart

```bash
# 1. Clone repository
git clone https://github.com/SoniaBlake-DataEng/llm-rag-data-pipeline.git
cd llm-rag-data-pipeline

# 2. Setup Virtual Environment
python -m venv venv
.\venv\Scripts\activate  # On Linux: source venv/bin/activate
pip install -r requirements.txt

# 3. Ingest documents into Vector Index
python -m src.ingestion.vector_indexer

# 4. Run tests
pytest tests/ -v

# 5. Start API Server
uvicorn src.api.app:app --reload --port 8000
```

---

## 📜 License
MIT License.
