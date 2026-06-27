# HR RAG API - Python FastAPI

Complete Python implementation of the Spring Boot HR RAG system using FastAPI, with all features including:
- JWT Authentication
- Multi-intent classification 
- Document RAG (PDF processing)
- SQL RAG (HR database queries)
- Intent-based routing
- CORS support

## Features

### Authentication & Security
- JWT token-based authentication
- Password hashing with bcrypt
- Protected endpoints
- User registration and login

### RAG Functionality
- **Document RAG**: PDF processing with embeddings and vector search
- **SQL RAG**: Database queries for HR data (salary, payslips, leave balance, performance reviews)
- **Intent Classification**: Smart routing based on question classification
- **Multi-intent Support**: Handle complex questions spanning multiple data sources

### Database Models
- Users (with roles and departments)
- Leave Balance
- Salary records
- Payslips  
- Performance Reviews

## Setup

### 1. Install Dependencies
```bash
cd RAG_Python_API
pip install -r requirements.txt
```

### 2. Environment Configuration
Edit `.env` file:
```env
OPENAI_API_KEY=your-actual-openai-api-key
PDF_PATH=hr_policies.pdf
SECRET_KEY=your-secret-key-for-jwt
```

### 3. Initialize Database
```bash
python init_db.py
```

### 4. Run the Application
```bash
python main.py
```

API will be available at: http://localhost:8000

## API Endpoints

### Authentication
- **POST** `/auth/register` - Register new user
- **POST** `/auth/login` - User login

### Chat
- **POST** `/api/ask` - Ask HR questions (requires authentication)

### Health
- **GET** `/` - Root endpoint
- **GET** `/health` - Health check

## Usage Examples

### 1. Register a User
```bash
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "test_user",
    "password": "password123",
    "department": "Engineering"
  }'
```

### 2. Login
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "password123"
  }'
```

### 3. Ask Questions
```bash
curl -X POST "http://localhost:8000/api/ask" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "How many leaves do I have remaining?"
  }'
```

## Sample Data

The initialization script creates 3 test users:
- **john_doe** / password123 (Engineering)
- **jane_smith** / password123 (HR)  
- **mike_wilson** / password123 (Finance)

Each user has sample data for:
- Leave balances
- Salary history
- Payslips
- Performance reviews

## Question Types Supported

### Single Intent
- "How many leaves do I have?" → Leave balance
- "What is my salary?" → Salary information
- "Show my payslip" → Payslip data
- "What was my performance rating?" → Performance review
- "What is the leave policy?" → Policy documents

### Multi Intent  
- "Show my salary and leave balance" → Combined response
- "What are my payslips and performance reviews?" → Multiple data sources

## Interactive Documentation

Visit http://localhost:8000/docs for Swagger UI documentation with interactive API testing.

## Architecture

```
RAG_Python_API/
├── main.py              # FastAPI application
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic request/response schemas
├── database.py          # Database configuration
├── auth.py              # JWT authentication service
├── chat_service.py      # Intent classification and routing
├── hr_service.py        # SQL RAG for HR data
├── document_service.py  # Document RAG for PDFs
├── init_db.py          # Database initialization
├── requirements.txt     # Python dependencies
└── .env                # Environment configuration
```

## Comparison with Spring Boot Version

This Python implementation provides identical functionality to the Spring Boot version:

| Feature | Spring Boot | Python FastAPI |
|---------|-------------|----------------|
| Authentication | Spring Security + JWT | FastAPI + python-jose |
| Database | JPA/Hibernate | SQLAlchemy |
| PDF Processing | LangChain4j | PyPDF2 + sentence-transformers |
| Vector Search | In-memory | FAISS |
| LLM Integration | Azure OpenAI | OpenAI API |
| Intent Classification | ✓ | ✓ |
| Multi-intent Support | ✓ | ✓ |
| CORS Support | ✓ | ✓ |

## Development

To add new HR data or modify existing models, update:
1. `models.py` - Database schema
2. `hr_service.py` - Query methods  
3. `chat_service.py` - Intent handling
4. `init_db.py` - Sample data