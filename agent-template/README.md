# Multi-Agent Template with Pydantic AI

A clean, simple template for building three-step multi-agent applications using **Pydantic AI**. This template provides a solid foundation that students can easily customize and extend for their own agent-based projects.

## 📚 What You'll Learn

By working with this template, you'll understand:

1. **Multi-Agent Architecture**: How to design systems with specialized AI agents
2. **Agent Orchestration**: Coordinating multiple agents in a sequential pipeline
3. **Pydantic AI Framework**: Using modern AI frameworks for production applications
4. **Tool Functions**: How agents use tools to accomplish specific tasks
5. **Structured Outputs**: Ensuring AI responses follow specific data models
6. **Async Programming**: Working with asynchronous Python code

## 🏗️ Architecture Overview

This template implements a **three-agent pipeline** where each agent has a specific role:

```
User Input
    ↓
Agent One (Process Input)
    ↓
Agent Two (Analyze/Transform)
    ↓
Agent Three (Synthesize Final Output)
    ↓
Display Final Report
```

### Agent Responsibilities

- **Agent One**: Processes the initial user input and structures data for the next agent
- **Agent Two**: Takes Agent One's output and performs analysis or transformation
- **Agent Three**: Synthesizes all previous work into a comprehensive final result

## 📋 Prerequisites

- **Python 3.12 or higher**
- **OpenAI API Key** (get from course materials or [OpenAI](https://platform.openai.com/))

## 🚀 Quick Start

### 1. Install UV (Package Manager)

UV is a fast Python package installer and resolver.

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:
```bash
uv --version
```

### 2. Set Up Project

```bash
# Navigate to template directory
cd agent-template

# Create virtual environment
uv venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
uv sync
```

### 3. Configure Environment

Create a `.env` file with your OpenAI API key:

```bash
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
```

**Important:** Never commit `.env` to git! It's already in `.gitignore`.

### 4. Run the Template

```bash
uv run python -m src.agent.main
```

You should see a welcome message and be able to enter text that gets processed through all three agents.

## 📁 Project Structure

```
agent-template/
├── src/
│   ├── agent/
│   │   ├── constants.py          # Agent prompts and configuration
│   │   ├── models.py             # Pydantic data models
│   │   ├── llm.py                # LLM configuration
│   │   ├── ui.py                 # Terminal UI functions
│   │   ├── main.py               # Main orchestration logic
│   │   ├── sub-agents/
│   │   │   ├── agent_one.py      # First agent
│   │   │   ├── agent_two.py      # Second agent
│   │   │   └── agent_three.py    # Third agent
│   │   └── tools/
│   │       └── example_tools.py  # Example helper functions
│   ├── settings.py               # Environment configuration
│   └── utils/
│       ├── debug.py              # Debug utilities
│       └── filesystem.py         # File utilities
├── pyproject.toml                # Project dependencies
├── .env                          # Your API key (don't commit!)
└── README.md                     # This file
```

## 🎓 Key Concepts

### 1. Creating Agents

Agents are created with specific configurations:

```python
agent = Agent(
    model=llm,                    # The LLM to use
    output_type=YourModel,        # Structured output type
    deps_type=InputType,          # What dependencies it needs
    system_prompt="...",          # Instructions for behavior
    retries=2,                    # Error retry attempts
)
```

### 2. Agent Tools

Tools are functions that agents can call:

```python
@agent.tool
def my_tool(ctx: RunContext[DepsType], arg: str) -> str:
    """Tool description for the AI."""
    # Access dependencies via ctx.deps
    return result
```

### 3. Running Agents

Agents run asynchronously:

```python
result = await agent.run(
    "Your instruction to the agent",
    deps=dependency_data,
)
output = result.output  # Get the structured output
```

### 4. Structured Outputs

When `output_type` is specified, agents return Pydantic models:

```python
class MyOutput(BaseModel):
    result: str
    confidence: float

agent = Agent(output_type=MyOutput)
# Agent will structure its response to match MyOutput
```

## 🔧 Customization Guide

### Step 1: Define Your Data Models

Edit `src/agent/models.py` to match your use case:

```python
class AgentOneOutput(BaseModel):
    # Replace with your fields
    processed_data: str
    metadata: dict
```

### Step 2: Update Agent Prompts

Edit `src/agent/constants.py` to give your agents specific instructions:

```python
AGENT_ONE_PROMPT = """You are an expert in X.
Your role is to:
- Do specific task A
- Process data in way B
..."""
```

### Step 3: Add Your Tools

Create tools in `src/agent/tools/` or directly in agent files:

```python
@agent_one.tool
def fetch_data(ctx: RunContext[str], query: str) -> dict:
    """Fetch data from API."""
    # Your implementation
    return data
```

### Step 4: Customize UI

Edit `src/agent/ui.py` to change how results are displayed:

```python
def display_report(report: FinalReport) -> None:
    # Customize the display for your use case
    console.print(...)
```

## 💡 Example Use Cases

Transform this template into:

1. **Research Assistant**: 
   - Agent One: Search for sources
   - Agent Two: Analyze sources
   - Agent Three: Synthesize research report

2. **Content Pipeline**:
   - Agent One: Generate draft
   - Agent Two: Edit and improve
   - Agent Three: Format and finalize

3. **Data Analysis**:
   - Agent One: Fetch data
   - Agent Two: Analyze patterns
   - Agent Three: Generate insights

4. **Code Assistant**:
   - Agent One: Understand requirements
   - Agent Two: Generate code
   - Agent Three: Review and document

## 🐛 Debugging

Enable debug logging by setting in `.env`:

```bash
DEBUG=true
```

Debug logs will show:
- Agent execution flow
- Tool calls with arguments
- Timing information

## 📚 Resources

- **Pydantic AI Docs**: [ai.pydantic.dev](https://ai.pydantic.dev)
- **Pydantic Documentation**: [docs.pydantic.dev](https://docs.pydantic.dev)
- **Rich Library**: [rich.readthedocs.io](https://rich.readthedocs.io)
- **OpenAI API**: [platform.openai.com/docs](https://platform.openai.com/docs)

## 🎯 Assignment Ideas

For students working with this template:

### Beginner
1. Change the prompts and see how agent behavior changes
2. Add a new field to the output models
3. Create a simple tool that agents can use

### Intermediate
4. Add a fourth agent to the pipeline
5. Implement error handling for specific scenarios
6. Create a more complex tool that calls an API

### Advanced
7. Add conversation history/memory between runs
8. Implement parallel agent execution instead of sequential
9. Add a database to store results
10. Create a web interface instead of CLI

## ⚠️ Important Notes

- **API Costs**: OpenAI API calls cost money. Monitor your usage at [platform.openai.com](https://platform.openai.com/)
- **Rate Limits**: Be aware of API rate limits
- **Error Handling**: Always handle potential errors from API calls
- **Security**: Never commit `.env` files or API keys to git

## 🤝 Getting Help

If you encounter issues:

1. Check that your `.env` file is properly configured
2. Ensure all dependencies are installed (`uv sync`)
3. Look at debug logs if enabled
4. Review the Pydantic AI documentation
5. Ask instructors or open an issue

## 🎉 Next Steps

1. **Explore**: Run the template and see how it works
2. **Understand**: Read through each file and understand the architecture
3. **Modify**: Start small - change prompts, add fields, etc.
4. **Build**: Transform this template into your own custom agent system!

**Happy building!** 🚀
