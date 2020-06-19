import os
import _thread as thread

import eventlet

from src.main.CommunicationLayer import WebService
from eventlet import wsgi


def run_server():
    # WebService.app.run()
    WebService.socket.run(WebService.app)
    # wsgi.server(eventlet.listen(('', 5000)), WebService.app)

def run_client():
    # Setting the option for https
    is_https = "true"

    # Apply cmd prompt command
    command_prefix = "cmd /c"

    # Run server command
    command_suffix = '\"set HTTPS=' + is_https + '&&npm start\"'    # notice the \" inside the string

    # Execute command
    os.system(command_prefix + " " + command_suffix)


if __name__ == '__main__':

    # Init & Execute threads
    try:
        thread.start_new_thread(run_server, ())   # (<func pointer>, (<params as tuple>))
        thread.start_new_thread(run_client, ())
    except Exception:
        print("Error: unable to start thread")

    # Keeping the threads running
    # VERY IMPORTANT - DO NOT DELETE THIS!!!!!!
    while True:
        pass
