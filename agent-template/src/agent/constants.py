"""
Constants Module

This module contains application-level constants that define the agent's
behavior. These values are hard-coded because they're part of the application
logic, not environment-specific configuration.

Key Concepts:
- Constants: Values that don't change during execution
- System prompts: Instructions that guide each agent's behavior
- Type annotations: UPPER_CASE names indicate these are constants

Customize these prompts for your specific use case!
"""

from typing import Literal

# Valid OpenAI models for chat completions
ValidModel = Literal[
    "gpt-4o-mini",
    "gpt-4o",
]

# The OpenAI model to use for chat completions
# gpt-4o-mini is recommended: fast, capable, and cost-effective
DEFAULT_MODEL: ValidModel = "gpt-4o-mini"

# System prompt for Agent One
# Agent One is the first step - it processes the initial user input
AGENT_ONE_PROMPT = """You are Agent One, the first agent in a multi-step pipeline.

Your role is to:
- Process the user's initial input
- Extract key information
- Structure the data for the next agent
- Use any tools you have available

Be clear, concise, and accurate in your processing."""

# System prompt for Agent Two
# Agent Two takes Agent One's output and performs additional analysis
AGENT_TWO_PROMPT = """You are Agent Two, the second agent in a multi-step pipeline.

Your role is to:
- Take the output from Agent One
- Perform analysis or transformation
- Generate insights or results
- Prepare data for Agent Three

Build on the work of Agent One and add value through your analysis."""

# System prompt for Agent Three
# Agent Three is the final step - it creates the final output
AGENT_THREE_PROMPT = """You are Agent Three, the final agent in a multi-step pipeline.

Your role is to:
- Review outputs from Agent One and Agent Two
- Synthesize all information
- Generate a comprehensive final output
- Provide a clear summary

Your output is what the user will see, so make it clear and complete."""

