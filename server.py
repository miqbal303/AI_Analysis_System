import asyncio
import websockets
from analysis import analyze_response

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

PROMPTS = [
    "Explain the concept of neural networks.",
    "What is supervised learning?",
    "Describe reinforcement learning applications."
]

async def mock_server(websocket, path):
    try:
        for prompt in PROMPTS:
            await websocket.send(prompt)  # Send prompt to client
            try:
                # Await response with a timeout
                response = await asyncio.wait_for(websocket.recv(), timeout=30)
                feedback = analyze_response(prompt, response)  # Analyze response
                await websocket.send(feedback)  # Send feedback to client
            except asyncio.TimeoutError:
                await websocket.send("Response timeout! Please try again.")
        # Notify client that all prompts are completed
        await websocket.send("All prompts are completed. Closing connection.")
    except websockets.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start the WebSocket server
start_server = websockets.serve(mock_server, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
