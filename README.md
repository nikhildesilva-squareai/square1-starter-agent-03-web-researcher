# Web Research Agent — Square 1 AI starter

**Part of [Square 1 AI](https://square1-tutor.vercel.app) · LLM Agent Architect · Project 3.**

🤖 **Agent project.** This repo provides the project scaffold, function stubs, and contract tests. Read the full brief on Square 1 for guidance.

MIT licensed — fork it, build on it, put it in your portfolio.

---

# P3: Web Research Agent

Build an AI agent that searches the web for information, retrieves content from multiple sources, synthesizes the findings, and delivers a cited summary to the user.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env        # Add your ANTHROPIC_API_KEY
```

## Usage

```bash
python -m src.cli
```

## Project Structure

```
src/
  search.py       - Web search client
  synthesizer.py  - Multi-source summarisation
  agent.py        - ResearchAgent orchestration
  cli.py          - Interactive command-line interface
tests/
  test_agent.py   - Contract tests for search, synthesis, and agent
```
