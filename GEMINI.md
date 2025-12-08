# Project: adk-deep-dive-local

## Overview
This project is a local workspace for the "ADK Deep Dive" workshop, focusing on building AI agents using Google's Agent Development Kit (ADK) and FastAPI. It is structured as a series of steps/exercises to teach different agent patterns.

Currently, it contains **Step 1: Greeting Agent**, which demonstrates the foundational pattern of a single agent with custom Python tools.

## Key Components

### 1. `greeting_agent/`
This directory contains the first agent of the workshop.
*   **Pattern:** Single Agent with Custom Tools.
*   **Model:** `gemini-2.0-flash-exp`
*   **Files:**
    *   `agent.py`: Defines the `root_agent` using `google.adk.Agent`.
    *   `tools.py`: Contains custom tools (`get_company_info`, `get_current_time`, `get_class_roadmap`) as Python functions.
    *   `config.py`: Configuration for generation (temperature, safety settings) and prompts.

### 2. `main.py`
A simple entry point script. Currently just prints a greeting.

### 3. `pyproject.toml` & `uv.lock`
Defines the project dependencies and python version (>=3.12).
*   **Key Dependencies:** `fastapi`, `google-adk`, `google-generativeai`, `litellm`.
*   **Package Manager:** `uv`.

## Building and Running

### Prerequisites
*   Python 3.12+
*   `uv` package manager

### Setup
1.  **Install dependencies:**
    ```bash
    uv sync
    ```
2.  **Set API Key:**
    Ensure your `GOOGLE_API_KEY` is set in the environment or a `.env` file.

### Running the Greeting Agent
The `greeting_agent` is designed to be run with the `adk` CLI.

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
*Note: The ADK Web UI typically starts on port 3002.*

## Development Conventions

*   **Agent Structure:** Each agent is self-contained in its own directory (e.g., `greeting_agent/`) containing `agent.py`, `tools.py`, and `config.py`.
*   **Tools:** Tools are defined as standard Python functions with type hints and docstrings. The docstrings are critical as they provide the tool description to the model.
*   **Configuration:** Agent configuration (model, temperature, safety) is separated into `config.py`.
*   **Type Hints:** Extensive use of type hints (e.g., `dict`, `int`) is expected.
