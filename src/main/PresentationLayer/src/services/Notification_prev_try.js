
import {useState, useEffect} from 'react';
import port from '../App';


var socketio = require('socket.io-client')('http://localhost:5000'); // TODO- maybe another port?

// export {connect}

function Notifications(props){
    
    useEffect(() => {
        setUsername(props.Username);
        setStorename(props.Storename);
        // connect();
    }, []);

    const [socket, setSocket] = useState({socket: null});
    const [username, setUsername] = useState({Username:''});
    const [storename, setStorename] = useState({Storename:''});

    const connect = async () => {
        socket = socketio.connect(port, {transports: ["websocket"], }); // maybe props.socket
        setHandlers();
    };

    // const setHandlers = (username, storename) => {
    const setHandlers = async () => {
        this.socket.on("message", (data) => {
          const {storename, msg} = data;
          const msgs = JSON.parse(data).messages;
          alert(msg);
        //   this.gui.add_notification(msgs); // TODO - tell einat to add this func
        //   <OpenStore msg={msgs} />
        });
        socket.on("connect", () => {
        //   this.socket.emit("subscribe", { username: username, room: storename });
          socket.emit("subscribe", { username: props.Username, room: props.Storename });
          //  maybe:         socket.emit("subscribe", { username: {username}, room: {storename} });

        });
      };

    const disconnect = () => {
    // disconnect (username, storename){
        // this.socket.emit("unsbscribe", { username: username, room: storename });
        this.socket.emit("unsbscribe", { username: props.username, room: props.storename });
    }
    
    const register_new_store = (storename) => {
        socket.emit("subscribe", { username: props.username, room: storename });
    }
}
// export {connect, register_new_store};

export default Notifications;
// module.exports = Notifications;
// export default Notifications.register_new_store;

//   render() {
//     return (
//       <div>
//         {/* Count: <strong>{this.state.count}</strong> */}  
// {/* 
//         <Websocket url= 'ws:localhost:8765/' // listens to this url, maybe ws instead of wss
//             onOpen= {this.requestUnreadMsgs} // send to server
//             onMessage={this.handleData.bind(this)} // recieve from server 
//             onClose = {this.alertLogout} // send to server 
//             />  */}
//       </div> // on<something> required The callback called when <something> happend. Data is JSON.parse'd
//     )
// }