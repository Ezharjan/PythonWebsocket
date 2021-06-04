import asyncio
import websockets
import json


async def client():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        # Allow user to enter username into command line
        username = input("Enter a username: ")
        data = json.dumps({"username": username})

        # Send username as JSON object to server
        await websocket.send(data)

        response = await websocket.recv()
        print(response)


asyncio.get_event_loop().run_until_complete(client())