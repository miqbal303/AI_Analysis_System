import unittest
import asyncio
from websockets import serve, connect
from client import client

async def mock_server(websocket, path):
    await websocket.send("Test prompt")
    response = await websocket.recv()
    await websocket.send(f"Feedback: {response}")

class TestWebSocketClient(unittest.TestCase):
    async def test_client_interaction(self):
        async with serve(mock_server, "localhost", 6789):
            uri = "ws://localhost:6789"
            async with connect(uri) as websocket:
                await websocket.send("Sample response")
                feedback = await websocket.recv()
                self.assertIn("Feedback", feedback)

    def test_client_lifecycle(self):
        asyncio.run(self.test_client_interaction())

if __name__ == "__main__":
    unittest.main()
