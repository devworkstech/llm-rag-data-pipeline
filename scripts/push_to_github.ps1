param([string]$Username = "soniablake")
git init; git branch -M main; git add .
git commit -m "feat: Enterprise LLM Knowledge Base RAG Data Pipeline - Pinecone, ChromaDB, FastAPI, Semantic Chunking"
git remote remove origin 2>$null
git remote add origin "https://github.com/$Username/llm-rag-data-pipeline.git"
git push -u origin main
