"""Recursive Text and Semantic Chunker."""
from typing import List, Dict, Any

class DocumentChunker:
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_text(self, text: str, metadata: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        metadata = metadata or {}
        words = text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = min(start + self.chunk_size, len(words))
            chunk_content = " ".join(words[start:end])
            chunk_meta = dict(metadata)
            chunk_meta["chunk_index"] = len(chunks)
            chunk_meta["word_count"] = len(words[start:end])
            chunks.append({
                "content": chunk_content,
                "metadata": chunk_meta
            })
            if end == len(words):
                break
            start += (self.chunk_size - self.chunk_overlap)

        return chunks
