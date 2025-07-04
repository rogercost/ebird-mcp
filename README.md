# ebird-mcp
An mcp server that makes the eBird API accessible to LLMs.

## Setup
1.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
2.  Set the `EBIRD_API_KEY` environment variable with your eBird API key.
3.  Set the `GOOGLE_API_KEY` environment variable with your Google Gemini API key.

## Running the Server
To run the MCP server, execute the following command in a terminal:
```bash
python mcp_server.py
```

## Running the Gemini CLI
In a separate terminal, run the Gemini CLI to interact with the MCP server:
```bash
python gemini_cli.py
