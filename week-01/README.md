# Personal Chatbot Assignment

Welcome to week 1! In this assignment, you'll build a basic chatbot using OpenAI's API. You'll learn about API integration, environment configuration, type safety, and functional programming while creating something useful.


**Estimated Time**: 3-4 hours

## 📋 Prerequisites

Before starting, make sure you have:

- **Python 3.11 or higher** installed ([download here](https://www.python.org/downloads/))

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

### Step 2: Get Your OpenAI API Key

The OPENAI_API_KEY is available on the BAI Probie GitHub homepage


### Step 3: Navigate to Project Directory

```bash
cd <your_directory_path>
```

### Step 4: Create Virtual Environment

A virtual environment keeps your project dependencies isolated.

```bash
uv venv
```

This creates a `.venv` directory. Activate it:

**On macOS/Linux:**
```bash
source .venv/bin/activate
```

**On Windows:**
```powershell
.venv\Scripts\activate
```

You should see `(.venv)` in your terminal prompt.

### Step 5: Install Dependencies

```bash
uv sync
```

This installs all required packages:
- `openai`: Official OpenAI Python SDK
- `pydantic`: Data validation using type hints
- `pydantic-settings`: Settings management with Pydantic
- `rich`: Formatting the messages in the terminal

### Step 6: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` in your editor and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxx
   ```

3. **That's it!** The model and system prompt are configured in the code (see `src/chatbot/constants.py`)

4. **Never commit `.env` to git!** (It's already in `.gitignore`)

## 🔍 Code Quality

This project uses [Ruff](https://docs.astral.sh/ruff/) for linting and formatting. Ruff is an extremely fast Python linter and formatter written in Rust.

### Check Your Code

Before submitting, make sure your code follows best practices:

```bash
uvx ruff check   # Lint all files in the current directory.
uvx ruff format  # Format all files in the current directory.
```

### What Ruff Checks

Ruff will help you:
- ✅ Follow Python style guidelines (PEP 8)
- ✅ Catch common bugs and anti-patterns
- ✅ Keep imports organized
- ✅ Use modern Python idioms
- ✅ Write cleaner, more readable code

## 📚 Project Structure

Here's what each file does:

```
week-01/
├── src/chatbot/
│   ├── __init__.py       # Package marker
│   ├── settings.py         # ✅ COMPLETE - Environment configuration with validation
│   ├── constants.py      # ✅ COMPLETE - Application constants | (OPTIONAL) Edit system prompt
│   ├── models.py         # ⚠️ TODO - Pydantic data models
│   ├── ui.py             # ✅ COMPLETE - Terminal UI functions
│   ├── api.py            # ⚠️ TODO - OpenAI API functions
│   └── main.py           # ⚠️ TODO - Main conversation loop
├── pyproject.toml        # Project dependencies
├── .env.example          # Environment template
├── .env                  # Your secrets (don't commit)
└── README.md             # This file
```

**Files marked ✅ are complete** - study them to learn best practices
**Files marked ⚠️ have TODOs** - this is where you'll code


## 💻 Implementation Guide

Work through the TODOs in this order:

### 1. Complete `models.py` (Start Here!)

**What to do**: Create a Pydantic model for data validation.

Open `src/chatbot/models.py` and complete:
- [ ] `ChatMessage` model (represents a single message with type-safe role validation)

**Tips**:
- Use type hints for all fields: `field_name: type`
- Use `Literal["value1", "value2"]` to restrict a field to specific values
- Check out `constants.py` to see how constants are organized

### 2. Complete `api.py` (API Integration)

**What to do**: Implement functions to interact with OpenAI's API.

Open `src/chatbot/api.py` and complete:
- [ ] `create_client()` - Initialize OpenAI client
- [ ] `create_system_message()` - Helper for system messages
- [ ] `get_chat_response()` - Main API call function (returns ChatMessage directly)

**Tips**:
- The OpenAI client is created with: `OpenAI(api_key="your-key")`
- Use `model.model_dump()` to convert Pydantic models to dicts for the API
- `get_chat_response()` returns a ChatMessage (the assistant's reply) - no wrapper needed!
- The API call structure is in the TODO comments

### 3. Complete `main.py` (Bring It Together!)

**What to do**: Build the conversation loop that users interact with.

Open `src/chatbot/main.py` and complete:
- [ ] Create OpenAI client
- [ ] Initialize conversation history
- [ ] Implement the main conversation loop

**Tips**:
- Conversation history is a `List[ChatMessage]`
- Always start with a system message
- The loop structure is outlined in the TODOs

## 🏃 Running Your Chatbot

Once you've completed the TODOs, run your chatbot:

```bash
uv run python -m src.chatbot.main
```

**Expected behavior**:
1. Welcome banner appears
2. You can type messages and get responses
3. Type `quit`, `exit`, or `bye` to end
4. Errors are displayed gracefully
5. Press `Ctrl+C` to force quit

## ✅ Testing Your Implementation

### Manual Testing Checklist

Test these scenarios:

- [ ] **Basic conversation**: Ask "What is Python?" and get a response
- [ ] **Follow-up questions**: The bot should remember context
- [ ] **Empty input**: Pressing Enter with no text should show an error
- [ ] **Quit commands**: `quit`, `exit`, `bye` should all work
- [ ] **Keyboard interrupt**: `Ctrl+C` should exit gracefully

### Example Conversation

```
╭─ Welcome ────────────────────────────────────╮
│ 🤖 Personal Chatbot                          │
│                                               │
│ Welcome! I'm your AI assistant powered by    │
│ OpenAI.                                       │
│                                               │
│ Commands:                                     │
│ • Type your message and press Enter to chat  │
│ • Type quit, exit, or bye to end             │
╰───────────────────────────────────────────────╯

You: What is Python?

🤔 Thinking...

╭─ 🤖 Assistant ───────────────────────────────╮
│ Python is a high-level, interpreted          │
│ programming language known for its           │
│ simplicity and readability...                │
╰───────────────────────────────────────────────╯

You: quit

╭─ Goodbye ─────────────────────────────────────╮
│ 👋 Goodbye!                                   │
│                                               │
│ Thanks for chatting! Come back anytime.      │
╰───────────────────────────────────────────────╯
```

## 🎓 Resources

- **OpenAI API Docs**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Pydantic Documentation**: [docs.pydantic.dev](https://docs.pydantic.dev)
- **Rich Library**: [rich.readthedocs.io](https://rich.readthedocs.io)
- **UV Documentation**: [docs.astral.sh/uv](https://docs.astral.sh/uv)
- **Ruff Documentation**: [docs.astral.sh/ruff](https://docs.astral.sh/ruff)

**Questions or issues?** Open an issue on the course repository or contact the instructors.

