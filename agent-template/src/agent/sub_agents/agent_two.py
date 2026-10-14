"""
Agent Two Module

This module defines Agent Two, the second agent in your three-step pipeline.
It takes the output from Agent One and performs additional processing.

Key Concepts:
- Chaining Agents: Taking output from one agent as input to another
- Dependencies: Using deps_type to specify what data this agent needs
- Tools: Functions specific to Agent Two's processing tasks

Agent Two builds on Agent One's work - customize it for your use case!
"""

from pydantic_ai import Agent, RunContext
from src.agent.models import AgentOneOutput, AgentTwoOutput
from src.agent.constants import AGENT_TWO_PROMPT
from src.agent.llm import llm
from src.utils.debug import debug_log


# Create Agent Two
# - model: The LLM to use (configured in llm.py)
# - deps_type: Agent Two receives AgentOneOutput as its dependency
# - output_type: The structured output format (AgentTwoOutput)
# - retries: Number of times to retry if there's an error
# - system_prompt: Instructions for the agent's behavior
agent_two = Agent(
    model=llm,
    deps_type=AgentOneOutput,
    output_type=AgentTwoOutput,
    retries=2,
    system_prompt=AGENT_TWO_PROMPT,
)


@agent_two.tool
def analyze_data(ctx: RunContext[AgentOneOutput]) -> str:
    """
    An example tool that analyzes data from Agent One.
    
    Replace this with your own tools specific to your use case!
    
    Args:
        ctx: Run context (contains AgentOneOutput as deps)
    
    Returns:
        Analysis result
    """
    agent_one_output = ctx.deps
    debug_log('[agent: "agent_two"] [tool-call: "analyze_data"] called')
    
    # Example: analyze the data from Agent One
    analysis = f"Analyzed: {agent_one_output.data} (length: {len(agent_one_output.data)})"
    return analysis


async def run_agent_two(agent_one_output: AgentOneOutput) -> AgentTwoOutput:
    """
    Run Agent Two with Agent One's output.
    
    This is the main entry point for Agent Two. It takes Agent One's output,
    performs additional processing, and returns structured output for Agent Three.
    
    Args:
        agent_one_output: The output from Agent One
    
    Returns:
        AgentTwoOutput with processed results
    
    Example usage:
        >>> output = await run_agent_two(agent_one_output)
        >>> print(output.result)
    """
    print("Running Agent Two...")
    debug_log('[agent: "agent_two"] Starting with Agent One output')
    
    # Run the agent with Agent One's output as dependency
    result = await agent_two.run(
        "Analyze and process the data from Agent One. Generate insights and results.",
        deps=agent_one_output,
    )
    
    output = result.output
    debug_log('[agent: "agent_two"] Completed successfully')
    print("✅ Agent Two completed")
    
    return output

