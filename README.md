# Lab 05: University AI Assistant using Retrieval-Augmented Generation (RAG)

## 📌 Overview
This lab implements a document based ‘University AI Assistant’ using a Retrieval Augmented Generation framework, and includes Cross Encoder Reranking functionality.

Whilst Large Language Models are powerful in their inbuilt knowledge alone, this system processes University documents (for example, information about degrees and university brochures), produces vector representations of them and saves these to a ChromaDB. Appropriate sections are then retrieved and reordered by importance and finally used as input for a Local Large Language Model (Llama 3.2 3B – accessed via Ollama) to produce well referenced, correct responses. There is also a Command Line Interface alongside a Streamlit based, web-based UI, which allows for multiple PDF files to be uploaded.


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

### 1. Document Processing (ingest.py & run_ingest.py)
* **Duplicate Detection: Uploaded PDFs are analysed by firstly converting them into bytes. These are then hashed (using hashlib.sha256) so that if they have previously been indexed (already indexed: ...) processing ceases.
* *Text Extraction & Sectioning: Text is page-wise extracted from PDFs using PyMuPDFLoader. This is then sectioned using the RecursiveCharacterTextSplitter method (chunk size = 1000, chunk overlap = 150) so that each section is still contextually coherent.
* **Vector Creation & Saving: Vector representations are produced with Ollama’s qwen3-embedding:0.6b model. These are then locally saved into a ChromaDB collection called university_knowledge.
* **Command Line Interface Processing (run_ingest.py): A CLIUploadedFile class is used to emulate a file being uploaded. This is then used to process and index the initial COMPUTING AWARD HANDBOOK_MOHE (2).pdf file. Subsequently the UI can be opened.

### 2. Retrieval, Reranking, Response Generation (rag_pipeline.py)
* **Two-Stage Retrieval (Retrieve & Rerank):**
  1. **Broad Vector Search:** Queries ChromaDB for the top $k=10$ semantically similar chunks.
  2. **Cross-Encoder Reranking:** Passes `(question, chunk)` pairs through `cross-encoder/ms-marco-MiniLM-L-6-v2` to score true contextual relevance, keeping only the **top 3 highest-scoring chunks**.
* **Grounded Prompt Engineering:** Feeds the top 3 chunks into `ChatOllama` (`llama3.2:3b`, `temperature=0`) with strict system instructions to prevent hallucination, cite sources (`[Source N]`), and abstain if the answer is not in the documents.

### 3. Interactive Web Interface (`app.py`)
* **Sidebar Document Repository: Multiple PDF files can be uploaded. Progress is shown in real time and the names of all currently indexed PDFs are displayed in the data/ folder.
* **Conversational Chat UI:** Previous chat messages are recorded within st.session_state.messages. Furthermore, each answer includes a ‘View Retrieved Sources’ menu which can be clicked to show the precise source document and page number.

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
* **What Happened:** Firstly, the python rag_pipeline.py code loaded the Cross Encoder ms-marco-MiniLM-L-6-v2 weights (105/105 layers). An interactive command Line Interface was then opened.
* **Sample Question:** *"Details about Software engineering?"*
* **Result Analysis:** Corresponding sections were successfully retrieved. These were then reduced to the 3 most relevant pages (page 6 and 9 of the MOHE Computing Award Handbook). Finally, a structured response was outputted describing: ACM/IEEE conformity; the 3 year programme format (mandatory third year industry experience and a self-directed fourth year project); and 8 distinct career routes.* **Screenshot Reference:** `screenshots/rag_pipeline_screenshot.png`

### 3. Launching the Streamlit Web Application (`app.py`)
* **Troubleshooting Note:** Attempting to open python app.py produced ScriptRunContext! errors as Streamlit needs its own web server in order to handle browser session information.
* **Resolution:** Using streamlit run app.py launched a Uvicorn/Streamlit web server at http://localhost:8501.
* **UI Capabilities Verified:**
  *Correct initial display of the UI (screenshots/streamlit_app_success.png, screenshots/Uni_Ai_Assistant.png).
  * Successful uploading and processing of further university PDFs (for example, the NSBM Sri Lanka Brochure) via the UI sidebar (screenshots/upload_doc_success.png).
  * Cross document querying with reference menus (screenshots/Output_of_ai_question.png).
