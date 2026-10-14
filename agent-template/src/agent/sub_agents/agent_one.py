"""
Agent One Module

This module defines Agent One, the first agent in your three-step pipeline.
It uses Pydantic AI to create an intelligent agent that processes user input.

Key Concepts:
- Pydantic AI Agent: An AI-powered agent that can use tools to accomplish tasks
- Tools: Functions that agents can call to perform specific operations
- System Prompt: Instructions that guide the agent's behavior
- Structured Output: Using output_type to ensure consistent output format

Agent One is the first step - customize it for your specific use case!
"""

from pydantic_ai import Agent, RunContext
from src.agent.models import AgentOneOutput
from src.agent.constants import AGENT_ONE_PROMPT
from src.agent.llm import llm
from src.utils.debug import debug_log
from datetime import datetime


# Create Agent One
# - model: The LLM to use (configured in llm.py)
# - output_type: The structured output format (AgentOneOutput)
# - retries: Number of times to retry if there's an error
# - system_prompt: Instructions for the agent's behavior
agent_one = Agent(
    model=llm,
    output_type=AgentOneOutput,
    retries=2,
    system_prompt=AGENT_ONE_PROMPT,
)


@agent_one.tool
def get_current_time(ctx: RunContext) -> str:
    """
    An example tool that Agent One can use.
    
    Replace this with your own tools specific to your use case!
    
    Args:
        ctx: Run context (contains the user input as deps)
        text: Text to process
    
    Returns:
        Processed text
    """
    debug_log('[agent: "agent_one"] [tool-call: "get_current_time"] called')
    # Example: convert to uppercase
    return datetime.now().isoformat()


async def run_agent_one(user_input: str) -> AgentOneOutput:
    """
    Run Agent One with the user's input.
    
    This is the main entry point for Agent One. It processes the user's input
    and returns structured output that can be passed to Agent Two.
    
    Args:
        user_input: The user's input to process
    
    Returns:
        AgentOneOutput with processed data
    
    Example usage:
        >>> output = await run_agent_one("Hello world")
        >>> print(output.data)
    """
    print("Running Agent One...")
    debug_log(f'[agent: "agent_one"] Starting with input: {user_input[:50]}...')
    
    # Run the agent with the user input
    result = await agent_one.run(
        f"Process this input: {user_input}",
    )
    
    output = result.output
    debug_log('[agent: "agent_one"] Completed successfully')
    print("✅ Agent One completed")
    
    return output

