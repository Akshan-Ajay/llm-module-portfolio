# Lab 05: University AI Assistant using Retrieval-Augmented Generation (RAG)

## 📌 Overview
This laboratory activity implements a document-grounded **University AI Assistant** using a **Retrieval-Augmented Generation (RAG)** architecture enhanced with **Cross-Encoder Reranking**. 

Instead of relying purely on a Large Language Model's pre-trained knowledge, this system ingests local university documents (such as degree handbooks and brochures), converts them into vector embeddings stored in **ChromaDB**, retrieves and reranks the most relevant passages, and uses a local LLM (**Llama 3.2 3B** via Ollama) to generate accurate, cited answers. It features both a Command-Line Interface (CLI) and an interactive **Streamlit** web application that supports multi-PDF uploads.

---

## 📂 Repository & Folder Structure

```text
Lab-05-AI-Agents/
├── README.md                                  # Detailed lab documentation & output analysis
├── .gitignore                                 # Excludes virtual env (rag_env), chroma_db, and caches
├── notebooks/
│   ├── app.py                                 # Streamlit web UI with multi-PDF upload & chat history
│   ├── ingest.py                              # Core PDF parsing, chunking, hashing & ChromaDB indexing
│   ├── run_ingest.py                          # CLI helper script to ingest initial handbook PDFs
│   ├── rag_pipeline.py                        # Retrieval, Cross-Encoder reranking, & LLM generation
│   ├── requirements.txt                       # Frozen Python dependencies for reproducibility
│   └── data/                                  # Local storage for uploaded and indexed PDF documents
│       └── COMPUTING AWARD HANDBOOK_MOHE (2).pdf
└── screenshots/                               # Visual verification of execution & outputs
    ├── run_ingest_sc.png
    ├── rag_pipeline_screenshot.png
    ├── streamlit_app_success.png
    ├── Uni_Ai_Assistant.png
    ├── upload_doc_success.png
    └── Output_of_ai_question.png
```

---

## 🧠 System Architecture & Code Breakdown

### 1. Document Ingestion Pipeline (`ingest.py` & `run_ingest.py`)
* **Validation & Deduplication:** Uses SHA-256 content hashing (`hashlib.sha256`) on uploaded PDF bytes to prevent duplicate indexing of identical documents. If a document hash already exists in ChromaDB, ingestion is skipped (`Already indexed: ...`).
* **Text Extraction & Chunking:** Utilizes `PyMuPDFLoader` to extract text page-by-page and splits it using `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=150`) to preserve semantic context across boundaries.
* **Embedding & Vector Storage:** Uses Ollama's `qwen3-embedding:0.6b` model to generate vector embeddings and persists them locally in **ChromaDB** under the collection `university_knowledge`.
* **CLI Batch Ingestion (`run_ingest.py`):** Simulates a file upload via a `CLIUploadedFile` wrapper to index the initial `COMPUTING AWARD HANDBOOK_MOHE (2).pdf` prior to launching the UI.

### 2. Retrieval, Reranking & Generation (`rag_pipeline.py`)
* **Two-Stage Retrieval (Retrieve & Rerank):**
  1. **Broad Vector Search:** Queries ChromaDB for the top $k=10$ semantically similar chunks.
  2. **Cross-Encoder Reranking:** Passes `(question, chunk)` pairs through `cross-encoder/ms-marco-MiniLM-L-6-v2` to score true contextual relevance, keeping only the **top 3 highest-scoring chunks**.
* **Grounded Prompt Engineering:** Feeds the top 3 chunks into `ChatOllama` (`llama3.2:3b`, `temperature=0`) with strict system instructions to prevent hallucination, cite sources (`[Source N]`), and abstain if the answer is not in the documents.

### 3. Interactive Web Interface (`app.py`)
* **Multi-PDF Knowledge Base Sidebar:** Allows users to upload multiple PDFs simultaneously, tracks progress with a live progress bar, and lists all currently indexed PDFs in `data/`.
* **Conversational Chat UI:** Maintains conversation history via `st.session_state.messages` and provides expandable **"View Retrieved Sources"** dropdowns displaying the exact source document name and page number for every answer.

---

## ⚙️ Environment Setup & Execution Workflow

### 1. Virtual Environment & Dependencies
A dedicated Python virtual environment (`rag_env`) was created and populated using `requirements.txt`:
```powershell
python -m venv rag_env
.\rag_env\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Local LLM & Embedding Models (Ollama)
Before running the scripts, the following local models were pulled via Ollama:
```powershell
ollama pull llama3.2:3b
ollama pull qwen3-embedding:0.6b
```

---

## 📊 Execution Outputs & Analysis

Below is a detailed breakdown of what occurred during execution, based on the captured terminal logs and screenshots:

### 1. Database Reset & Document Ingestion (`run_ingest.py`)
* **What Happened:** Initially, running `python run_ingest.py` returned `Already indexed: COMPUTING_AWARD_HANDBOOK_MOHE__2_.pdf` because the SHA-256 hash check detected existing vectors in `chroma_db`. After clearing the old database (`Remove-Item -Recurse -Force chroma_db`), re-running `run_ingest.py` extracted, chunked, embedded, and stored the handbook from scratch:
  ```text
  Ingesting: COMPUTING AWARD HANDBOOK_MOHE (2).pdf...
  Successfully indexed COMPUTING_AWARD_HANDBOOK_MOHE__2_.
  ```
* **Screenshot Reference:** `screenshots/run_ingest_sc.png`

### 2. CLI RAG Pipeline Verification (`rag_pipeline.py`)
* **What Happened:** Running `python rag_pipeline.py` loaded the `ms-marco-MiniLM-L-6-v2` Cross-Encoder weights (`105/105` layers) and initiated an interactive terminal prompt.
* **Test Query:** *"Details about Software engineering?"*
* **Result Analysis:** The pipeline retrieved 10 chunks, reranked them down to the top 3 most relevant pages (**Pages 6 and 9** of the MOHE Computing Award Handbook), and generated a structured breakdown covering ACM/IEEE alignment, year-by-year curriculum structure (compulsory 3rd-year industry training, 4th-year individual project), and 8 career pathways.
* **Screenshot Reference:** `screenshots/rag_pipeline_screenshot.png`

### 3. Launching the Streamlit Web Application (`app.py`)
* **Troubleshooting Note:** Running `python app.py` directly triggered `missing ScriptRunContext!` warnings because Streamlit requires its own server runtime to manage browser sessions.
* **Resolution:** Launching via `streamlit run app.py` started the Uvicorn/Streamlit web server on `http://localhost:8501`.
* **UI Capabilities Verified:**
  * Initial interface rendering (`screenshots/streamlit_app_success.png` & `screenshots/Uni_Ai_Assistant.png`).
  * Uploading and indexing additional university PDFs (e.g., *NSBM Sri Lanka Brochure*) via the sidebar (`screenshots/upload_doc_success.png`).
  * Querying across multiple documents with expandable source citations (`screenshots/Output_of_ai_question.png`).
