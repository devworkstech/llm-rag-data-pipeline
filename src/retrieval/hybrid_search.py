"""Hybrid Vector + Lexical Search Engine."""
import re
from typing import List, Dict, Any

class HybridSearchEngine:
    def __init__(self, index_data: List[Dict[str, Any]] = None):
        self.index = index_data or []

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        query_words = set(re.findall(r'\w+', query.lower()))
        results = []
        for item in self.index:
            content_words = set(re.findall(r'\w+', item["content"].lower()))
            common = query_words.intersection(content_words)
            lexical_score = len(common) / max(len(query_words), 1)
            results.append({
                "content": item["content"],
                "metadata": item.get("metadata", {}),
                "score": round(lexical_score, 4)
            })
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]
