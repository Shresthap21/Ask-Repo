<<<<<<< HEAD
=======
# AskRepo – AI Codebase Assistant

Ask questions about any codebase using **semantic search + LLMs**.

AskRepo scans a repository, splits code into chunks, converts them into embeddings, stores them in a **FAISS vector index**, and retrieves relevant code snippets to answer questions using a **Large Language Model (Groq)**.

This allows developers to quickly understand unfamiliar codebases by asking natural language questions.


## 🚀 Features

* Scan a repository and detect source code files
* Split code into overlapping chunks for better context
* Generate embeddings using **SentenceTransformers**
* Store vectors in **FAISS** for fast similarity search
* Retrieve the most relevant code snippets
* Use **Groq LLM** to explain the code and answer questions


## 🏗️ How It Works

The system follows a **Retrieval-Augmented Generation (RAG)** pipeline:

```
Repository
   ↓
Scan source files
   ↓
Chunk code into segments
   ↓
Generate embeddings
   ↓
Store vectors in FAISS
   ↓
User question
   ↓
Semantic search
   ↓
Relevant code snippets
   ↓
LLM explanation
```

This enables **semantic code search + AI explanations**.


## 📁 Project Structure

```
ask-repo/

core/
│
├── chunker.py       # Splits code into chunks
└── scanner.py       # Scans repository and loads files

vector_store/
│
└── db.py            # Handles embeddings and FAISS vector search

ai_assistant.py      # LLM integration using Groq
main.py              # Entry point for indexing and querying

requirements.txt
```


## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/ask-repo
cd ask-repo
```

Install dependencies:

```
pip install -r requirements.txt
```


## 🔑 Setup Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_api_key_here
```

Get a free API key from:

```
https://console.groq.com
```


## ▶️ Running the Project

Start the application:

```
python main.py
```

Enter the path of the repository you want to analyze:

```
Enter repository path: /path/to/repo
```

Example:

```
Enter repository path: C:\Users\username\projects\my-app
```

The system will:

1. Scan the repository
2. Chunk the code files
3. Generate embeddings
4. Store vectors in FAISS


## 💬 Ask Questions About the Codebase

Once indexing is complete, you can ask questions like:

```
Ask about the codebase: where is authentication implemented
```

Example output:

```
AI Answer:

File: auth/middleware.py

Code:
def verify_token(...)

Explanation:
Authentication is handled through a JWT verification middleware
that validates the incoming request token.
```


## 📦 Requirements

Main dependencies used:

* `faiss-cpu`
* `sentence-transformers`
* `numpy`
* `groq`
* `python-dotenv`


## 🧠 Example Use Cases

AskRepo can help developers:

* Understand unfamiliar repositories
* Locate where specific features are implemented
* Navigate large codebases faster
* Explore open source projects
* Learn how systems are structured


## 🔮 Possible Improvements

Future enhancements could include:

* Function-level code chunking
* Support for GitHub repository URLs
* Persistent FAISS index
* CLI tool interface
* Web UI for interactive queries
>>>>>>> 176e0315395e3fec0a719c76947cfec95520eaef
