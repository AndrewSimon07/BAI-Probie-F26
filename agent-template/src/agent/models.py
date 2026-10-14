"""
Data Models Module

This module defines the data structures used throughout your agent application.
We use Pydantic models to ensure all data is valid and type-safe.

Key Concepts:
- Pydantic models: Classes that automatically validate data
- Type hints: Declaring what type each field should be
- Optional fields: Fields that can be None (using | None)

Why use models?
- Catch errors early (before processing bad data)
- Self-documenting code (clear what data looks like)
- IDE support (autocomplete and type checking)
- Type safety: Prevent invalid data from being created
"""

from pydantic import BaseModel, Field
from datetime import datetime


class AgentOneOutput(BaseModel):
    """
    Output from Agent One.
    
    Agent One is the first step in the pipeline. It processes the initial user input
    and produces structured data for the next agent.
    
    Customize this model for your use case!
    """
    
    data: str = Field(description="Processed data from Agent One")
    metadata: dict[str, str] = Field(
        default_factory=dict,
        description="Optional metadata"
    )


class AgentTwoOutput(BaseModel):
    """
    Output from Agent Two.
    
    Agent Two takes Agent One's output and performs additional processing.
    
    Customize this model for your use case!
    """
    
    result: str = Field(description="Processed result from Agent Two")
    analysis: str = Field(description="Analysis or insights")


class AgentThreeOutput(BaseModel):
    """
    Output from Agent Three.
    
    Agent Three is the final step. It combines outputs from previous agents
    and produces the final result.
    
    Customize this model for your use case!
    """
    
    final_output: str = Field(description="Final processed output")
    summary: str = Field(description="Summary of all agent work")


class FinalReport(BaseModel):
    """
    The complete final report combining all agent outputs.
    
    This is what gets displayed to the user.
    """
    
    user_input: str = Field(description="The original user input")
    generated_at: str = Field(
        default_factory=lambda: datetime.now().isoformat(),
        description="ISO timestamp when report was generated"
    )
    agent_one_output: AgentOneOutput
    agent_two_output: AgentTwoOutput
    agent_three_output: AgentThreeOutput
    