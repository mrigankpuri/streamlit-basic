import streamlit as st
from services.ingestion_service import IngestionService
from services.evidence_discovery_service import EvidenceDiscoveryService
from services.claim_discovery_service import ClaimDiscoveryService
from services.chat_service import ChatService

def main():
    st.title("Boston Scientific GenAI Enabler")
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Choose a feature",
        ["Evidence Discovery", "Claim Discovery", "Open Chat"]
    )
    
    if page == "Evidence Discovery":
        st.header("Evidence Discovery")
        claim = st.text_area("Enter your marketing claim:")
        if st.button("Find Evidence"):
            # TODO: Implement evidence discovery
            st.write("Evidence discovery functionality will be implemented here")
            
    elif page == "Claim Discovery":
        st.header("Claim Discovery")
        evidence = st.text_area("Enter your evidence:")
        if st.button("Find Claims"):
            # TODO: Implement claim discovery
            st.write("Claim discovery functionality will be implemented here")
            
    else:  # Open Chat
        st.header("Open Chat")
        user_input = st.text_input("Ask a question:")
        if st.button("Send"):
            # TODO: Implement chat functionality
            st.write("Chat functionality will be implemented here")

if __name__ == "__main__":
    main() 