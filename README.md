# PUSL 3205 — Large Language Models and Generative AI: Practical Portfolio

* **Student Name:** Suthakaran Akshan (Student ID: `10967118`)
* **Module:** PUSL 3205 — Large Language Models and Generative AI
* **Institution:** NSBM Green University (in affiliation with University of Plymouth)
* **Academic Year:** 2026

---

## 1. Portfolio Overview

In this collection of experiments I explore step by step; an introduction to NLP, Transformers, model compression, Retrieval Augmented Generation and self-operating ‘agents’. Within the six labs I transition from basic statistical text analysis, onto manually designing my own decoder only neural network, finetune existing large language models on localised data, embed localised models within organisational information and then manage both on-site and remotely connected agents.

---

## 2. Laboratory Progression & Summary

| Lab | Directory | Core Focus | Key Technologies & Models | Key Outcomes & Metrics |
| :--- | :--- | :--- | :--- | :--- |
| **Lab 01** | [`Lab-01-Machine-Learning/`](./Lab-01-Machine-Learning/) | Sentiment Analysis Using Traditional ML | Python, Pandas, NLTK, Seaborn, `CountVectorizer` (BOW), `TfidfVectorizer`, Logistic Regression, `LinearSVC` | Trained on 3,000 UCI customer reviews (Amazon, IMDb, Yelp); Logistic Regression achieved **81.17% accuracy** and **81.26% F1-score**. |
| **Lab 02** | [`Lab-02-LLM-Everyday-Life/`](./Lab-02-LLM-Everyday-Life/) | AI in Everyday Challenges (*FoodLoop* — Group 3) | LLM Ideation Partner, Conceptual System Architecture, Random Forest + LLM Hybrid Design | Designed **FoodLoop**, a student food-waste reduction concept combining inventory alerts, LLM leftover recipes, Random Forest shopping predictions, and a campus food-sharing marketplace. |
| **Lab 03** | [`Lab-03-Tiny-Transformer/`](./Lab-03-Tiny-Transformer/) | Building a Tiny Decoder-Only Transformer | PyTorch, `TinyStories` dataset (5,000 stories / 4.17M tokens), Character-Level Tokenization, AdamW, Gradio | Implemented a **~0.83M parameter** causal Transformer (4 layers, 4 heads, 128 embedding dim); reached **1.5412 validation loss** (**4.6700 perplexity**) with an interactive Gradio story generator. |
| **Lab 04** | [`Lab-04-Fine-Tune/`](./Lab-04-Fine-Tune/) | Domain Fine-Tuning with QLoRA & SFT | Google Colab (NVIDIA Tesla T4), `Qwen/Qwen2.5-0.5B-Instruct`, PEFT/LoRA, BitsAndBytes (4-bit NF4), TRL (`SFTTrainer`) | Fine-tuned Qwen 2.5 (0.5B) on 30 custom Q&A pairs for a Homagama computer shop, transforming generic outputs into accurate, domain-specific customer support responses. |
| **Lab 05** | [`Lab-05-RAG-Pipeline/`](./Lab-05-RAG-Pipeline/) | University AI Assistant with Two-Stage RAG | Ollama (`llama3.2:3b`, `qwen3-embedding:0.6b`), ChromaDB, `ms-marco-MiniLM-L-6-v2` Cross-Encoder, PyMuPDF, Streamlit | Built a multi-PDF University AI Assistant featuring SHA-256 deduplication, top-10 vector search + top-3 Cross-Encoder reranking, strict source citations, and a Streamlit UI. |
| **Lab 06** | [`Lab 06 - Tool-Using AI Agents & n8n Automation/`](./Lab%2006%20-%20Tool-Using%20AI%20Agents%20%26%20n8n%20Automation/) | Tool-Using AI Agents, Persistent Memory & n8n | LangChain (`bind_tools`), Ollama (`llama3.2:3b`), SQLite, ChromaDB, `pyautogui`, Docker, n8n, Google Calendar OAuth 2.0 | Built 6-tool Windows GUI/file agents, dual short-

---

## 3. Repository Structure

```text
LLM-Practical-Portfolio/
│
├── README.md                                  # Portfolio overview, progression matrix & setup guide
├── Final-Reflection.md                        # Cross-lab architectural synthesis & engineering reflection
│
├── Lab-01-Machine-Learning/                   # Traditional NLP sentiment analysis (BOW, TF-IDF, Logistic Regression, LinearSVC)
│   ├── README.md
│   ├── notebook/
│   └── screenshots/
│
├── Lab-02-LLM-Everyday-Life/                  # Group 3 conceptual product design (FoodLoop) & presentation artifacts
│   ├── README.md
│   ├── group-activity/
│   │   ├── group-members.md
│   │   ├── activity-outcomes.md
│   │   └── discussion-summary.md
│   └── screenshots/
│   └── ppt_presentation/
|       └── FoodLoop-Group 3 Presentation.pptx
|
├── Lab-03-Tiny-Transformer/                   # From-scratch PyTorch decoder-only Transformer trained on TinyStories
│   ├── README.md
│   ├── notebooks/
│   └── results/
│
├── Lab-04-Fine-Tune/                          # 4-bit QLoRA supervised fine-tuning of Qwen2.5-0.5B-Instruct
│   ├── README.md
│   ├── notebooks/
│   └── screenshots/
│
├── Lab-05-RAG-Pipeline/                       # Local University AI Assistant with ChromaDB, Cross-Encoder reranking & Streamlit
│   ├── README.md
│   ├── notebooks/
│   └── screenshots/
│
└──Lab-Tool-Using-Ai-Agents-and-n8n-Automation//                          # Lab 06: Multi-tool OS agents, SQLite persistent memory, RAG & Dockerized n8n
    ├── README.md
    ├── notebooks/
    └── screenshots/
