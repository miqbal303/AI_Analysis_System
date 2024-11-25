import asyncio
import websockets

async def client():
    try:
        async with websockets.connect("ws://localhost:6789") as websocket:
            while True:
                try:
                    prompt = await websocket.recv()  # Receive prompt from server
                    if prompt == "All prompts are completed. Closing connection.":
                        print(prompt)
                        break  # Exit the loop when server indicates completion

                    print(f"Prompt received: {prompt}")
                    response = input("Your response: ")  # Get response from user
                    await websocket.send(response)  # Send response to server
                    feedback = await websocket.recv()  # Get feedback from server
                    print(f"Feedback: {feedback}")
                except websockets.ConnectionClosed as e:
                    print(f"Connection closed by server: {e}")
                    break
                except Exception as e:
                    print(f"An error occurred: {e}")
    except websockets.ConnectionClosedError as e:
        print(f"Connection failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(client())
