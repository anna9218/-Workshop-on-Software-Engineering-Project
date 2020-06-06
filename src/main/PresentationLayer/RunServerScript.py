import os
import _thread as thread
from src.main.CommunicationLayer import WebService


def run_server():
    WebService.app.run()


def run_client():
    # Setting the option for https
    is_https = "true"

    # Apply cmd prompt command
    command_prefix = "cmd /c"

    # Run server command
    command_suffix = '\"set HTTPS=' + is_https + '&&npm start\"'

    # Execute command
    os.system(command_prefix + " " + command_suffix)


if __name__ == '__main__':

    # Init & Execute threads
    try:
        thread.start_new_thread(run_server, ())
        thread.start_new_thread(run_client, ())
    except Exception:
        print("Error: unable to start thread")

    # Keeping the threads running
    # VERY IMPORTANT - DO NOT DELETE THIS!!!!!!
    while True:
        pass
