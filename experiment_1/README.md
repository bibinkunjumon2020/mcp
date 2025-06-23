# 🤖 MCP-Powered Math Agent

A blazing-fast Python agent that connects to a custom **Math server** via [LangChain MCP](https://github.com/langchain-ai/langchain/tree/main/libs/langchain_mcp_adapters), uses [`ChatOllama`](https://github.com/langchain-ai/langchain-ollama), and executes instructions like:

> “What’s (10 + 34 + 200) × 12 × 30?”

🌐 Powered by local models like `qwen3` via [Ollama](https://ollama.com), and built with modern AI orchestration tools like **LangGraph**.

---

## 📦 Features

✅ Connects to a custom math server using `stdio`  
✅ Uses MCP tools to add and multiply via structured tool calling  
✅ Interacts with local LLMs using `langchain_ollama`  
✅ Executes multi-step instructions agentically  
✅ Built with `asyncio` and `LangGraph` REACT agent

---

## 🗂 Project Structure

```
mcp-project-1/
├── my_client.py      # Starts the REACT agent and sends a math question
├── my_server.py      # MCP server exposing `add` and `multiply` tools
├── pyproject.toml    # Poetry config with dependencies
├── README.md         # You're reading it!
└── .gitignore        # Ignored files and folders
```

---

## 🚀 Getting Started

### 🧱 Prerequisites

- Python **3.12+**
- [Poetry](https://python-poetry.org/) for dependency management
- [Ollama](https://ollama.com) installed and running locally (e.g. with `qwen3` model)

### 📥 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/mcp-project-1.git
cd mcp-project-1

# Install dependencies
poetry install

# Activate the environment
poetry shell
```

---

## 🧪 Running the Agent

Make sure your model (e.g., `qwen3:latest`) is available in Ollama:

```bash
ollama pull qwen3
ollama run qwen3
```

Then run the agent:

```bash
poetry run python my_client.py
```

You'll see output like:

```
The result of (10 + 34 + 200) × 12 × 30 is 87,840
```

---

## 🛠 Custom Math Server (MCP)

`my_server.py` defines two tools:

```python
@mcp.tool()
def add(a: int, b: int) -> int: return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int: return a * b
```

Run the server in background (if needed):

```bash
python my_server.py
```

Or let the client spawn it via stdio (as it does now).

---

## 📚 Dependencies

Managed with Poetry via `pyproject.toml`:

- `langchain-mcp-adapters`
- `langgraph`
- `langchain-ollama`
- `asyncio`

---

## 👨‍💻 Author

Created by **[bibinkunjumon2020](mailto:bibinkunjumon2020@gmail.com)**  
🔗 GitHub: [yourusername](https://github.com/yourusername)

---

## 🧠 Powered By

- 🧩 [LangGraph](https://github.com/langchain-ai/langgraph)
- 🧠 [LangChain](https://www.langchain.com/)
- 🦙 [Ollama](https://ollama.com)
- ⚙️ [LangChain MCP Adapters](https://github.com/langchain-ai/langchain/tree/main/libs/langchain_mcp_adapters)

---

## 📄 License

MIT – use it, hack it, share it.
