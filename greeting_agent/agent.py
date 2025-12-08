"""
Greeting Agent - Step 1 of 9
Demonstrates basic ADK agent structure with custom Python function tools
"""

from google.adk import Agent
from .config import GREETING_AGENT_CONFIG, GREETING_AGENT_DESCRIPTION, GREETING_AGENT_INSTRUCTION, GREETING_AGENT_MODEL
from .tools import get_company_info, get_current_time, get_class_roadmap

root_agent = Agent(
    name="greeting_agent",
    model=GREETING_AGENT_MODEL,
    generate_content_config=GREETING_AGENT_CONFIG,
    description=GREETING_AGENT_DESCRIPTION,
    instruction=GREETING_AGENT_INSTRUCTION,
    tools=[get_company_info, get_current_time, get_class_roadmap],
)