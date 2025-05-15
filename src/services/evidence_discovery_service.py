from abc import ABC, abstractmethod
from typing import List, Dict, Any

class EvidenceDiscoveryService(ABC):
    """Service responsible for discovering evidence for marketing claims."""
    
    @abstractmethod
    def find_evidence(self, claim: str) -> List[Dict[str, Any]]:
        """Find evidence supporting a given marketing claim."""
        pass
    
    @abstractmethod
    def get_evidence_details(self, evidence_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific piece of evidence."""
        pass
    
    @abstractmethod
    def rank_evidence(self, evidence_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Rank evidence based on relevance and reliability."""
        pass 