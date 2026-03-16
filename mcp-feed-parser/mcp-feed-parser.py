"""FastMCP tools for querying freeCodeCamp RSS feeds."""

from typing import Any

import feedparser
from fastmcp import FastMCP


mcp = FastMCP(name="freeCodeCamp Feed Parser")


def _search_feed(feed_url: str, query: str, max_results: int) -> list[dict[str, Any]]:
    """Search an RSS/Atom feed for items whose title/description match a query.

    Args:
        feed_url: Feed URL to parse.
        query: Case-insensitive text to match.
        max_results: Maximum number of matching entries to return.

    Returns:
        A list of normalized feed entries.
    """
    parsed_feed = feedparser.parse(feed_url)
    query_lower = query.lower()
    results: list[dict[str, Any]] = []

    for entry in parsed_feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")

        if query_lower in title.lower() or query_lower in description.lower():
            results.append(
                {
                    "title": title,
                    "description": description,
                    "link": entry.get("link", ""),
                }
            )

        if len(results) >= max_results:
            break

    return results


@mcp.tool()
def fcc_news_parser(
    query: str, max_results: int = 5
) -> list[dict[str, Any]] | dict[str, str]:
    """Search the freeCodeCamp news RSS feed by title and description."""
    results = _search_feed("https://www.freecodecamp.org/news/rss/", query, max_results)
    return results or {"message": "No matching news items found."}


@mcp.tool()
def fcc_youtube_parser(
    query: str, max_results: int = 5
) -> list[dict[str, Any]] | dict[str, str]:
    """Search the freeCodeCamp YouTube RSS feed by title and description."""
    results = _search_feed(
        "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ",
        query,
        max_results,
    )
    return results or {"message": "No matching videos found."}


@mcp.tool()
def fcc_secret_message() -> str:
    """Return a simple motivational message."""
    return "Keep Exploring, Keep Learning! 🚀"


if __name__ == "__main__":
    mcp.run()
