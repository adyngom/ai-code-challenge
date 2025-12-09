#!/bin/bash
# ADK Deep Dive Services Startup Script
# Starts services needed for the ADK Deep Dive project.

set -e

echo "🚀 Starting ADK Deep Dive Services..."

# Activate virtual environment
if [ -d ".venv" ]; then
    source .venv/bin/activate
    echo "✅ Virtual environment activated"
else
    echo "❌ Virtual environment not found. Please run 'uv sync' first."
    exit 1
fi

# Check for API key
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found."
    echo "📝 Please create a .env file and add your GOOGLE_API_KEY."
    echo "Example: GOOGLE_API_KEY=AIza..."
    exit 1
fi

# Verify API key is set
if ! grep -q "GOOGLE_API_KEY" .env; then
    echo "⚠️  GOOGLE_API_KEY not configured in .env"
    echo "Please add your API key from https://aistudio.google.com/apikey"
    exit 1
fi

echo "🔍 Starting ADK Web on port 8000..."
uv run adk web --host 0.0.0.0 --port 8000 > /tmp/adk-web.log 2>&1 &
ADK_PID=$!
echo "   ADK Web PID: $ADK_PID"
sleep 2

# Start Streamlit UI
echo "🎨 Starting Streamlit UI on port 8501..."
uv run streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0 --server.enableCORS=false --server.enableXsrfProtection=false > /tmp/streamlit.log 2>&1 &
STREAMLIT_PID=$!
echo "   Streamlit PID: $STREAMLIT_PID"

echo ""
echo "✅ All services started successfully!"
echo ""
echo "📍 Access your interfaces:"
echo "   🎨 Streamlit UI: Port 8501"
echo "   🔍 ADK Web:      Port 8000 (Debugging)"
echo ""
echo "📝 Service PIDs:"
echo "   Streamlit: $STREAMLIT_PID"
echo "   ADK Web: $ADK_PID"
echo ""
echo "📊 View logs:"
echo "   tail -f /tmp/streamlit.log"
echo "   tail -f /tmp/adk-web.log"
echo ""
echo "🛑 Stop services:"
echo "   kill $STREAMLIT_PID $ADK_PID"
