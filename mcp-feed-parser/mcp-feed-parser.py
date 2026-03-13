# imports
from fastmcp import FastMCP
import feedparser


mcp = FastMCP(name="freeCodeCamp Feed Parser")


@mcp.tool()
def fcc_news_parser(query: str, max_results: int = 5):
    """
    Parses the freeCodeCamp RSS news feed by title/description.
    """
    feed_url = "https://www.freecodecamp.org/news/rss/"
    feed = feedparser.parse(feed_url)
    
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "description": description,
                "link": entry.get("link", "")
            })
        results.append({"title": title, "url": entry.get("link", "")})
        if len(results) >= max_results:
            break
    return results or {"message": "No matching news items found."}


@mcp.tool()
def fcc_youtube_parser(query: str, max_results: int = 5):
    """
    Parses the freeCodeCamp YouTube channel RSS feed by title/description.
    """
    feed_url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    feed = feedparser.parse(feed_url)
    
    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "")
        description = entry.get("description", "")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({
                "title": title,
                "description": description,
                "link": entry.get("link", "")
            })
        if len(results) >= max_results:
            break
    return results or {"message": "No matching videos found."}


@mcp.tool()
def fcc_secret_message():
    """
    A tool that returns a hidden message.
    """
    return "Keep Exploring, Keep Learning! 🚀"


if __name__ == "__main__":
    mcp.run() # Run the MCP server by using STDIO for communication.