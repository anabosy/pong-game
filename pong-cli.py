import asyncio
import subprocess
import requests
import sys


# update the project folder to make sure that the command uvicorn can locate
# the player.py file and open it on new terminal window
folder_path = "/Users/ragadkeadan/PycharmProjects/PythonProject"

async def start_server(port):
    commands = [f"cd {folder_path}", f"uvicorn player:app --host 127.0.0.1 --port {port}"]
    combined_command = ' ; '.join(commands)
    subprocess.run([
        "osascript", "-e",
        f'tell application "Terminal" to do script "{combined_command}"'
    ])
    print(f"Server started on port {port}")

async def main():
    await asyncio.gather(
        start_server(8000),  # Start server on port 8000
        start_server(8001)   # Start server on port 8001
    )
def interactive_cli(pong_time_ms = None):

    while True:
        user_input = input("Enter command ('run servers', 'start', 'pause', 'resume', 'stop', 'exit'): ")
        if user_input.lower() == 'run servers':
            # runs the players ( two servers instances) in a new terminals.
            asyncio.run(main())
        elif user_input.lower() == 'start':
            # start the game by letting the first server(port 8000) to ping other one (8001)
            try:
                if not pong_time_ms:
                    response = requests.get(f"http://localhost:8000/ping?pong_time_ms=1000")
                else:
                    response = requests.get(f"http://localhost:8000/ping?pong_time_ms={pong_time_ms}")
            except Exception as e:
                print(f"Error pinging http://localhost:8000/ping: {e}")
        elif user_input.lower() == 'pause':
            # pause by stop the first player from sending a ping requests
            response = requests.get(f"http://localhost:8000/pause")
        elif user_input.lower() == 'resume':
            # resume the game by requesting from the first player to resume and continue from the stop point.
            response = requests.get(f"http://localhost:8000/resume")
        elif user_input.lower() == 'stop':
            # not working yet
            print("stop")
        elif user_input.lower() == 'exit':
            # not working yet
            print("exit")
            break
        else:
            print("Invalid command. Please enter ('run servers', 'start', 'pause', 'resume', 'stop', 'exit').")

if __name__ == "__main__":

    # you can run the code by sending adding the pong_time_ms as a first arg or without ( default 1000 milliseconds)
    # it is an interactive cli so once you run it you should run the servers first and then start the game,
    # 
    if len(sys.argv) > 1:
        pong_time_ms = sys.argv[1]
        interactive_cli(pong_time_ms)
    else:
        interactive_cli()
