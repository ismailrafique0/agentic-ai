# API-Lab (Week 02) - Final Project

Complete API client demonstrating all concepts from Phases 01-05.

## Project Structure

```
API-Lab/
├── final_project/
│   ├── src/
│   │   ├── api_client.py
│   │   └── utils.py
│   ├── .env.example
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
└── evidence/
```

## Features

- API communication with JSONPlaceholder
- HTTP methods (GET, POST, PUT, DELETE)
- JSON parsing and data extraction
- Authentication with API keys via environment variables
- Comprehensive error handling (404, 400, 401, 429, 500)
- Request timeout handling
- Network failure handling
- Rate limiting awareness

## Setup

```bash
cd final_project
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API key (use dummy key for JSONPlaceholder)
python src/api_client.py
```

## API Details

- **Base URL:** https://jsonplaceholder.typicode.com
- **Authentication:** Not required for JSONPlaceholder (demonstrates pattern)
- **Rate Limiting:** Be mindful of requests

## Security

- Never commit real API keys
- Use `.env` for credentials
- `.env` is in `.gitignore`
