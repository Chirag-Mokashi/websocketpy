# WebSocket Demo — Echo, Reverse & Character Count

A minimal Python WebSocket demonstration using the `websockets` library, showing how to build a real-time bidirectional server with character-streaming responses.

## Overview

This project implements a WebSocket server that responds to a text message with three sequential actions:

1. **Echo with delay** — streams the message back one character at a time
2. **Reverse echo with delay** — streams the reversed message one character at a time
3. **Character count** — counts occurrences of the last character in the message (excluding the last character itself) and returns the result

## Files

| File | Description |
|------|-------------|
| `server.py` | WebSocket server — handles incoming messages and streams responses |
| `client.py` | Test client — sends a message and receives all responses |

## How It Works

```
Client sends: {"message": "The quick brown fox jumped over the lazy dog o"}
        |
        v
Server streams each character of the message (echo)
        |
        v
Server streams each character of the reversed message
        |
        v
Server sends: "Count of 'o' (excluding last character): 4"
```

## Setup

```bash
pip install websockets
```

## Run

Start the server in one terminal:
```bash
python server.py
# WebSocket server is running on ws://localhost:8765
```

Run the client in another terminal:
```bash
python client.py
```

## Tech Stack

- Python 3
- `websockets` (async WebSocket library)
- `asyncio`