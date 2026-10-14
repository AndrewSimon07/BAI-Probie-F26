from textwrap import dedent

RAG_AGENT_SYSTEM_PROMPT = dedent("""
    TODO: Write a concise system prompt that:
    - States the agent answers questions using a vector database of user data
    - Requires grounding answers strictly in retrieved facts
    - Mentions the `perform_rag` tool and when to use it
    - Instructs to say "I don't know" if facts are insufficient
    """)
