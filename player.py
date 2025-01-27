import asyncio

import requests
from fastapi import FastAPI, Request

app = FastAPI()

# Flag to control whether the server is accepting requests
is_paused = False
pause_event = asyncio.Event()  # Used to control pausing

# Initially set the event to allow execution
pause_event.set()


async def controlled_sleep(milliseconds):
    for _ in range(milliseconds):  # Sleep one second at a time to allow pausing
        await pause_event.wait()  # Wait until pause_event is set
        await asyncio.sleep(1/1000)

@app.get("/pause")
async def pause_server():
    global is_paused
    is_paused = True
    pause_event.clear()  # Pause by clearing the event
    return {"message": "Server paused."}

@app.get("/resume")
async def resume_server():
    global is_paused
    is_paused = False
    pause_event.set()  # Resume by setting the event
    return {"message": "Server resumed."}

@app.get("/")
async def root():
    return {"Hello": "World"}

async def ping(server_host, server_port, pong_time_ms):

        await controlled_sleep(pong_time_ms)  # Pause sleep for 1 seconds
        print("read_root:", server_host, server_port)
        try:
            message = ""
            if server_port == '8000':
                if pong_time_ms:
                    response =  requests.get(f"http://{server_host}:8001/ping?pong_time_ms={pong_time_ms}")
                else:
                    response = requests.get(f"http://{server_host}:8001/ping?pong_time_ms=1000")
                message = f"Received pong from {server_host}:8001 response :  {response}"
            else:
                if pong_time_ms:
                    response = requests.get(f"http://{server_host}:8000/ping?pong_time_ms={pong_time_ms}")
                else:
                    response = requests.get(f"http://{server_host}:8000/ping?pong_time_ms=1000")

                message = f"Received pong from {server_host}:8000 response :  {response}"
            response.raise_for_status()  # Raise an exception for bad status codes
            print(message)

        except Exception as e:
            print(f"Error pinging {server_host}:8001: {e}")


@app.get("/ping")
async def read_item(pong_time_ms: int = None, request: Request = None):
    server_host, server_port = request.headers.get("host").split(":")
    print("got ping")
    asyncio.create_task(ping(server_host,server_port, pong_time_ms ))
    # print(f"pong from {server_port}")
    return {"pong"}
