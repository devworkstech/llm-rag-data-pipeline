# LLM Knowledge Base RAG Data Pipeline Architecture

## System Design
1. **Document Ingestion**: Recursively reads unstructured documents and applies clean text normalization.
2. **Chunking Strategy**: Configured with a 512-token window and 10% overlap to balance context retention with embedding precision.
3. **Metadata Filtering**: Enables downstream queries to filter by domain (`department == "compliance"`) before vector scoring.
4. **Hybrid Retrieval**: Combines semantic embeddings with lexical matching for high precision on acronyms and domain terms.
