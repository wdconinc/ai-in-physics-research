"""Week 5 Meeting 1 — MCP Server Skeleton

Implement a minimal MCP server that exposes two physics database queries
as LLM-callable tools.

Goal: by the end of this exercise your server should return
      spectral type 'M1-2Ia-Iab' for Betelgeuse.

Steps:
  1. Implement query_simbad() using astroquery.simbad
  2. Implement search_arxiv() using the arxiv library
  3. Test each tool in isolation with the __main__ block below
  4. Run this server and invoke both tools via llm_client.py

Start the server:
    python mcp_skeleton.py

Then, in a separate terminal:
    python llm_client.py
"""

# Install dependencies if needed:
#   pip install mcp astroquery arxiv anthropic python-dotenv

import asyncio
import json
from mcp.server import Server
from mcp.server.stdio import stdio_server

server = Server("physics-tools")


@server.tool()
async def query_simbad(object_name: str) -> dict:
    """Query SIMBAD for basic properties of a named astronomical object.

    Returns a dict with keys: object_type, spectral_type, parallax_mas,
    radial_velocity_km_s.
    Raises ValueError if the object is not found in SIMBAD.
    """
    # TODO: implement using astroquery.simbad
    # Hint:
    #   from astroquery.simbad import Simbad
    #   Simbad.add_votable_fields("sptype", "plx", "rv_value", "otype")
    #   result_table = Simbad.query_object(object_name)
    #   if result_table is None:
    #       raise ValueError(f"Object not found in SIMBAD: {object_name}")
    raise NotImplementedError("Implement query_simbad using astroquery.simbad")


@server.tool()
async def search_arxiv(keyword: str, max_results: int = 5) -> list:
    """Search arXiv for recent papers matching a keyword.

    Returns a list of dicts, each with keys:
    arxiv_id, title, authors, abstract.
    """
    # TODO: implement using the arxiv library
    # Hint:
    #   import arxiv
    #   client = arxiv.Client()
    #   search = arxiv.Search(
    #       query=keyword,
    #       max_results=max_results,
    #       sort_by=arxiv.SortCriterion.SubmittedDate,
    #   )
    #   return [
    #       {
    #           "arxiv_id": r.get_short_id(),
    #           "title": r.title,
    #           "authors": [a.name for a in r.authors],
    #           "abstract": r.summary,
    #       }
    #       for r in client.results(search)
    #   ]
    raise NotImplementedError("Implement search_arxiv using the arxiv library")


async def _test_tools():
    """Quick smoke tests — run before connecting the LLM client."""
    print("--- Testing query_simbad ---")
    result = await query_simbad("Betelgeuse")
    assert "spectral_type" in result, "Missing spectral_type key"
    print(json.dumps(result, indent=2))

    print("\n--- Testing search_arxiv ---")
    results = await search_arxiv("Betelgeuse", max_results=3)
    assert isinstance(results, list) and len(results) > 0, "Expected a non-empty list"
    print(f"{len(results)} result(s). First title: {results[0]['title']}")


async def _serve():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    import sys

    if "--test" in sys.argv:
        asyncio.run(_test_tools())
    else:
        asyncio.run(_serve())
