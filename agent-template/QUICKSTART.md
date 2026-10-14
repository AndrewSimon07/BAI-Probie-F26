# Quick Start Guide

Get up and running with the Multi-Agent Template in 5 minutes!

## 1. Install UV

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 2. Set Up Environment

```bash
# Navigate to template
cd agent-template

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# OR
.venv\Scripts\activate     # Windows

# Install dependencies
uv sync
```

## 3. Configure API Key

Create a `.env` file:

```bash
echo 'OPENAI_API_KEY=sk-proj-your-key-here' > .env
```

Replace `sk-proj-your-key-here` with your actual OpenAI API key.

## 4. Run It!

```bash
uv run python -m src.agent.main
```

You should see:
- Welcome message
- Prompt for input
- Three agents processing in sequence
- Final report display

## What's Next?

1. **Explore the Code**: Start with `src/agent/main.py` to see the orchestration
2. **Customize Agents**: Edit `src/agent/sub_agents/` files
3. **Add Tools**: Create functions in `src/agent/tools/`
4. **Modify Models**: Update `src/agent/models.py` for your data structures
5. **Change Prompts**: Edit `src/agent/constants.py` to change agent behavior

## Common Issues

**Issue**: `ModuleNotFoundError`  
**Fix**: Make sure you activated the virtual environment and ran `uv sync`

**Issue**: `OpenAI API Error`  
**Fix**: Check that your `.env` file has the correct API key

**Issue**: `No module named 'src'`  
**Fix**: Make sure you're running from the project root directory

## Example Interaction

```
Enter your input: Analyze the sentiment of "This is amazing!"

Running Agent One...
✅ Agent One completed

Running Agent Two...
✅ Agent Two completed

Running Agent Three...
✅ Agent Three completed

[Beautiful formatted output showing results from all three agents]
```

Happy building! 🚀

