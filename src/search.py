"""Web search client for the Research Agent."""


class SearchClient:
    """Client that queries a web search API and returns structured results.

    Each result should contain at minimum: title, url, and snippet.
    """

    def __init__(self, api_key: str | None = None):
        """Initialise the search client.

        Args:
            api_key: API key for the search provider. If None, read from env.
        """
        raise NotImplementedError("TODO: implement search client initialisation")

    def search(self, query: str, num_results: int = 5) -> list[dict]:
        """Search the web for the given query and return structured results.

        Args:
            query: The search query string.
            num_results: Maximum number of results to return.

        Returns:
            A list of dicts, each with keys 'title', 'url', and 'snippet'.
        """
        raise NotImplementedError("TODO: implement web search query")

    def fetch_page(self, url: str) -> str:
        """Fetch and extract the main text content from a URL.

        Args:
            url: The web page URL to fetch.

        Returns:
            The extracted text content of the page.
        """
        raise NotImplementedError("TODO: implement page content extraction")
