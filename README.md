# ebird-mcp
An mcp server that makes the eBird API accessible to LLMs.

## Setup
1.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set the `EBIRD_API_KEY` environment variable with your eBird API key.


## Running the Server
To run the MCP server, execute the following command in a terminal:
```bash
python mcp_server.py
```

## Demonstration Use Case: Gemini CLI
1.  Install the Gemini CLI using the instructions here: https://github.com/google-gemini/gemini-cli
2.  Run `gemini` in this project's root directory. It should pick up the MCP configuration in ./.gemini/settings.json which tells it to use the running MCP server.

## Example Interaction
```
╭─────────────────────────────────────────────────────────────────────────────────────────────────╮
│  > Use ebird to list the top 10 hotspots in Rhode Island that were visited in the past 3 days.  │
╰─────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ Here are the top 10 hotspots in Rhode Island visited in the past 3 days:


   1. Apponaug Cove
   2. Beavertail State Park
   3. Big River Management Area
   4. Block Island-Point Judith Ferry
   5. Bowen's Wharf
   6. Brickyard Pond & Veterans Memorial Park
   7. Brown University Campus
   8. Castle Hill
   9. Diamond Hill Reservoir, Cumberland
   10. Doug Rayner Wildlife Refuge at Nockum Hill
```
