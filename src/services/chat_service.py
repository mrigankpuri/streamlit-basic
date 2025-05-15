from abc import ABC, abstractmethod
from typing import List, Dict, Any

class ChatService(ABC):
    """Service responsible for handling chat interactions."""
    
    @abstractmethod
    def process_message(self, message: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Process a user message and return a response."""
        pass
    
    @abstractmethod
    def get_chat_history(self, session_id: str) -> List[Dict[str, Any]]:
        """Retrieve chat history for a specific session."""
        pass
    
    @abstractmethod
    def clear_chat_history(self, session_id: str) -> None:
        """Clear chat history for a specific session."""
        pass 