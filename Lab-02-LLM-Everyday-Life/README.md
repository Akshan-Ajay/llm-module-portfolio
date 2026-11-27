# PUSL 3205 – Large Language Models and Generative AI
## Lab 02: AI in Everyday Challenges — *FoodLoop* (Group 3: The Food Waster)

---

## 1. Lab Objective & Problem Context

The objective of **Lab 02** was to apply Large Language Models (LLMs) and complementary machine learning techniques to solve an everyday challenge faced by university students, fostering critical thinking, structured product design, and practical AI integration.

### Assigned Challenge: Group 3 — The Food Waster
University students frequently buy more groceries than they can consume, forget perishable items stored in shared refrigerators or hostels, and discard usable leftovers due to a lack of meal ideas. Simultaneously, fellow students on campus actively seek affordable, ready-to-eat meals and low-cost groceries.

---

## 2. Lab Session Execution & Development Workflow

During the lab session, our group partnered with an LLM as an interactive product-development collaborator to move from problem framing to system architecture and UI prototyping:

1. **Problem Decomposition & Persona Alignment:** We used iterative LLM prompting to analyze student grocery habits—specifically identifying dorm/boarding-house constraints (limited cooking equipment, tight budgets, and busy lecture schedules).
2. **Architectural Separation of Concerns (ML vs. LLM):** Through critical evaluation, our group separated deterministic numerical prediction from generative language tasks rather than relying on an LLM for every function:
   * **Computer Vision / Barcode Parsing:** Automates item and quantity entry from receipts, barcodes, or food photos.
   * **Random Forest Regressor (Tabular ML):** Learns individual purchase, consumption, and waste patterns over time to recommend realistic future shopping quantities.
   * **LLM Assistant (Generative AI):** Generates step-by-step student recipes from expiring pantry items and drafts clear, safety-tagged descriptions for surplus marketplace listings.
3. **Prototyping & Visual Mock-ups:** We translated the architecture into end-to-end wireframes covering pantry tracking, AI recipe generation, and a campus peer-to-peer food sharing marketplace.
4. **Pitch Preparation:** We synthesized the problem, technical workflow, and AI roles into a structured 2–3 minute group presentation.

---

## 3. Product Overview: FoodLoop

**FoodLoop** is an AI-powered mobile application designed to minimize student food waste while connecting surplus food with budget-conscious peers on campus.

### Target Users
* **Primary Users:** University students living in hostels, boarding houses, or shared apartments who manage their own groceries and frequently lose track of perishables.
* **Secondary Users:** Students seeking affordable, safe surplus meals or unopened bulk ingredients within walking distance on campus.

### Core System Modules

| Module | Functionality | Underlying Technology / AI Role |
| :--- | :--- | :--- |
| **Smart Pantry & Multi-Modal Logging** | Logs food items and quantities via photo capture, barcode scanning, or manual entry; updates remaining stock as items are consumed or discarded. | Vision Recognition Model (e.g., YOLOv8) + SQL Inventory Database |
| **Proactive Expiry Alerts** | Monitors shelf life and sends timely push notifications before items spoil or go unused. | Node.js Scheduled Notification Service |
| **Predictive Shopping Optimizer** | Analyzes historical buy-use-waste ratios (e.g., buying 10 bananas, eating 6, wasting 4 $\rightarrow$ recommending 6–7 next trip) to prevent overbuying. | **Random Forest Regressor** (`scikit-learn`) |
| **AI Leftover Recipe Assistant** | Generates fast, low-cost recipes strictly prioritizing ingredients currently nearing expiration in the user's pantry. | **Large Language Model** (Prompt-constrained for dorm equipment & prep time) |
| **Campus Surplus Marketplace** | Enables students to share for free or sell suitable extra food and unopened groceries at affordable prices nearby. | NoSQL/Firebase Listing Feed + LLM Description & Safety Tag Generator |

---

## 4. System Architecture & Prototype Screenshots

All visual artifacts generated and documented during the lab session are stored in the `screenshots/` directory:

* **`screenshots/01-system-architecture.png`** — End-to-end data pipeline illustrating how mobile app inputs feed the SQL inventory, routing data to the Vision Recognition Service, Random Forest Purchase Predictor, LLM Recipe/Marketplace Assistant, and Notification/Marketplace services.
* **`screenshots/02-ui-inventory-dashboard.png`** — *My Pantry* dashboard showing categorized stock (Produce, Dairy & Chilled, Pantry & Dry), freshness indicators, weekly waste/savings metrics, and *Use Soon* alerts.
* **`screenshots/03-ui-llm-recipe-assistant.png`** — *AI Recipe Assistant* interface demonstrating context-aware recipe generation (*Creamy Spinach & Cheese Toast*) using expiring spinach, milk, and bread.
* **`screenshots/04-ui-student-marketplace.png`** — *Campus Food Marketplace* feed displaying free and low-cost student listings with distance tags, seller ratings, and freshness/allergen hashtags.

---

## 5. Ethical, Safety & Practical Guardrails Considered

During our group discussion, we established three design guardrails to ensure real-world viability:
1. **Food Safety in Peer Sharing:** Marketplace listings require clear preparation/expiry timestamps, dietary/allergen tags, and restrictions limiting cooked-food sharing to same-day portions alongside unopened packaged goods.
2. **Practical Student Constraints:** The LLM recipe prompt explicitly restricts suggestions to basic dorm equipment (microwave, kettle, single hob/pan) and under 20 minutes of preparation time.
3. **Cold-Start Fallback for ML:** Because the Random Forest Regressor requires personal purchase-and-waste history, new users start with baseline single-student portion heuristics until sufficient weekly logs are recorded.

---

## 6. Repository Structure

```text
Lab-02-LLM-Everyday-Life/
├── README.md                                  # Lab documentation, system design & implementation report
├── group-activity/
│   ├── group-members.md                       # Group 3 member roster and individual contributions
│   ├── activity-outcomes.md                   # Formal deliverables (concept, target user, features, prototype)
│   └── discussion-summary.md                  # Summary of LLM brainstorming, trade-offs & prompt logs
└── screenshots/
    ├── 01-system-architecture.png             # End-to-end system workflow diagram
    ├── 02-ui-inventory-dashboard.png          # Pantry inventory & expiry tracking UI mock-up
    ├── 03-ui-llm-recipe-assistant.png         # LLM leftover recipe generator UI mock-up
    ├── 04-ui-student-marketplace.png          # Campus food-sharing marketplace UI mock-up
    └── 05-llm-brainstorming-evidence.png      # Evidence of LLM collaboration during lab activity