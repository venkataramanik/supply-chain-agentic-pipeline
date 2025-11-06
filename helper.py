import os

def load_env():
    """Load environment variables for CrewAI from Codespaces secrets."""
    openai_key = os.getenv("OPENAI_API_KEY")
    serper_key = os.getenv("SERPER_API_KEY")

    if not openai_key:
        print("⚠️ Warning: OPENAI_API_KEY not found. Check Codespaces Secrets.")
    if not serper_key:
        print("⚠️ SERPER_API_KEY not found. (Only needed if using SerperDevTool)")

    # Optional: show confirmation (not the actual key)
    print("✅ Environment variables loaded securely from Codespaces.")
