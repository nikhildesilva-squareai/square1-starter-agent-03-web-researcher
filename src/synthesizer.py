"""Multi-source content synthesizer for the Research Agent."""

from anthropic import Anthropic


class Synthesizer:
    """Synthesizes information from multiple sources into a coherent summary
    with citations.
    """

    def __init__(self, client: Anthropic | None = None, model: str = "claude-sonnet-4-20250514"):
        """Initialise the synthesizer with an Anthropic client.

        Args:
            client: Anthropic client instance. If None, create from env.
            model: Claude model identifier.
        """
        raise NotImplementedError("TODO: implement synthesizer initialisation")

    def summarize(self, sources: list[dict], query: str) -> str:
        """Summarize content from multiple sources into a cited response.

        Args:
            sources: A list of dicts with keys 'title', 'url', and 'content'.
            query: The original user query to answer.

        Returns:
            A markdown-formatted summary with inline citations [1], [2], etc.
        """
        raise NotImplementedError("TODO: implement multi-source summarisation with citations")
