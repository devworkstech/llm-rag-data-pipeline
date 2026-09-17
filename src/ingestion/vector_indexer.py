"""Vector Database Indexer supporting Pinecone and in-memory mock."""
import logging
from typing import List, Dict, Any
from src.ingestion.chunker import DocumentChunker
from src.ingestion.metadata_tagger import MetadataTagger

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VectorIndexer:
    def __init__(self):
        self.chunker = DocumentChunker()
        self.tagger = MetadataTagger()
        self.in_memory_index = []

    def index_document(self, filename: str, content: str) -> int:
        meta = self.tagger.extract_metadata(filename, content)
        chunks = self.chunker.chunk_text(content, metadata=meta)
        for c in chunks:
            self.in_memory_index.append(c)
        logger.info("Indexed " + str(len(chunks)) + " chunks from " + filename)
        return len(chunks)

if __name__ == "__main__":
    sample_text = "Enterprise Data Governance Policy. All datasets in Delta Lake must have data contracts and classification tags."
    indexer = VectorIndexer()
    count = indexer.index_document("governance.md", sample_text)
    print("Indexed total chunks:", count)
