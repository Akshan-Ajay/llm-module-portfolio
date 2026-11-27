# PUSL 3205 – Large Language Models and Generative AI
## Lab 02: AI in Everyday Challenges — *FoodLoop* (Group 3: The Food Waster)

> **Lab Scope Note:** This lab focused on critical thinking, problem framing, research, using an LLM as a product-development brainstorming partner, designing conceptual UI/architecture mock-ups, creating presentation slides, and delivering a 2–3 minute group pitch. No production code or live software deployment was carried out for this activity.

---

## 1. Lab Objective & Assigned Challenge

The objective of **Lab 02** was to apply Large Language Models (LLMs) to an everyday challenge faced by university students—developing critical thinking, problem-solving, and creative design skills while exploring how AI can be applied to real-world situations.

### Group 3 — The Food Waster
University students often buy more food than they can eat, forget perishable items they have stored, or discard leftovers because they do not know what to make with them. At the same time, other students on campus are looking for affordable food options. Our goal was to use an LLM as a product-development partner to conceptualize an innovative product or service that reduces unnecessary student food waste.

---

## 2. Group Members

| Name | Student ID | Key Contributions |
| :--- | :--- | :--- |
| **Suthakaran Akshan** | 10967118 | Problem framing, LLM brainstorming & prompt design, system/feature conceptualisation, slide preparation, and presentation |
| **Wcn Coonghe** | 10965216 | Research on student food waste & campus sharing ideas, feature/workflow refinement, slide preparation, and presentation |
| **Nishovithan** | 10965286 | Concept evaluation, user journey & scenario thinking, slide preparation, and presentation |

---

## 3. What We Did During the Lab Session

1. **Idea Selection & Problem Exploration:** Analyzed why students overbuy groceries or waste leftovers in hostels/shared housing and identified the dual opportunity to connect surplus food with budget-conscious peers.
2. **LLM-Assisted Ideation & Scoping:** Used an LLM as a brainstorming partner to refine features, define student constraints (limited dorm cooking equipment, tight budgets, short prep times), and structure a cohesive product concept (**FoodLoop**).
3. **Conceptual Architecture & AI Role Separation:** Mapped out how data moves through the proposed system and clearly separated responsibilities between different AI approaches:
   * **Food Recognition (Vision / Barcode):** Conceptual item and quantity logging via photo, barcode scan, or manual entry.
   * **Random Forest Regressor (Proposed Tabular ML):** Learns from a user's historical purchase, usage, and waste logs to recommend realistic buying quantities on future shopping trips.
   * **LLM Assistant (Generative AI):** Suggests practical meals from ingredients the user already has on hand and assists with clear marketplace listings.
4. **Visual Mock-ups & Presentation Slides:** Designed a system architecture diagram and mobile UI mock-ups, compiled the solution into a slide deck, and delivered a 2–3 minute group presentation.

---

## 4. Product Concept Overview: FoodLoop

**FoodLoop** is a conceptual mobile application designed to help students track the food they buy, use, and waste, turn expiring ingredients into practical meals, optimize future grocery quantities, and share or sell suitable surplus food within a campus marketplace.

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
