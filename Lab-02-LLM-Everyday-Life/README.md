# PUSL 3205 – Large Language Models and Generative AI
## Lab 02: AI in Everyday Challenges — *FoodLoop* (Group 3: The Food Waster)

---

## 1. Lab Objective & Problem Context

The objective of **Lab 02** was to apply Large Language Models (LLMs) and complementary machine learning techniques to solve an everyday challenge faced by university students, fostering critical thinking, structured product design, and practical AI integration.

### Assigned Challenge: Group 3 — The Food Waster
Students often purchase excessive amounts of food, forget what they have placed in communal fridges and hostel fridges and also throw away still edible food as they struggle to think of ideas for meals. Additionally, students across a university strive to source cheap consumable food and inexpensive foodstuffs.

---

## 2. Lab Session Execution & Development Workflow

In the lab, our group worked together with an LLM to design a solution to the above issue and developed an AI based product as follows:

1. **Problem Decomposition & Persona Alignment:** Using multiple prompts, we interrogated student behaviour regarding food purchasing. This highlighted student housing related limitations including poor cooking facilities, limited finances, and high workloads.
2. **Designing Appropriate ML and Generative AI Tools** Careful consideration allowed us to distinguish between prescriptive quantitative and generative qualitative tools. Thus, rather than utilising an LLM for all areas of the product, we used:
   * **Computer Vision and Barcode Recognition: ** Automatically recognise and input food and associated amounts from receipts, barcodes and/or photographs of food.
   * **Random Forest Regressor (Tabular ML):** Identify people’s food purchasing, consumption and wastage trends and advise on appropriate future food buying volumes.
   * **LLM (Generative AI): ** Create sequential student recipes using soon-expiring food within their pantry. Furthermore, it can formulate concise and clearly-labelled (safe) information for students to list on the Campus Food Marketplace.
3. **Prototyping & Visual Mock-ups:** We then devised complete wireframe designs for the following app functionality – inventory management, AI recipe creation and campus food gifting/trading.
4. **Presentation Development:**Our group compiled a 2-3 minute presentation encapsulating our analysis, design process and the application of AI.

---

## 3. Product Overview: FoodLoop

**FoodLoop** is an AI-powered mobile application designed to minimize student food waste while connecting surplus food with budget-conscious peers on campus.

### Target Users
* **Main Users:** Students residing in hostels, boarding houses and/or shared housing that self-manage their food and commonly misremember what they have.
* **Secondary Users:** Students looking for cheap and safe food to gift or to buy, especially within local on-campus areas.
Product Components


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

Our group recognised and defined key considerations that should be adhered to when designing the product for successful operation:
1. **Food Marketplace Safety: **  Listings must specify when food was prepared and its expiry date. Furthermore, they must include food and allergy relevant information. Finally, only students may gift freshly prepared food and this must be in single portions for the same day. Sealed foodstuffs may also be gifted.
2. **Student Operational Limitations: ** The LLM recipe advisor is prompted to only provide recipes that can be prepared with simple student housing cooking appliances (microwave, kettle and one hob/pan) and within under 20 minutes.
3. **Cold-Start Fallback for ML:** As the Random Forest Regressor depends on an individual’s food buying and wastage information, novices initially receive generic one person serving size guidelines. Appropriate personal data is then analysed week-by-week.

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
