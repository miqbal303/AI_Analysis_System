import unittest
import asyncio
import websockets
from websockets.server import serve
from server import mock_server

class TestWebSocketServer(unittest.TestCase):
    async def test_server_connection(self):
        async with serve(mock_server, "localhost", 6789):
            uri = "ws://localhost:6789"
            async with websockets.connect(uri) as websocket:
                prompt = await websocket.recv()
                self.assertIsInstance(prompt, str)
                await websocket.send("Sample response")
                feedback = await websocket.recv()
                self.assertIn("Your response", feedback)

    def test_server_lifecycle(self):
        asyncio.run(self.test_server_connection())

if __name__ == "__main__":
    unittest.main()
