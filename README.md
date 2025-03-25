# 🕵️‍♂️ scout_ai

Interact with AI-powered Solana agents via a simple Python client.

## ⚡️ Overview

`scout_ai` is a lightweight SDK to create and interact with Solana-based AI agents using the [Scout API](https://api.scout.onl).  
Each agent is assigned its own private wallet and can respond to queries like checking balances, simulating trades, and more.

---

## 📦 Installation

```bash
git clone https://github.com/your-username/scout_ai.git
cd scout_ai
```

# scout_ai example usage
```bash
from scout_client import ScoutAgent

# Create a new agent (generates a private Solana wallet)
agent = ScoutAgent.create(api_key="test", name="MyAgent")
print("Agent ID:", agent.agent_id)

# Send a query to the agent
response = agent.query("What's my SOL balance?")
print("Response:", response)
```
