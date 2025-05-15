from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IngestionService(ABC):
    """Service responsible for ingesting and processing documents."""
    
    @abstractmethod
    def ingest_document(self, document_path: str) -> Dict[str, Any]:
        """Ingest a single document and return its processed content."""
        pass
    
    @abstractmethod
    def ingest_documents(self, document_paths: List[str]) -> List[Dict[str, Any]]:
        """Ingest multiple documents and return their processed contents."""
        pass
    
    @abstractmethod
    def get_document_metadata(self, document_id: str) -> Dict[str, Any]:
        """Retrieve metadata for a specific document."""
        pass 