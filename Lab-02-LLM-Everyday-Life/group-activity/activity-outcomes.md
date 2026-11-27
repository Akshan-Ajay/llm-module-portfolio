# Activity Outcomes — Group 3: The Food Waster (*FoodLoop*)

> **Note on Scope:** For this lab activity, our group worked through idea selection, background thinking and research, conceptual architecture/UI mock-ups, presentation slides, and our live pitch. No production code was written or deployed as part of this lab.

---

## 1. Product Concept
**FoodLoop** is a conceptual mobile application designed to help university students reduce household and hostel food waste while connecting surplus or unused food with students looking for affordable options. Users can conceptually log food items (via photo, barcode scan, or manual entry), update consumption or waste, receive expiry/usage reminders, generate recipes from items they already have, use historical purchase-and-waste patterns to guide future buying quantities, and share or sell suitable extra food within a campus marketplace.

## 2. Product Name
**FoodLoop** — chosen to represent a continuous, low-waste cycle: tracking food from purchase to consumption or sharing so less edible food ends up in the bin.

## 3. Target User
* **Primary Target Users:** University students who buy or store groceries/meals and risk forgetting items, overbuying, or throwing away leftovers due to busy schedules or uncertainty about how to use them.
* **Secondary Target Users:** Students looking for budget-friendly, accessible surplus food or shared items within their university community.

## 4. Key Features (Conceptual Design)
* **Food Logging & Tracking:** Conceptual support for adding items via photo, barcode scan, or manual entry, and updating quantities as food is eaten or discarded.
* **Expiry & Unused-Item Reminders:** Alerts prompting students when stored items have been unused for a while or are approaching expiry.
* **LLM Recipe Suggestions:** Using a Large Language Model to suggest practical meals based on ingredients the user already has on hand.
* **Purchase & Waste Pattern Guidance (Random Forest Regressor):** Conceptually learning from a user's buy, use, and waste history (for example, suggesting buying 6–7 bananas next time instead of 10 if 6 were used and 4 were wasted) to help calibrate future shopping quantities.
* **Campus Food Sharing / Marketplace:** A conceptual space where users can share or sell suitable extra food at an affordable price so surplus food reaches someone who can use it.

## 5. Visual Prototype / Mock-ups & Presentation
During the lab, we created visual mock-ups and a system flow diagram and incorporated them into our presentation slides to illustrate:
* How user inputs flow through inventory tracking, food recognition, reminders, recipe/shopping suggestions, and marketplace sharing (`screenshots/01-system-architecture.png`).
* How the pantry view, AI recipe assistant, and campus marketplace could look in practice (`screenshots/02-ui-inventory-dashboard.png`, `screenshots/03-ui-llm-recipe-assistant.png`, `screenshots/04-ui-student-marketplace.png`).