import asyncio
import subprocess
import time
import requests



async def start_server(port):
    """Starts a FastAPI server on the specified port in a new terminal."""
    commands = ["cd /Users/ragadkeadan/PycharmProjects/PythonProject", f"uvicorn player:app --host 127.0.0.1 --port {port}"]
    combined_command = ' ; '.join(commands)
    # subprocess.Popen(["", "-c", f"{command}; bash"])
    subprocess.run([
        "osascript", "-e",
        f'tell application "Terminal" to do script "{combined_command}"'
    ])
    print(f"Server started on port {port}")
    # time.sleep(0.5)  # Slight delay for server startup

async def main():
    await asyncio.gather(
        start_server(8000),  # Start server on port 8000
        start_server(8001)   # Start server on port 8001
    )
def interactive_cli():

    while True:
        user_input = input("Enter command ('run servers', 'start', 'pause', 'resume', 'stop', 'exit'): ")
        if user_input.lower() == 'run servers':
            asyncio.run(main())
            # time.sleep(50)
        elif user_input.lower() == 'start':
            try:
                response = requests.get(f"http://localhost:8000/ping")
            except Exception as e:
                print(f"Error pinging http://localhost:8000/ping: {e}")
        elif user_input.lower() == 'pause':
            response = requests.get(f"http://localhost:8000/pause")
            print("pause2")
        elif user_input.lower() == 'resume':
            response = requests.get(f"http://localhost:8000/resume")
            print("resume2")
        elif user_input.lower() == 'stop':
            print("stop")
        elif user_input.lower() == 'exit':
            print("exit")
            break
        else:
            print("Invalid command. Please enter ('run servers', 'start', 'pause', 'resume', 'stop', 'exit').")

if __name__ == "__main__":

    interactive_cli()
