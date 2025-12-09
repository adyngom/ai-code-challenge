
import streamlit as st
import os
import asyncio
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
load_dotenv('greeting_agent/.env')
load_dotenv('thoughtful_ai_agent/.env')

from google import genai
from google.genai import types

# Import agents
try:
    from greeting_agent.agent import root_agent as greeting_agent
    from thoughtful_ai_agent.agent import root_agent as thoughtful_agent
except ImportError as e:
    st.error(f"Failed to import agents: {e}")
    st.stop()

# Page Config
st.set_page_config(
    page_title="ADK Agents Demo",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .agent-card {
        padding: 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = {
        "Greeting Agent": [],
        "Thoughtful AI Agent": []
    }

# Sidebar
st.sidebar.title("🤖 Agent Selector")
selected_agent_name = st.sidebar.radio(
    "Choose an agent:",
    ["Greeting Agent", "Thoughtful AI Agent"]
)

agent_map = {
    "Greeting Agent": greeting_agent,
    "Thoughtful AI Agent": thoughtful_agent
}

current_agent = agent_map[selected_agent_name]

# Display Agent Info
st.markdown(f"""
<div class="agent-card">
    <h3>{selected_agent_name}</h3>
    <p>{current_agent.description if hasattr(current_agent, 'description') else 'No description'}</p>
</div>
""", unsafe_allow_html=True)

# Helper function to run agent using GenAI SDK directly
async def run_agent(agent, user_message, chat_history):
    """Run ADK agent with streaming response using direct GenAI SDK"""
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("GOOGLE_API_KEY not found in environment!")
        return

    client = genai.Client(api_key=api_key)

    # Build history for context
    # Note: mixing "user" and "model" roles
    history_content = []
    for msg in chat_history:
        role = "user" if msg["role"] == "user" else "model"
        history_content.append(types.Content(
            role=role,
            parts=[types.Part(text=msg["content"])]
        ))

    # Configuration
    # We map ADK agent properties to GenAI config
    tools = agent.tools if hasattr(agent, 'tools') else None
    instruction = agent.instruction if hasattr(agent, 'instruction') else None
    
    # Create the chat config
    
    chat = client.aio.chats.create(
        model=agent.model,
        history=history_content,
        config=types.GenerateContentConfig(
            system_instruction=instruction,
            tools=tools,
            temperature=0.3, # Default or from agent config if we parsed it
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
        )
    )

    # Send message and stream response
    
    response_stream = await chat.send_message_stream(user_message)

    full_response = ""
    message_placeholder = st.empty()
    
    # Status container to show "Thinking..." or tool activity if possible
    status_container = st.status("Agent is processing...", expanded=False)

    async for chunk in response_stream:
        # If we get text, show it
        if chunk.text:
            full_response += chunk.text
            message_placeholder.markdown(full_response)
            status_container.update(label="Responding...", state="running")
        
        # Check for function calls in the chunk (if exposed during auto-execution)
        
        if hasattr(chunk, 'function_calls') and chunk.function_calls:
             for fc in chunk.function_calls:
                 status_container.write(f"🛠️ Tool Used: `{fc.name}`")
    
    status_container.update(label="Complete", state="complete")
    return full_response

# Main Chat Loop
st.divider()

# Display Chat History
for msg in st.session_state.messages[selected_agent_name]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
if prompt := st.chat_input("Ask something..."):
    # 1. User Message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add to history *before* sending so it's included? 
    # No, typically we send current + history.
    # We'll append to storage now.
    st.session_state.messages[selected_agent_name].append(
        {"role": "user", "content": prompt}
    )

    # 2. Assistant Response
    with st.chat_message("assistant"):
        history_for_api = st.session_state.messages[selected_agent_name][:-1]
        
        response_text = asyncio.run(run_agent(current_agent, prompt, history_for_api))
        
        # 3. Save Response
        st.session_state.messages[selected_agent_name].append(
            {"role": "assistant", "content": response_text}
        )
