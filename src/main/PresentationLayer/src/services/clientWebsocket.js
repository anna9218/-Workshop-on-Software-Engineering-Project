var socket = require('socket.io-client')('http://localhost:5000'); // TODO- maybe another port?


class clientWebsocket {
    constructor(gui) {
      this.gui = gui;
      this.socket = null;
    }

    connect(host, username, storename) {
        this.socket = io.connect(host, {transports: ["websocket"], });
        this.setHandlers(username, storename);
    }

    setHandlers(username, storename) {
        this.socket.on("message", (data) => {
          const {storename, msg} = data;
          const msgs = JSON.parse(data).messages;
          console.log(msgs)
          this.gui.add_notification(msgs); // TODO - tell einat to add this func
        });
        // this.socket.on("connect", () => {
        //   this.socket.emit("join", { username: username, room: storename });
        // });
      }

    disconnect(username, storename) {
        this.socket.emit("leave", { username: username, room: storename });
    }

}

module.exports = clientWebsocket;
