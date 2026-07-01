"""Contract tests for the Web Research Agent.

These tests verify the public interface of each module.
They are expected to FAIL against the stubs and PASS once implemented.
"""

import pytest
from src.search import SearchClient
from src.synthesizer import Synthesizer
from src.agent import ResearchAgent


class TestSearchClient:
    """Search must return structured results."""

    def test_search_returns_structured_results(self):
        """search() returns a list of dicts with title, url, and snippet keys."""
        client = SearchClient()
        results = client.search("Python programming", num_results=3)
        assert isinstance(results, list) and len(results) > 0
        for r in results:
            assert "title" in r
            assert "url" in r
            assert "snippet" in r


class TestSynthesizer:
    """Synthesizer must produce a summary from source material."""

    def test_synthesizer_produces_summary(self):
        """summarize() returns a non-empty string given source documents."""
        synth = Synthesizer()
        sources = [
            {"title": "Source A", "url": "https://a.com", "content": "Python is a language."},
            {"title": "Source B", "url": "https://b.com", "content": "Python is used in AI."},
        ]
        summary = synth.summarize(sources, query="What is Python?")
        assert isinstance(summary, str) and len(summary) > 0


class TestResearchAgent:
    """The agent must handle a multi-source research query."""

    def test_agent_handles_multi_source_queries(self):
        """research() returns a non-empty cited answer."""
        agent = ResearchAgent()
        answer = agent.research("What are the benefits of Python for data science?")
        assert isinstance(answer, str) and len(answer) > 0
