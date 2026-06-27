# HR RAG System

A complete HR Assistant powered by Retrieval-Augmented Generation (RAG), built with **Python FastAPI** backend and **React + Vite** frontend.

---

## Screenshot
<img width="1917" height="873" alt="Screenshot 2026-06-27 103604" src="https://github.com/user-attachments/assets/7477e074-f59b-4362-a30d-7ec98ca73882" />
<img width="1917" height="883" alt="Screenshot 2026-06-27 103632" src="https://github.com/user-attachments/assets/e01374b0-78a0-49bd-b25a-f67993cd270e" />


---

## Overview

Complete HR Assistant RAG system with:
- JWT Authentication
- Multi-intent classification
- Document RAG (PDF processing)
- SQL RAG (HR database queries)
- Intent-based routing
- CORS support

---

## Project Structure

```
RAG_hr_system/
├── RAG_Python_API/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── chat_service.py
│   ├── hr_service.py
│   ├── document_service.py
│   ├── init_db.py
│   ├── requirements.txt
│   └── .env.example
│
└── HR_RAG_Frontend/
    ├── src/
    │   ├── pages/
    │   │   ├── Login.jsx
    │   │   ├── Register.jsx
    │   │   └── Chat.jsx
    │   ├── api.js
    │   └── main.jsx
    └── package.json
```

---

## Backend Setup

### 1. Install Dependencies
```bash
cd RAG_Python_API
pip install -r requirements.txt
```

### 2. Environment Configuration
Copy `.env.example` to `.env` and fill in your values:
```env
AZURE_OPENAI_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=your-chat-deployment-name
AZURE_OPENAI_CLASSIFIER_DEPLOYMENT=your-classifier-deployment-name
PDF_PATH=C:\path\to\HR-Policy.pdf
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

API available at: **http://localhost:8080**  
Swagger UI at: **http://localhost:8080/docs**

---

## Frontend Setup

```bash
cd HR_RAG_Frontend
npm install
npm run dev
```

Frontend available at: **http://localhost:5173**

---

## API Endpoints

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/auth/register` | Register new user | ❌ |
| POST | `/auth/login` | User login | ❌ |
| POST | `/api/ask` | Ask HR questions | ✅ |
| GET | `/health` | Health check | ❌ |

---

## Usage Examples

### Register
```bash
curl -X POST "http://localhost:8080/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"username": "test_user", "password": "password123", "department": "Engineering"}'
```

### Login
```bash
curl -X POST "http://localhost:8080/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "password123"}'
```

### Ask Questions
```bash
curl -X POST "http://localhost:8080/api/ask" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"message": "How many leaves do I have remaining?"}'
```

---

## Sample Test Users

| Username | Password | Department |
|----------|----------|------------|
| john_doe | password123 | Engineering |
| jane_smith | password123 | HR |
| mike_wilson | password123 | Finance |

---

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

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python FastAPI |
| Authentication | JWT + bcrypt |
| Database | SQLAlchemy + SQLite |
| PDF Processing | PyPDF2 |
| Embeddings | sentence-transformers (all-MiniLM-L6-v2) |
| Vector Search | FAISS (cosine similarity) |
| LLM | Azure OpenAI (GPT) |
| Frontend | React + Vite |
| Styling | Brutalism CSS |
