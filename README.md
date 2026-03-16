# mcp-examples

Reference implementations of MCP servers using:

- FastAPI + `fastapi-mcp`
- FastMCP (STDIO and HTTP transports)
- FastMCP + `feedparser` for RSS/Atom querying

These examples are intentionally small and are useful as starter templates.

## Repository layout

```text
.
├── .env-template
├── fastapi-mcp/
│   └── fastapi-mcp-calculator.py
├── fastmcp/
│   ├── fastmcp-calculator.py
│   └── fastmcp-calculator-v2.py
├── mcp-feed-parser/
│   └── mcp-feed-parser.py
└── requirements.txt
```

## Prerequisites

- Python 3.10+
- uv (Python package manager and runner)
- Node.js (optional, only for MCP Inspector)

## Environment setup

Create a local environment file from the template:

```bash
cp .env-template .env
```

Then edit `.env` with your local values.

The provided `.env-template` includes starter defaults. The current examples do
not require environment variables unless you wire these values into the scripts.

## Install dependencies (uv)

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Examples

### 1) FastAPI + FastAPI-MCP calculator

File: `fastapi-mcp/fastapi-mcp-calculator.py`

What it demonstrates:
- Building a basic FastAPI calculator API (`add`, `subtract`, `multiply`, `divide`)
- Mounting MCP over the same app using `FastApiMCP(app).mount_http()`
- Running with Uvicorn on `0.0.0.0:8000`

Run:

```bash
uv run python fastapi-mcp/fastapi-mcp-calculator.py
```

### 2) FastMCP calculator (STDIO transport)

File: `fastmcp/fastmcp-calculator.py`

What it demonstrates:
- Registering tools with `@mcp.tool()`
- Naming/tagging tools for better discoverability
- Running an MCP server over STDIO (useful for local client subprocess integration)

Run:

```bash
uv run python fastmcp/fastmcp-calculator.py
```

### 3) FastMCP calculator (HTTP transport)

File: `fastmcp/fastmcp-calculator-v2.py`

What it demonstrates:
- The same calculator tools as above
- Running FastMCP with HTTP transport on `localhost:8080`

Run:

```bash
uv run python fastmcp/fastmcp-calculator-v2.py
```

### 4) FastMCP feed parser

File: `mcp-feed-parser/mcp-feed-parser.py`

What it demonstrates:
- Querying RSS/Atom feeds using `feedparser`
- Reusing a shared feed-search helper
- Exposing feed lookup as MCP tools:
	- `fcc_news_parser`
	- `fcc_youtube_parser`
	- `fcc_secret_message`

Run:

```bash
uv run python mcp-feed-parser/mcp-feed-parser.py
```

## Inspecting/debugging with MCP Inspector

The MCP Inspector is the easiest way to test tools and inspect schemas.

```bash
npx @modelcontextprotocol/inspector <your-server-command>
```

For example (local Python server):

```bash
npx @modelcontextprotocol/inspector uv run python fastmcp/fastmcp-calculator.py
```

## Notes

- The FastAPI sample filename is intentionally kept as-is (`calcularor`) to match repository history.
- Calculator division tools guard against division by zero.
- The feed parser returns a fallback message when no matches are found.

## References:

- MCP documentation and specification: https://modelcontextprotocol.io/
- MCP Inspector guide: https://modelcontextprotocol.io/docs/tools/inspector
- `@modelcontextprotocol/inspector` package: https://www.npmjs.com/package/@modelcontextprotocol/inspector
- FastMCP docs: https://gofastmcp.com/getting-started/welcome
- FastMCP repository: https://github.com/prefecthq/fastmcp
- FastAPI-MCP docs: https://fastapi-mcp.tadata.com/
- FastAPI docs: https://fastapi.tiangolo.com/
- feedparser docs: https://feedparser.readthedocs.io/en/latest/

## Original reference video

- https://youtu.be/DosHnyq78xY?si=V4DSGMHX4kE3BYMh