@echo off
setlocal
echo ===================================================
echo  Enterprise LLM Knowledge Base RAG Data Pipeline
echo ===================================================
git init
git branch -M main
git add .
git commit -m "feat: Enterprise LLM Knowledge Base RAG Data Pipeline - Pinecone, ChromaDB, FastAPI, Semantic Chunking"
set /p GH_USER="Enter GitHub username (or press enter for soniablake): "
if "%GH_USER%"=="" set GH_USER=soniablake
git remote remove origin 2>nul
git remote add origin https://github.com/%GH_USER%/llm-rag-data-pipeline.git
git push -u origin main
pause
