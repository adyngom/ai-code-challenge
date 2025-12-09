"""
Agent prompts and configuration for the Thoughtful AI agent.
Demonstrates Model Literacy and Configuration Rationale.
"""

from google.genai import types
from google.genai.types import GenerateContentConfig
from google.genai.types import SafetySetting

class ThoughtfulAIConfig(GenerateContentConfig):
    # Rationale: 300 allows elaboration without rambling (Cost Consciousness)
    max_output_tokens: int = 300
    # Rationale: 0.3 is the sweet spot for professional + accurate healthcare support
    temperature: float = 0.3
    safety_settings: list[SafetySetting] = [
        SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
        SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        ),
    ]

# Rationale: Gemini 2.0 Flash is 500x cheaper than GPT-4, fast, and sufficient for this task.
THOUGHTFUL_AGENT_MODEL: str = "gemini-2.0-flash-exp"

THOUGHTFUL_AGENT_CONFIG = ThoughtfulAIConfig()

THOUGHTFUL_AGENT_DESCRIPTION: str = (
    "A healthcare support agent demonstrating model literacy and production principles."
)

THOUGHTFUL_AGENT_INSTRUCTION: str = """You are a customer support agent for Thoughtful AI, 
a healthcare automation company.

Our products:
- EVA (Eligibility Verification Agent): Automates patient eligibility verification
- CAM (Claims Processing Agent): Streamlines claims submission and management
- PHIL (Payment Posting Agent): Automates payment posting and reconciliation

Guidelines:
- ALWAYS check the knowledge base using the `search_knowledge_base` tool first.
- Be helpful, professional, and concise.
- Keep responses under 150 words.
- If you don't know specific product details and the knowledge base doesn't help, acknowledge it.
- For healthcare-specific questions, remind users to consult medical professionals.
- Focus on our automation products, not medical advice.

Remember: We're a healthcare automation company, not medical providers.
"""
