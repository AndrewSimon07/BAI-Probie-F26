# Stock Market Analyst - AI-Powered Analysis

Welcome to week 2! In this assignment, you'll explore an advanced multi-agent system built with **Pydantic AI**. You'll learn about agent-based architectures, AI tool usage, and how specialized agents can collaborate to solve complex problems.

**Estimated Time**: 2-3 hours (reading, understanding, and experimenting)

## 📚 Learning Objectives

By exploring this project, you will learn:

1. **Agent-Based Architecture**: How to design systems with specialized AI agents
2. **Pydantic AI Framework**: Using modern AI frameworks for production applications
3. **Tool Functions**: How agents use tools to interact with external APIs
4. **Structured Outputs**: Ensuring AI responses follow specific data models
5. **Async Programming**: Working with asynchronous Python code
6. **Multi-Agent Orchestration**: Coordinating multiple agents to accomplish complex tasks
7. **Type Safety**: Using Pydantic models for data validation throughout the system

## 🏗️ System Architecture

This application uses a **three-agent architecture**, where each agent has a specialized role:

### 1. Data Agent 📊
**Responsibility**: Fetches stock market data from Yahoo Finance

**Tools**:
- `get_stock_data()`: Retrieves current and historical stock data
- `validate_stock_symbol()`: Validates and normalizes ticker symbols

**Input**: Stock symbol (e.g., "AAPL")  
**Output**: `StockData` model with prices, volume, market cap, etc.

### 2. Analysis Agent 🔍
**Responsibility**: Performs technical analysis on stock data

**Tools**:
- `calculate_ma_20()`: Calculates 20-day moving average
- `calculate_ma_50()`: Calculates 50-day moving average
- `get_support_and_resistance()`: Identifies key price levels
- `assess_volatility()`: Evaluates price volatility
- `get_overall_price_change()`: Calculates period change percentage

**Input**: `StockData` model  
**Output**: `TechnicalAnalysis` model with trend, indicators, and summary

### 3. Research Agent 💡
**Responsibility**: Generates educational insights and recommendations

**Tools**:
- `get_stock_summary()`: Creates concise overview
- `get_key_metrics()`: Extracts important metrics
- `generate_educational_notes()`: Produces learning points

**Input**: `StockData` + `TechnicalAnalysis` models  
**Output**: Recommendations, explanations, and educational notes

### Agent Workflow

```
User Input (Stock Symbol)
        ↓
    Data Agent → StockData
        ↓
    Analysis Agent → TechnicalAnalysis
        ↓
    Research Agent → Insights & Recommendations
        ↓
    Beautiful Report Display
```

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.12 or higher** installed ([download here](https://www.python.org/downloads/))
- **OpenAI API Key** (available on the BAI Probie GitHub homepage)

## 🚀 Setup Instructions

### Step 1: Install uv

`uv` is a super fast Python package installer and resolver.

**On macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**On Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv --version
```

### Step 2: Navigate to Project Directory

```bash
cd assignments/week-02
```

### Step 3: Create Virtual Environment

```bash
uv venv
```

Activate it:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```powershell
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
uv sync
```

This installs:
- `pydantic-ai`: AI agent framework
- `openai`: OpenAI API client
- `pydantic`: Data validation
- `pydantic-settings`: Settings management
- `yfinance`: Yahoo Finance API wrapper
- `rich`: Beautiful terminal formatting

### Step 5: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in your editor and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
   ```

3. **Never commit `.env` to git!** (It's already in `.gitignore`)

## 📁 Project Structure

```
week-02/
├── src/
│   ├── settings.py              # ✅ Environment configuration
│   ├── stock_analyst/
│   │   ├── constants.py         # ✅ Application constants & prompts
│   │   ├── models.py            # ✅ Pydantic data models
│   │   ├── ui.py                # ✅ Rich terminal UI functions
│   │   ├── main.py              # ✅ Main CLI orchestrator
│   │   ├── agents/
│   │   │   ├── data_agent.py    # ✅ Data fetching agent
│   │   │   ├── analysis_agent.py # ✅ Technical analysis agent
│   │   │   └── research_agent.py # ✅ Research insights agent
│   │   └── tools/
│   │       └── stock_tools.py   # ✅ Helper functions for agents
│   └── utils/
│       └── filesystem.py        # ✅ Utility functions
├── pyproject.toml               # Project dependencies
├── .env.example                 # Environment template
├── .env                         # Your secrets (don't commit!)
└── README.md                    # This file
```

**All files are complete** - this is a reference implementation to study!

## 💻 Running the Application

Once you've completed setup, run the stock analyst:

```bash
uv run python -m src.stock_analyst.main
```

**Expected behavior**:
1. Welcome banner appears with example stocks
2. You can enter stock symbols (e.g., AAPL, GOOGL, TSLA)
3. The system fetches data, analyzes trends, and generates insights
4. A beautiful report is displayed with:
   - Current price and market data
   - Recent price history
   - Technical analysis (trend, indicators, levels)
   - Research insights and recommendations
   - Educational learning points
5. You can analyze another stock or quit
6. Type `quit`, `exit`, or `bye` to end

## 🧪 Example Usage

```
Enter stock symbol: AAPL

⏳ Fetching stock data...
⏳ Analyzing market trends...
⏳ Generating insights...

======================================================================

╭─────────────────────────────────────────────────────────────────╮
│ Apple Inc. (AAPL)                                               │
│                                                                 │
│ $175.43  ↑ $2.15 (+1.24%)                                      │
│                                                                 │
│ Market Cap: $2.75T | Volume: 52,043,890 | Period: 1mo         │
╰─────────────────────────────────────────────────────────────────╯

[Price chart and technical analysis displayed...]

Analyze another stock? (y/n) [y]:
```

## 🎓 Key Concepts to Study

### 1. Pydantic AI Agents

Agents are created with:
```python
agent = Agent(
    'openai:gpt-4o-mini',           # Model to use
    deps_type=str,                   # Type of dependencies
    result_type=TechnicalAnalysis,   # Structured output type (optional)
    system_prompt=AGENT_PROMPT,      # Instructions for the agent
)
```

### 2. Agent Tools

Tools are functions that agents can call:
```python
@agent.tool
def my_tool(ctx: RunContext[DepsType]) -> ReturnType:
    """Tool description for the AI."""
    # Access dependencies via ctx.deps
    # Return results to the agent
```

### 3. Running Agents

Agents are run asynchronously:
```python
result = await agent.run(
    "Your instruction to the agent",
    deps=dependency_data,
)
# Access the result via result.data
```

### 4. Structured Outputs

When `result_type` is specified, the agent returns a Pydantic model:
```python
analysis_agent = Agent(
    'openai:gpt-4o-mini',
    result_type=TechnicalAnalysis,  # Agent MUST return this type
)
# The agent will structure its response to match TechnicalAnalysis
```

### 5. Multi-Agent Coordination

Agents work together in sequence:
```python
# Agent 1: Fetch data
data = await data_agent.run("Get stock data", deps=symbol)

# Agent 2: Analyze (uses Agent 1's output)
analysis = await analysis_agent.run("Analyze trends", deps=data)

# Agent 3: Research (uses both previous outputs)
insights = await research_agent.run("Generate insights", deps=(data, analysis))
```

## 🔬 Experiments to Try

1. **Add a new stock symbol**: Try analyzing different stocks (tech, retail, finance)

2. **Change the time period**: Modify the code to analyze different periods (1y, 6mo, etc.)

3. **Add a new tool**: Create a tool that calculates RSI (Relative Strength Index)

4. **Create a new agent**: Build a "News Agent" that fetches recent news articles

5. **Modify prompts**: Edit the system prompts in `constants.py` to change agent behavior

6. **Add more indicators**: Implement MACD, Bollinger Bands, or other technical indicators

## 🎯 Advanced Challenges

For students who want to dive deeper:

1. **Portfolio Agent**: Create an agent that analyzes multiple stocks together

2. **Comparison Agent**: Build an agent that compares two stocks side-by-side

3. **Alert System**: Add functionality to set price alerts and track them

4. **Historical Backtesting**: Test trading strategies against historical data

5. **Sentiment Analysis**: Integrate news sentiment into the analysis

6. **Database Integration**: Store analysis results in a database for tracking

## 🔍 Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting.

Check your code:
```bash
uvx ruff check   # Lint all files
uvx ruff format  # Format all files
```

## ⚠️ Important Notes

### This is NOT Financial Advice

This tool is built for **educational purposes only**. It demonstrates AI agent architecture and technical analysis concepts. Never make investment decisions based solely on automated analysis. Always:
- Do your own research
- Consult with financial professionals
- Understand the risks of investing
- Only invest what you can afford to lose

### API Rate Limits

- Yahoo Finance API is free but has rate limits
- OpenAI API calls cost money (check your usage at platform.openai.com)
- The shared API key has usage limits

### Data Accuracy

- Stock data is provided "as is" from Yahoo Finance
- Historical data may have gaps or inaccuracies
- Real-time data may be delayed by 15 minutes

## 📚 Additional Resources

- **Pydantic AI Docs**: [ai.pydantic.dev](https://ai.pydantic.dev)
- **Pydantic Documentation**: [docs.pydantic.dev](https://docs.pydantic.dev)
- **Yahoo Finance**: [finance.yahoo.com](https://finance.yahoo.com)
- **Rich Library**: [rich.readthedocs.io](https://rich.readthedocs.io)
- **Technical Analysis**: [Investopedia](https://www.investopedia.com/terms/t/technicalanalysis.asp)
- **OpenAI API**: [platform.openai.com/docs](https://platform.openai.com/docs)

## 🤝 Getting Help

**Questions or issues?** 
- Review the code comments - they're very detailed!
- Check the Pydantic AI documentation
- Open an issue on the course repository
- Contact the instructors

## 🎉 What's Next?

After understanding this system:
1. Experiment with different stocks and time periods
2. Read through each module to understand the architecture
3. Try implementing one of the advanced challenges
4. Share your insights and learnings with the cohort

**Happy learning, and remember: invest in your education first!** 📚✨

