# server.py
import asyncio
import websockets
import json

async def echo(websocket, path):
    print("Client connected")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            data = json.loads(message)

            # Action 1: Echo with delay
            for char in data["message"]:
                await websocket.send(char)
                await asyncio.sleep(0.1)

            # Action 2: Reverse echo with delay
            reversed_message = data["message"][::-1]
            for char in reversed_message:
                await websocket.send(char)
                await asyncio.sleep(0.1)

            # Action 3: Count last character occurrences
            last_char = data["message"][-1]
            count = data["message"][:-1].count(last_char)
            response = f"Count of '{last_char}' (excluding last character): {count}"
            await websocket.send(response)
            print(f"Sent response: {response}")

    except Exception as e:
        print(f"Error: {e}")

start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
print("WebSocket server is running on ws://localhost:8765")
asyncio.get_event_loop().run_forever()
