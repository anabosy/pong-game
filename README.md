Ping-Pong Server-Client Game
Overview
This project demonstrates a simple ping-pong interaction between two FastAPI server instances running on different ports. The interaction is controlled via an interactive Command-Line Interface (CLI). The servers can handle asynchronous ping-pong requests, pause and resume their actions, and maintain game flow with a specified delay (pong_time_ms) between actions.

Features
Run Multiple Servers: Automatically start two servers (localhost:8000 and localhost:8001) in new terminal windows.
Interactive CLI: Control the game with commands like start, pause, resume, and stop.
Asynchronous Pings: Servers asynchronously send ping requests to each other.
Pause & Resume: Pause and resume the game flow using dedicated endpoints.
Custom Timing: Specify the delay (pong_time_ms) for ping-pong interactions.
Setup and Installation
Prerequisites
Python 3.7 or higher
pip (Python package manager)
FastAPI
Uvicorn (ASGI server)
requests library
Installation Steps
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git
cd your-repo
Install dependencies:

bash
Copy
Edit
pip install fastapi uvicorn requests
Update the project folder path: In the Python file, update the folder_path variable to point to your project folder:

python
Copy
Edit
folder_path = "/path/to/your/project"
How to Run the Project
Step 1: Start the CLI
Run the Python script to launch the interactive CLI:

bash
Copy
Edit
python script.py [pong_time_ms]
If pong_time_ms is not provided, the default delay is 1000 ms.
Example:
bash
Copy
Edit
python script.py 1500
Step 2: Use CLI Commands
In the CLI, you can use the following commands:

Command	Description
run servers	Starts two FastAPI servers on ports 8000 and 8001 in new terminal windows.
start	Initiates the ping-pong game between the two servers.
pause	Pauses the game by stopping the first server from sending requests.
resume	Resumes the game from the paused state.
stop	Placeholder command (not implemented yet).
exit	Placeholder command to exit the CLI (not fully functional).
Endpoints
The FastAPI servers expose the following endpoints:

Endpoint	Method	Description
/ping	GET	Handles the ping request and asynchronously sends a ping to the other server.
/pause	GET	Pauses the server, stopping it from responding to requests.
/resume	GET	Resumes the server, allowing it to handle requests again.
/	GET	Returns a basic "Hello World" message.
Code Structure
script.py:
Contains the CLI logic.
Starts two FastAPI servers on ports 8000 and 8001 using osascript.
Handles ping-pong game interactions via CLI commands.
FastAPI Server Logic:
Implements the /ping endpoint to handle ping requests and pass them to the other server.
Implements /pause and /resume endpoints to manage game state.
Example Usage
Run the CLI:

bash
Copy
Edit
python script.py
Start the servers:

arduino
Copy
Edit
> run servers
This opens two new terminal windows with servers running on localhost:8000 and localhost:8001.

Start the game:

markdown
Copy
Edit
> start
The servers will start pinging each other with the default or specified pong_time_ms.

Pause the game:

css
Copy
Edit
> pause
Resume the game:

lua
Copy
Edit
> resume
Known Limitations
The stop and exit commands are placeholders and need to be implemented.
The game currently only supports two servers.
Future Improvements
Add functionality to stop the servers gracefully.
Implement proper exit handling for the CLI.
Extend the game to support multiple servers dynamically.
Let me know if you'd like any further modifications to this README! 😊














