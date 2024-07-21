# client.py
import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            message = "The quick brown fox jumped over the lazy dog o"
            print(f"Sending message: {message}")
            await websocket.send(json.dumps({"message": message}))

            print("Echo with delay:")
            for _ in message:
                response = await websocket.recv()
                print(f"Received: {response}", end="", flush=True)
            print("\n")

            print("Reverse echo with delay:")
            for _ in message[::-1]:
                response = await websocket.recv()
                print(f"Received: {response}", end="", flush=True)
            print("\n")

            response = await websocket.recv()
            print(f"Final response: {response}")

    except Exception as e:
        print(f"Error: {e}")

asyncio.get_event_loop().run_until_complete(test())

