# ADK Deep Dive: Zero to Mastery in Multi-Agent Systems

Welcome to the official workspace for the **ADK Deep Dive Master Class**.

## 👨‍🏫 About the Author
**Ady** is a Google Developer Expert (GDE) in Angular with a deep passion for AI and Machine Learning that has spanned the last five years. Merging a background in robust enterprise web development with cutting-edge AI, Ady has designed this master class to bridge the gap between theory and production.

This curriculum has been taught to **over 500 students**, helping developers transition from basic prompting to architecting complex, autonomous systems.

## 🎯 Goals & Objectives
The primary goal of this repository is to demonstrate **enterprise-level best practices** for the Google Agent Development Kit (ADK). We aim to move beyond simple prototypes and focus on:

*   **Zero to Mastery:** A structured learning path from your first agent to complex orchestration.
*   **Production Patterns:** implementing reliable, testable, and scalable agent architectures.
*   **Multi-Agent Orchestration:** Learning how to coordinate multiple agents (Sequential, Parallel, Hierarchical) to solve real-world problems.
*   **ADK Fundamentals:** Deep understanding of tools, configuration, and state management within the ADK framework.

## 🗺️ The Journey
This project uses a "learn by doing" approach, evolving through 4 distinct phases and 9 specialized agents:

### Phase 1: Foundation 🏗️
*   **Greeting Agent:** Master the basics—single agent configuration, custom tool definitions, and environment setup. *(Current Step)*

### Phase 2: Real Workflows 🔄
*   **Customer Service:** Implement sequential logic and state hand-offs.
*   **Content Pipeline:** Build automation chains for generating and refining content.
*   **Medical Authorization:** Handle strict constraints and domain-specific knowledge.

### Phase 3: Intelligent Decision-Making 🧠
*   **Financial Advisor:** leverage parallel processing for complex data analysis.
*   **Brand Intelligence:** Synthesize information from multiple sources.

### Phase 4: Production-Grade Systems 🚀
*   **Software Assistant:** Technical problem solving and code generation.
*   **Project Management:** Coordination, planning, and task tracking.
*   **Verified Recommendations:** Advanced architectures with verification layers for high-stakes decisions.

## 🛠️ Tech Stack
*   **Google ADK (Agent Development Kit)**
*   **Google Gemini Models** (Pro, Flash, Flash-Exp)
*   **FastAPI**
*   **Python 3.12+**

## 🚀 Getting Started on IDX

1.  **Set Your API Key:** This project uses an agent-centric configuration. Before you begin, you will need to create a `.env` file inside of each agent folder (e.g. `greeting_agent/` and `thoughtful_ai_agent/`). You can do this by running the following commands in the terminal:

    ```bash
    cp greeting_agent/.env.template greeting_agent/.env
    cp thoughtful_ai_agent/.env.template thoughtful_ai_agent/.env
    ```

    Then, open the newly created `.env` files and paste in your API key.

2.  **Launch the Services:** Run the following command in your terminal to start the ADK Web and Streamlit UIs:

    ```bash
    .idx/start-services.sh
    ```

3.  **Access the UIs:** Once the services are running, you can access them at the following ports:

    *   **Streamlit UI:** Port 8501
    *   **ADK Web UI:** Port 8000

## 🚀 Getting Started (Manual)

1.  **Prerequisites:** Ensure you have `python 3.12+` and `uv` installed.
2.  **Installation:**

    ```bash
    uv sync
    ```

3.  **Environment:** Set your `GOOGLE_API_KEY` in a `.env` file in each agent's directory.
4.  **View and debug all agents:**

    ```bash
    adk web
    ```

5.  **Run one agent:**

**Using ADK CLI:**

```bash
# Run via the ADK command line interface
adk run greeting_agent
```

**Using ADK Web UI:**

```bash
# Launch the web interface for testing
adk web
```

*Note: The ADK Web UI typically starts on port 8000.*

**Using the Streamlit Interface:**

```bash
# Run the Streamlit app for interaction
uv run streamlit run streamlit_app.py
```

*Note: The Streamlit Web UI typically starts on port 8501.*

---

*Designed for the next generation of AI Engineers.*
