"""
Custom tools for thoughtful_ai_agent.
Demonstrates Hybrid Architecture (Semantic Matching + LLM Fallback).
"""

import os
from google import genai
from typing import List, Dict, Optional, Tuple

# Predefined Q&A Dataset
QA_DATASET = [
    {
        "question": "What does the eligibility verification agent (EVA) do?",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "Tell me about EVA",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What is EVA?",
        "answer": "EVA automates the process of verifying a patient's eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
    },
    {
        "question": "What does the claims processing agent (CAM) do?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "Tell me about CAM",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "What is CAM?",
        "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
    },
    {
        "question": "How does the payment posting agent (PHIL) work?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about PHIL",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "What is PHIL?",
        "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
    },
    {
        "question": "Tell me about Thoughtful AI's Agents.",
        "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
    },
    {
        "question": "What are the benefits of using Thoughtful AI's agents?",
        "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
    }
]

# Cache for embeddings to avoid re-computing
_EMBEDDINGS_CACHE: Optional[List[Dict]] = None
_CLIENT: Optional[genai.Client] = None

def _get_client():
    global _CLIENT
    if _CLIENT is None:
        _CLIENT = genai.Client()
    return _CLIENT

def _get_embedding(text: str) -> List[float]:
    """Get embedding for text using Gemini."""
    client = _get_client()
    result = client.models.embed_content(
        model="text-embedding-004",
        contents=text
    )
    # Handle different response structures if needed, but this is standard
    return result.embeddings[0].values

def _cosine_similarity(v1: List[float], v2: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if not v1 or not v2 or len(v1) != len(v2):
        return 0.0
    
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude1 = sum(a * a for a in v1) ** 0.5
    magnitude2 = sum(b * b for b in v2) ** 0.5
    
    if magnitude1 * magnitude2 == 0:
        return 0.0
        
    return dot_product / (magnitude1 * magnitude2)

def _initialize_knowledge_base():
    """Lazy load and embed the knowledge base."""
    global _EMBEDDINGS_CACHE
    if _EMBEDDINGS_CACHE is not None:
        return

    print("Initializing knowledge base embeddings...")
    _EMBEDDINGS_CACHE = []
    for item in QA_DATASET:
        embedding = _get_embedding(item["question"])
        _EMBEDDINGS_CACHE.append({
            "question": item["question"],
            "answer": item["answer"],
            "embedding": embedding
        })
    print(f"Knowledge base initialized with {len(_EMBEDDINGS_CACHE)} items.")

def search_knowledge_base(query: str) -> str:
    """Search the Thoughtful AI knowledge base for answers about products (EVA, CAM, PHIL).

    This tool uses semantic matching to find precise answers from the verified Q&A dataset.
    ALWAYS use this tool first when asked about Thoughtful AI products, agents, or benefits.

    Args:
        query: The user's question or search query.

    Returns:
        str: The exact answer if a match is found (confidence > 0.8), or a message indicating no match.
    """
    try:
        _initialize_knowledge_base()
        
        query_embedding = _get_embedding(query)
        best_match = None
        best_score = 0.0
        
        for item in _EMBEDDINGS_CACHE:
            score = _cosine_similarity(query_embedding, item["embedding"])
            if score > best_score:
                best_score = score
                best_match = item["answer"]
        
        # Threshold from Thoughtful_AI strategy
        threshold = 0.70
        
        if best_score >= threshold:
            return f"[Match Found (Score: {best_score:.2f})] {best_match}"
        else:
            return f"[No High Confidence Match (Best Score: {best_score:.2f})] No exact match found in knowledge base."
            
    except Exception as e:
        return f"Error searching knowledge base: {str(e)}"
