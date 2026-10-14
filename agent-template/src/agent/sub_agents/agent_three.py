"""
Agent Three Module

This module defines Agent Three, the final agent in your three-step pipeline.
It takes outputs from both Agent One and Agent Two and creates the final result.

Key Concepts:
- Final Synthesis: Combining all previous work into a final output
- Multiple Dependencies: Using a custom model to pass multiple inputs
- Comprehensive Output: Creating the final user-facing result

Agent Three is the final step - it synthesizes everything!
"""

from pydantic_ai import Agent, RunContext
from pydantic import BaseModel
from src.agent.models import AgentOneOutput, AgentTwoOutput, AgentThreeOutput
from src.agent.constants import AGENT_THREE_PROMPT
from src.agent.llm import llm
from src.utils.debug import debug_log


class AgentThreeDeps(BaseModel):
    """
    Dependencies for Agent Three.
    
    Agent Three needs outputs from both previous agents.
    """
    agent_one_output: AgentOneOutput
    agent_two_output: AgentTwoOutput


# Create Agent Three
# - model: The LLM to use (configured in llm.py)
# - deps_type: Agent Three receives outputs from both previous agents
# - output_type: The structured output format (AgentThreeOutput)
# - retries: Number of times to retry if there's an error
# - system_prompt: Instructions for the agent's behavior
agent_three = Agent(
    model=llm,
    deps_type=AgentThreeDeps,
    output_type=AgentThreeOutput,
    retries=2,
    system_prompt=AGENT_THREE_PROMPT,
)


@agent_three.tool
def summarize_results(ctx: RunContext[AgentThreeDeps]) -> str:
    """
    An example tool that creates a summary of all previous work.
    
    Replace this with your own tools specific to your use case!
    
    Args:
        ctx: Run context (contains outputs from Agent One and Two)
    
    Returns:
        Summary text
    """
    deps = ctx.deps
    debug_log('[agent: "agent_three"] [tool-call: "summarize_results"] called')
    
    # Example: create a summary
    summary = (
        f"Agent One processed: {deps.agent_one_output.data}\n"
        f"Agent Two analyzed: {deps.agent_two_output.result}"
    )
    return summary


async def run_agent_three(
    agent_one_output: AgentOneOutput,
    agent_two_output: AgentTwoOutput
) -> AgentThreeOutput:
    """
    Run Agent Three with outputs from both previous agents.
    
    This is the main entry point for Agent Three. It synthesizes all previous work
    and creates the final output that will be shown to the user.
    
    Args:
        agent_one_output: The output from Agent One
        agent_two_output: The output from Agent Two
    
    Returns:
        AgentThreeOutput with the final result
    
    Example usage:
        >>> output = await run_agent_three(agent_one_output, agent_two_output)
        >>> print(output.final_output)
    """
    print("Running Agent Three...")
    debug_log('[agent: "agent_three"] Starting final synthesis')
    
    # Create dependencies object with both previous outputs
    deps = AgentThreeDeps(
        agent_one_output=agent_one_output,
        agent_two_output=agent_two_output
    )
    
    # Run the agent
    result = await agent_three.run(
        "Synthesize all information from Agent One and Agent Two. "
        "Create a comprehensive final output and summary.",
        deps=deps,
    )
    
    output = result.output
    debug_log('[agent: "agent_three"] Completed successfully')
    print("✅ Agent Three completed")
    
    return output

