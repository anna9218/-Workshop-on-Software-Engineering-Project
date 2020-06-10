from src.main.CommunicationLayer import WebService, Websocket

if __name__ == "__main__":
 #   WebService.app.run()
    WebService.socket.run(WebService.app)

