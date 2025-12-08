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

## 🚀 Getting Started

1.  **Prerequisites:** Ensure you have `python 3.12+` and `uv` installed.
2.  **Installation:**
    ```bash
    uv sync
    ```
3.  **Environment:** Set your `GOOGLE_API_KEY` in a `.env` file.
4.  **Run an Agent:**
    ```bash
    adk run greeting_agent
    ```

---
*Designed for the next generation of AI Engineers.*
