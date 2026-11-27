# PUSL 3205 – Large Language Models and Generative AI
## Lab 02: AI in Everyday Challenges — *FoodLoop* (Group 3: The Food Waster)

> **Lab Scope Note:** This lab focused on critical thinking, problem framing, research, using an LLM as a product-development brainstorming partner, designing conceptual UI/architecture mock-ups, creating presentation slides, and delivering a 2–3 minute group pitch. No production code or live software deployment was carried out for this activity.

---

## 1. Lab Objective & Assigned Challenge

The task for this lab was to utilise LLMs and develop our own problem solving and design skills to investigate how AI can be used to help solve common issues.

### Group 3 — The Food Waster
Many university students purchase too much food, and then either forget or are unable to utilise food that has been stored. Students also often do not know how to re-use food and so will throw it away. Concurrently, there are many students on campus who wish to eat cheaply. We aimed to therefore utilise an LLM as a co-creator and devise a novel product or service which helps to decrease students’ avoidable food waste.

---


## 2. What We Did During the Lab Session

1. Problem Exploration: Examined why university students tend to purchase and also unnecessarily dispose of food and recognised that there was potential to link students together – those with excess food and those wishing to save money.
2. LLM Brainstorm and definition: Worked with an LLM to further develop key functionality. Identified student cooking limitations (such as lack of cooking facilities in university residences) alongside their financial and time restraints. Developed an integrated solution – ‘FoodLoop’.
3. Functionality and AI specialisation: Defined the flow of data within the system and specialised which areas of AI would be most applicable:
   * Food Identification (vision & bar-coding): Enables food and associated volumes to be recognised either photographically, by bar-coding or via direct input.
   * Random Forest Regressor (Proposed Tabular AI): Analyses users’ previous purchasing, consumption and disposal information to advise on optimal future buying volumes.
   * LLM Assistant (generative AI): Provides students with easy-to-prepare recipes using their current stock and helps to effectively interpret and present market place information.
4. **Visual Mock-ups & Presentation Slides:** Created system flow and mobile interface designs. Developed a presentation to summarise the solution and presented this to the group (2-3 minutes).

---

## 4. Product Concept Overview: FoodLoop

**FoodLoop** is an envisioned mobile application which enables university students to monitor their food purchasing, consumption and disposal. It can then transform students’ surplus food into easy-to-prepare dishes. Additionally, it can advise on ideal future purchasing volumes. Finally, it facilitates students to both list and sell underutilised food on a campus wide, cost-effective marketplace, so that appropriate food can be obtained by others.

### Target Users
* **Primary Users:** University students living in hostels, boarding houses, or shared apartments who manage their own groceries and risk forgetting items or discarding leftovers.
* **Secondary Users:** Students looking for affordable, accessible surplus food or shared groceries within their campus community.

### Core Conceptual Features

| Feature | Description | Proposed AI / System Role |
| :--- | :--- | :--- |
| **Multi-Modal Food Logging** | Users log items and quantities by taking a photo, scanning a barcode, or entering food manually, and update amounts as items are eaten or thrown away. | Vision recognition / barcode parsing + SQL inventory tracking |
| **Expiry & Unused-Item Alerts** | Sends timely reminders when stored food has been unused for a while or is nearing its expiry date. | Automated reminder & notification service |
| **LLM Recipe Assistant** | Suggests simple, budget-friendly meals using ingredients already available in the user's inventory. | Large Language Model (constrained to available ingredients & student cooking setups) |
| **Smart Shopping Quantity Predictor** | Learns from past buy, use, and waste history (e.g., buying 10 bananas, eating 6, wasting 4 $\rightarrow$ suggesting 6–7 next time). | **Random Forest Regressor** |
| **Campus Food Marketplace** | Allows students to share or sell suitable extra food at an affordable price so surplus food reaches someone who can use it. | Campus peer-to-peer listing feed |

---

## 5. Visual Artifacts (`screenshots/`)

* **`screenshots/01-system-architecture.png`** — End-to-end conceptual system flow showing how mobile app inputs connect to inventory tracking, food recognition, the Random Forest purchase predictor, the LLM recipe/marketplace assistant, reminders, and the campus marketplace.
* **`screenshots/02-ui-inventory-dashboard.png`** — *My Pantry* UI mock-up displaying categorized food items, freshness/expiry indicators, waste/savings summary, and *Use Soon* alerts.
* **`screenshots/03-ui-llm-recipe-assistant.png`** — *AI Recipe Assistant* UI mock-up illustrating a generated recipe (*Creamy Spinach & Cheese Toast*) created from expiring pantry items.
* **`screenshots/04-ui-student-marketplace.png`** — *Campus Food Marketplace* UI mock-up showcasing free and low-cost student listings with distance, seller ratings, and item tags.
* **`screenshots/05-llm-brainstorming-evidence.png`** — Screenshot capturing our LLM brainstorming interaction used to define student cooking constraints and refine FoodLoop's features.

---

## 6. Repository Structure

```text
Lab-02-LLM-Everyday-Life/
├── README.md                                  # Lab documentation, concept overview & presentation summary
├── group-activity/
│   ├── group-members.md                       # Group 3 member roster and individual contributions
│   ├── activity-outcomes.md                   # Formal conceptual deliverables (concept, target user, features, mock-ups)
│   └── discussion-summary.md                  # Summary of group discussion & how LLMs supported ideation
└── screenshots/
    ├── 01-system-architecture.png             # Conceptual system architecture diagram
    ├── 02-ui-inventory-dashboard.png          # Pantry & expiry tracking UI mock-up
    ├── 03-ui-llm-recipe-assistant.png         # LLM recipe assistant UI mock-up
    ├── 04-ui-student-marketplace.png          # Campus surplus food marketplace UI mock-up
