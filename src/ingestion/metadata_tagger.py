"""Automated Document Metadata Extraction."""
import re
from datetime import datetime
from typing import Dict, Any

class MetadataTagger:
    @staticmethod
    def extract_metadata(filename: str, text: str) -> Dict[str, Any]:
        tags = []
        domain = "general"

        if "governance" in filename.lower() or "governance" in text.lower():
            tags.append("governance")
            domain = "data_governance"
        if "compliance" in filename.lower() or "hipaa" in text.lower() or "soc2" in text.lower():
            tags.append("compliance")
            domain = "regulatory"

        # Detect headers
        headers = re.findall(r'^#+\s+(.+)$', text, flags=re.MULTILINE)

        return {
            "source_file": filename,
            "domain": domain,
            "tags": tags,
            "headers": headers[:5],
            "ingested_at": datetime.utcnow().isoformat()
        }
