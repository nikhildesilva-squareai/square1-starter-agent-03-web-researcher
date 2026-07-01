"""ResearchAgent: orchestrates search, content retrieval, and synthesis."""

from src.search import SearchClient
from src.synthesizer import Synthesizer


class ResearchAgent:
    """Agent that researches a topic by searching the web, retrieving page
    content from top results, and synthesizing a cited answer.
    """

    def __init__(self, search_client: SearchClient | None = None, synthesizer: Synthesizer | None = None):
        """Initialise the research agent with search and synthesis components.

        Args:
            search_client: SearchClient instance. If None, create a default one.
            synthesizer: Synthesizer instance. If None, create a default one.
        """
        raise NotImplementedError("TODO: implement agent initialisation with search + synthesizer")

    def research(self, query: str) -> str:
        """Research a topic end-to-end: search -> fetch -> synthesize.

        Args:
            query: The user's research question.

        Returns:
            A synthesized, cited answer as a markdown string.
        """
        raise NotImplementedError("TODO: implement full research pipeline")
