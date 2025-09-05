# Corrective RAG

Corrective RAG is an experimental project aimed at building a **Corrective Retrieval-Augmented Generation (RAG)** system.  
The project will focus on document ingestion, vector storage, retrieval, and later extend into corrective mechanisms for refining responses.

---

## 🚀 Features (Work in Progress)
- Document ingestion from web sources  
- Text splitting using `RecursiveCharacterTextSplitter`  
- Embedding with `OpenAIEmbeddings`  
- Vector storage powered by **ChromaDB**  
- Retrieval pipeline setup for RAG

---

## 📂 Project Structure
```
CRAG/
│── .env                # Environment variables
│── .env.example        # Example environment file
│── .gitignore
│── poetry.lock
│── poetry.toml
│── pyproject.toml
│── ingestion.py        # Document ingestion and vectorstore creation
│
└── graph/
    ├── chains/
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   └── test_chains.py
    │   └── __init__.py
    │
    ├── nodes/
    │   ├── __init__.py
    │   ├── consts.py
    │   ├── graph.py
    │   └── state.py
    │
    └── __init__.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/mouyse/Corrective-RAG.git
cd Corrective-RAG
```

### 2. Setup Virtual Environment (Poetry)
```bash
poetry install
```

### 3. Configure Environment Variables
Copy `.env.example` into a `.env` file and add your keys:
```env
OPENAI_API_KEY=your_openai_api_key
```

### 4. Run Ingestion
```bash
poetry run python ingestion.py
```

This will:
- Load documents from URLs  
- Split text into manageable chunks  
- Create embeddings using OpenAI  
- Store vectors in ChromaDB  

---

## 🔮 Roadmap
- [x] Setup ingestion pipeline  
- [ ] Add corrective refinement mechanisms  
- [ ] Integrate feedback-based corrections  
- [ ] Expand retriever with hybrid search  
- [ ] Build end-to-end RAG pipeline  

---

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a PR.

---

## 👤 Author
**Jay**  
📧 jayy.shah16@gmail.com  

---
