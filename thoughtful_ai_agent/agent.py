"""
Thoughtful AI Agent
Demonstrates Model Literacy and Hybrid Architecture with ADK.
"""

from google.adk import Agent
from .config import THOUGHTFUL_AGENT_CONFIG, THOUGHTFUL_AGENT_DESCRIPTION, THOUGHTFUL_AGENT_INSTRUCTION, THOUGHTFUL_AGENT_MODEL
from .tools import search_knowledge_base

root_agent = Agent(
    name="thoughtful_ai_agent",
    model=THOUGHTFUL_AGENT_MODEL,
    generate_content_config=THOUGHTFUL_AGENT_CONFIG,
    description=THOUGHTFUL_AGENT_DESCRIPTION,
    instruction=THOUGHTFUL_AGENT_INSTRUCTION,
    tools=[search_knowledge_base],
)
