"""
Research Agent Module

This module defines the Research Agent, which generates insights and recommendations.
It takes stock data and technical analysis, then creates human-friendly explanations
that help students understand what's happening with the stock.

Key Concepts:
- Educational Focus: Explanations are for learning, not financial advice
- Natural Language: The agent converts technical indicators into readable insights
- Context Awareness: Uses both data and analysis to provide comprehensive insights
- Structured Output: Returns a dictionary with recommendation and explanation

The Research Agent is the "communicator" - it takes technical information and
makes it accessible to beginners.
"""

from pydantic_ai import Agent, RunContext
from src.stock_analyst.models import StockData, TechnicalAnalysis, ResearchDependencies
from src.stock_analyst.constants import RESEARCH_AGENT_PROMPT
from src.stock_analyst.llm import llm
from src.utils.debug import debug_log


# This agent generates natural language insights and recommendations
research_agent = Agent(
    model=llm,
    deps_type=ResearchDependencies,  # Takes both StockData and TechnicalAnalysis
    retries=2,
    system_prompt=RESEARCH_AGENT_PROMPT,
)


@research_agent.tool
def get_stock_summary(ctx: RunContext[ResearchDependencies]) -> str:
    """
    Generate a concise summary of the stock's current state.

    This tool provides a quick overview of key metrics.

    Args:
        ctx: Run context with stock data and analysis

    Returns:
        Summary string with key information
    """
    data = ctx.deps.stock_data
    analysis = ctx.deps.analysis
    debug_log('[agent: "research_agent"] [tool-call: "get_stock_summary"]')
    # Format the summary
    summary = (
        f"{data.company_name} ({data.symbol}) is currently trading at ${data.current_price}, "
        f"{'' if data.price_change >= 0 else '-'}${abs(data.price_change)} "
        f"({'+' if data.price_change_percent >= 0 else ''}{data.price_change_percent}%) "
        f"from the previous close. "
        f"The technical analysis indicates a {analysis.trend_strength} {analysis.trend} trend "
        f"with {analysis.volatility} volatility."
    )

    return summary


@research_agent.tool
def get_key_metrics(ctx: RunContext[ResearchDependencies]) -> dict[str, str | float]:
    """
    Extract key metrics for the agent to reference.
    
    Args:
        ctx: Run context with stock data and analysis
    
    Returns:
        Dictionary of important metrics
    """
    data = ctx.deps.stock_data
    analysis = ctx.deps.analysis

    debug_log('[agent: "research_agent"] [tool-call: "get_key_metrics"]')
    
    metrics = {
        "symbol": data.symbol,
        "company": data.company_name,
        "current_price": data.current_price,
        "price_change_percent": data.price_change_percent,
        "trend": analysis.trend,
        "trend_strength": analysis.trend_strength,
        "volatility": analysis.volatility,
        "support_level": analysis.support_level or "Not determined",
        "resistance_level": analysis.resistance_level or "Not determined",
        "ma_20": analysis.moving_average_20 or "Not available",
        "ma_50": analysis.moving_average_50 or "Not available",
    }
    
    return metrics


@research_agent.tool
def generate_educational_notes(ctx: RunContext[ResearchDependencies]) -> list[str]:
    """
    Generate educational learning points based on the analysis.
    
    These help students understand key concepts demonstrated by this stock.
    
    Args:
        ctx: Run context with stock data and analysis
    
    Returns:
        List of educational notes
    """
    debug_log('[agent: "research_agent"] [tool-call: "generate_educational_notes"]')
    analysis = ctx.deps.analysis
    
    notes = []
    
    # Note about trends
    if analysis.trend == "bullish":
        notes.append(
            "Bullish Trend: When a stock shows an upward trend, it means prices have been "
            "generally increasing. This can indicate positive investor sentiment."
        )
    elif analysis.trend == "bearish":
        notes.append(
            "Bearish Trend: A downward trend means prices have been generally decreasing. "
            "This could indicate concerns about the company or broader market conditions."
        )
    else:
        notes.append(
            "Neutral Trend: When prices move sideways without clear direction, the market "
            "may be uncertain or waiting for new information."
        )
    
    # Note about volatility
    if analysis.volatility == "high":
        notes.append(
            "High Volatility: Large price swings can mean both higher risk and higher potential "
            "returns. Volatile stocks require careful consideration and risk management."
        )
    elif analysis.volatility == "low":
        notes.append(
            "Low Volatility: Stable price movements often indicate a mature, established company. "
            "Lower volatility typically means lower risk but also potentially lower returns."
        )
    
    # Note about moving averages
    if analysis.moving_average_20 and analysis.moving_average_50:
        notes.append(
            "Moving Averages: These indicators smooth out price fluctuations to reveal trends. "
            "The 20-day MA shows short-term trends, while the 50-day MA shows medium-term trends."
        )
    
    # Note about support and resistance
    if analysis.support_level and analysis.resistance_level:
        notes.append(
            "Support & Resistance: These are price levels where the stock tends to stop falling "
            "(support) or rising (resistance). They help identify potential entry and exit points."
        )
    
    return notes


async def generate_research_report(stock_data: StockData, analysis: TechnicalAnalysis) -> dict[str, str | list[str]]:
    """
    Generate a comprehensive research report with insights and recommendations.

    This is the main interface for getting research insights.
    It runs the Research Agent to produce human-friendly explanations.

    Args:
        stock_data: The stock market data
        analysis: The technical analysis results

    Returns:
        Dictionary with:
        - recommendation: Investment perspective (educational)
        - explanation: Detailed explanation for students
        - educational_notes: Key learning points

    Example usage:
        >>> data = await fetch_stock_data_with_agent("AAPL")
        >>> analysis = await analyze_stock(data)
        >>> report = await generate_research_report(data, analysis)
        >>> print(report["recommendation"])
    """
    print("Running Research Agent...")
    # Create dependencies object
    deps = ResearchDependencies(stock_data=stock_data, analysis=analysis)

    # Run the agent to generate insights
    result = await research_agent.run(
        f"Generate a comprehensive research report for {stock_data.symbol}. "
        f"Provide:\n"
        f"1. An educational investment perspective based on the technical analysis\n"
        f"2. A detailed explanation that helps students understand what's happening\n"
        f"3. Key learning points about investing concepts demonstrated here\n\n"
        f"Remember: This is for educational purposes only, not financial advice. "
        f"Use the available tools to get summaries and metrics.",
        deps=deps,
    )

    # Extract the response text
    # The agent returns natural language, which we'll structure into our report
    response_text = result.output

    # Parse the response into sections
    # For now, we'll use the whole response as the explanation
    # and generate recommendation and notes separately using tools

    # Create a simple recommendation based on the trend
    if analysis.trend == "bullish" and analysis.trend_strength in ["moderate", "strong"]:
        recommendation = (
            "Educational Perspective: This stock shows positive momentum. "
            "For learning purposes, observe how the trend develops and what factors might sustain it."
        )
    elif analysis.trend == "bearish" and analysis.trend_strength in ["moderate", "strong"]:
        recommendation = (
            "Educational Perspective: This stock is in a downtrend. "
            "Study what factors might be causing the decline and how long such trends typically last."
        )
    else:
        recommendation = (
            "Educational Perspective: This stock is showing mixed signals or consolidation. "
            "Watch for a clearer trend to develop before drawing conclusions."
        )

    recommendation += " Remember: This is not financial advice. Always do your own research."

    report = {
        "recommendation": recommendation,
        "explanation": response_text,
    }

    print("✅ Research Agent completed successfully")
    return report

