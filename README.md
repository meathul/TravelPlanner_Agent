
#  Trip Planner Agent Workflow

**Built with CrewAI**
Plan your perfect getaway with the power of AI agents working in synergy! This intelligent workflow features specialized agents that collaborate to design a smart, data-driven, and personalized 7-day travel itinerary.

---

## Project Overview

This project leverages multiple autonomous agents to plan a trip from scratch. Each agent has a clearly defined role and utilizes real-time tools to gather information and make decisions.

### Agents in Action

* **Expert Travel Agent**
  Designs a detailed 7-day travel itinerary including:

  * Per-day plans
  * Estimated budget
  * Packing suggestions
  * Safety tips
    *Powered by GPT-4 + Tools (Search, Calculator)*

* **City Selection Expert**
  Analyzes travel trends, weather, seasonality, pricing, and preferences to select the best city for travel.
  *Powered by GPT-4 + Web Search*

* **Local Tour Guide**
  Acts as your on-ground AI guide with detailed insights into the chosen city’s:

  * Attractions
  * Local customs
  * Hidden gems
    *Powered by GPT-4 + Web Search*

---

##  Tech Stack

*  **CrewAI** — Multi-agent framework
*  **OpenAI GPT-3.5 & GPT-4** — Natural language agents
*  **SearchTools** — To fetch real-time web data
*  **CalculatorTools** — To calculate trip budgets
*  **Python 3.10+**

---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/trip-planner-ai.git
cd trip-planner-ai
```

### 2. Install Dependencies

Make sure you have [Poetry](https://python-poetry.org/) or pip environment ready:

```bash
poetry install
# or
pip install -r requirements.txt
```

### 3. Set up OpenAI API Keys

Export your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your_key_here
```

### 4. Run the Workflow

```bash
python run_trip_planner.py
```

---

##  Agent Class Blueprint

All agents are initialized in the `TravelAgents` class:

```python
TravelAgents().expert_travel_agent()
TravelAgents().city_selection_expert()
TravelAgents().local_tour_guide()
```

You can call these individually or orchestrate them via a Crew workflow.

---

## 📌 TODOs & Future Enhancements

* [ ] Add a User Preferences Agent
* [ ] Integrate a UI for city selection and results
* [ ] Include multi-city itinerary support
* [ ] Export results to PDF or shareable formats

---

##  Contribution

Pull requests are welcome! Feel free to suggest new agents, tools, or improvements.



##  Credits

Created  by Athul inspired from aiwithbrandon — Powered by GPT-4 & CrewAI.


