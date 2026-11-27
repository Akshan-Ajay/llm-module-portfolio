---

# Final Reflection: From Statistical Text Models to Autonomous Local AI Agents

**Module:** PUSL 3205 — Large Language Models and Generative AI  
**Student:** Suthakaran Akshan (`10967118`)  

---

## 1. Executive Synthesis: The Arc of NLP & Generative AI

By undertaking all 6 PUSL 3205 labs, a holistic understanding was gained about the progression of artificial intelligence for language processing and the relevance of different approaches to application needs:

1. **Statistical Representations (Lab 01):** Using BOW and TF-IDF along with Logistic Regression and LinearSVC confirmed that sparse word level data can produce highly accurate results (81.17%) for labellled sentiment analysis. However, such models fail to represent syntactic and semantic information and are also non-generative.
2. **People-First AI Design (Lab 02):**  Working alongside an LLM in the FoodLoop project illustrated that good AI design follows from well-defined problems and application focussed solutions. Appropriate technologies were therefore deployed for each aspect of the solution; namely, Random Forests for numerical prediction and an LLM for inferencing.
3. **Basic Neural Language Models (Lab 03):**  Manually coding a decoder-only Transformer neural network (~0.83M parameters) in PyTorch enabled an understanding of auto-regressive self-attention, positional encodings and cross-entropy for sequence prediction. Model perplexity was obtained as 4.6700 and controlled generation was realised by adjusting the temperature parameter.
4. **Efficient Fine-tuning for Application Specificity (Lab 04):**  Efficient Fine-tuning for Application Specificity (Lab 04): 4-bit precision (NF4) and QLoRA (r=16, alpha=32) fine-tuning of `Qwen2.5-0.5B-Instruct’ on one NVIDIA Tesla T4 graphics card illustrated that even a small base model can effectively encode bespoke application specific information (a computer store in Homagama, Sri Lanka) based on as few as 30 expertly selected question-answer examples.
5. **Information-based Knowledge Access (Lab 05):** Developing the University AI Assistant highlighted the value of Retrieval Augmented Generation (RAG) where information is regularly updated and/or sources need to be referenced. Integration of high-density embeddings (`qwen3-embedding:0.6b’, ChromaDB) together with a Cross-Encoder re-ranker (`ms-marco-MiniLM-L-6-v2’) and stringent non-hallucination prompts ensured truthful responses which referenced precise pages within the MOHE Computing Award Handbook.
6. **Autonomy, Memory and Process Coordination (Lab 06 / `Lab-05-AI-Agents’):**  Enhancing the local `llama3.2:3b’ model using LangChain to interface with tools including pyautogui, I/O and SQLite memory storage as well as ChromaDB RAG and Dockerised n8n process coordination, enabled the LLM to transition from a static text producer to a dynamic control centre. It could thus manipulate computer software and even book genuine appointments on a Google Calendar through OAuth 2.0.

---

## 2. Key Architectural Trade-Offs Learned

### Fine-Tuning (QLoRA) vs. Retrieval-Augmented Generation (RAG)
* **When to Fine-Tune (Lab 04):** Fine-tuning (Lab 04) is optimal where a model needs to be personalised for voice, format and core functionality. It does, however, have limited ability to autonomously refresh factual information and is unable to name specific pages on referenced documents.

Using RAG with Reranking (Lab 05) is ideal for developing real-time and audit-able information resources, for example, university handbooks and publicity material. Employing a 2-stage retrieval and reranking procedure (initial `k=10` dense retrieval, followed by top 3 Cross-Encoder reranking) vastly enhanced the relevancy of contextual information for generation.
* **When to Use RAG + Reranking (Lab 05):** Essential for dynamic, verifiable knowledge bases (such as university handbooks and brochures). Adding a two-stage retrieve-and-rerank pipeline (`k=10` dense search $\rightarrow$ top-3 Cross-Encoder reranking) significantly improved context precision before generation.

### Small Local Models (`3B` / `0.5B`) vs. Deterministic Tools
Utilising Ollama to run `llama3.2:3b` locally eliminated both API charges and safeguarded student and organisational data within PDFs.

Nevertheless, small parameter models are not adept at performing complex numerical computations and can misinterpret equivocal tool inputs. By using deterministic tools (either Windows’ `calc.exe` or n8n’s Calculator node), applying `temperature=0` and clearly defining prompts in key-value pairs greatly augmented tool invocation accuracy.

### Code-First Agents vs. Visual Workflow Orchestration (n8n + Docker)
Code-based Agents and Graphical n8n/Docker workflow management

Python and LangChain Agents enable precise management of OS graphical user interface (GUI) functions via `pyautogui`, bespoke SQLite database design and local vector databases.

Further, Dockerised n8n Workflows expedite connections to external cloud-based OAuth 2.0 APIs (for instance, Google Calendar). These also include inherent chat-window history functionality, graphical workflow monitoring and swift development capabilities.

---

## 3. Practical Engineering Challenges & Takeaways

Across the labs, resolving real environment and system issues reinforced essential software engineering discipline:
* **Environment & Path Isolation:** Resolving PowerShell virtual environment collisions (`rag_env`) and Streamlit's `ScriptRunContext` execution model highlighted the importance of isolated environments and frozen dependency manifests.
* **Container Networking:** Configuring `http://host.docker.internal:11434` inside Dockerized n8n demonstrated how containerized services communicate with host-level local inference servers.
* **Data & Credential Hygiene:** Enforcing `.gitignore` rules for vector stores, SQLite databases, and OAuth 2.0 client secrets established production-grade repository security practices.

---

## 4. Conclusion
The six labs collectively show how a range of technologies including conventional NLP, bespoke Transformers, QLoRA and a two-stage RAG can all be utilised along with local tool agents to create secure and practical AI.
