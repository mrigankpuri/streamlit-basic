from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ClaimDiscoveryService(ABC):
    """Service responsible for discovering marketing claims based on evidence."""
    
    @abstractmethod
    def find_claims(self, evidence: str) -> List[Dict[str, Any]]:
        """Find marketing claims supported by given evidence."""
        pass
    
    @abstractmethod
    def get_claim_details(self, claim_id: str) -> Dict[str, Any]:
        """Get detailed information about a specific claim."""
        pass
    
    @abstractmethod
    def validate_claim(self, claim: str, evidence: str) -> Dict[str, Any]:
        """Validate if a claim is supported by given evidence."""
        pass 