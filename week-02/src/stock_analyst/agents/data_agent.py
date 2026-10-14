"""
Data Agent Module

This module defines the Data Agent, which is responsible for fetching stock market data.
It uses Pydantic AI to create an intelligent agent that can retrieve and validate data.

Key Concepts:
- Pydantic AI Agent: An AI-powered agent that can use tools to accomplish tasks
- Tools: Functions that agents can call to interact with external systems
- Dependencies: Data that gets passed to the agent (in this case, the stock symbol)
- System Prompt: Instructions that guide the agent's behavior

The Data Agent is straightforward - it takes a stock symbol and fetches the data.
It validates that the symbol is correct and the data is complete.
"""

from pydantic_ai import Agent, RunContext
from src.stock_analyst.models import StockData
from src.stock_analyst.tools.stock_tools import fetch_stock_data
from src.stock_analyst.constants import DATA_AGENT_PROMPT
from src.stock_analyst.llm import llm
from src.utils.debug import debug_log


# Create the Data Agent
# - Model: We use OpenAI's GPT model (configured via settings)
# - deps_type: The type of dependency this agent expects (a stock symbol string)
# - retries: Number of times to retry if there's an error
# - We pass the API key from settings to ensure it's available
data_agent = Agent(
    model=llm,
    output_type=StockData,
    retries=2,
    system_prompt=DATA_AGENT_PROMPT,
)


@data_agent.tool
def get_stock_data(_: RunContext, symbol: str) -> StockData:
    """
    This tool fetches stock market data for a given symbol and period.

    Args:
        symbol: Valid, market-recognized stock ticker symbol (e.g., "AAPL") - NOTE: you may need to infer the symbol from the user's input

    Returns:
        StockData object with current and historical information
    """
    debug_log(f'[agent: "data_agent"] [tool-call: "get_stock_data"] called with symbol={symbol}')
    result = fetch_stock_data(symbol)
    return result

async def fetch_stock_data_with_agent(symbol: str) -> StockData:
    """
    High-level function to fetch stock data using the Data Agent.

    This is the main interface that other parts of the application use.
    It handles running the agent and returning the results.

    Args:
        symbol: Stock ticker symbol entered by the user (e.g., "AAPL")

    Returns:
        StockData object with all the information

    Raises:
        ValueError: If the symbol is invalid or data cannot be fetched

    Example usage:
        >>> data = await fetch_stock_data_with_agent("AAPL", "1mo")
        >>> print(f"Current price: ${data.current_price}")
    """
    print("Running Data Agent...")

    # Run the agent with the symbol as dependency
    result = await data_agent.run(
        f"Fetch stock market data for {symbol}. "
        f"Validate the symbol first, then retrieve the data.",
    )

    stock_data = result.output
    
    print("✅ Data Agent completed successfully")
    return stock_data

