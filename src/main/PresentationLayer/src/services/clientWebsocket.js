export {connect}
var socket = require('socket.io-client')('http://localhost:5000'); // TODO- maybe another port?

// TODO - ask einat how to add the call to connect (<username>, <storename>)
class clientWebsocket{//(props){
  // const [socket, setSocket] = useState(null);
    constructor(gui) {
      this.gui = gui;
      this.socket = null;
    }

    // useEffect(async () => {
    //   // init system on startup
    //   props.my_prop
    // });
    
    // const connect = (username, storename) => {
    connect(username, storename) {
        this.socket = io.connect(port, {transports: ["websocket"], });
        this.setHandlers(username, storename);
    };

    // const setHandlers = (username, storename) => {
    setHandlers (username, storename){
        this.socket.on("message", (data) => {
          const {storename, msg} = data;
          const msgs = JSON.parse(data).messages;
          alert(msg);
          this.gui.add_notification(msgs); // TODO - tell einat to add this func
          <OpenStore msg={msgs} />
        });
        this.socket.on("connect", () => {
          this.socket.emit("subscribe", { username: username, room: storename });
        });
      };

    // const disconnect = (username, storename) => {
    disconnect (username, storename){
        this.socket.emit("unsbscribe", { username: username, room: storename });
    };

};

export default clientWebsocket;
// module.exports = clientWebsocket;

