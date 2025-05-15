# Boston Scientific GenAI Enabler

A modular and extensible GenAI-based system for evidence and claim discovery in marketing materials.

## Features

1. **Evidence Discovery**: Find supporting evidence for marketing claims
2. **Claim Discovery**: Discover marketing claims based on given evidence
3. **Open Chat**: Interactive chat interface for general queries

## Project Structure

```
src/
├── services/
│   ├── ingestion_service.py      # Document ingestion service
│   ├── evidence_discovery_service.py  # Evidence discovery service
│   ├── claim_discovery_service.py     # Claim discovery service
│   └── chat_service.py           # Chat interface service
├── models/                       # Data models and schemas
├── config/                       # Configuration files
├── utils/                        # Utility functions
└── app.py                        # Main Streamlit application
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run src/app.py
```

## Architecture

The project follows a service-oriented architecture with the following components:

1. **Ingestion Service**: Handles document processing and storage
2. **Evidence Discovery Service**: Finds evidence for marketing claims
3. **Claim Discovery Service**: Discovers claims based on evidence
4. **Chat Service**: Manages interactive chat functionality

Each service is designed to be modular and can be easily integrated with different frontend frameworks or backend systems.

## Future Enhancements

1. Integration with web search and online resources
2. Advanced document processing capabilities
3. Custom UI implementation (e.g., React-based frontend)
4. Enhanced security and access control
5. Analytics and reporting features