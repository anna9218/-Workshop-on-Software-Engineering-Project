
import {useState, useEffect} from 'react';
import port from '../App';
import 'bootstrap/dist/css/bootstrap.min.css';


var socketio = require('socket.io-client')('http://localhost:5000'); // TODO- maybe another port?

var socket = {socket: null};
var nickname = {nickname:''};
var storeName = {storeName:''};

export function init(nickname, store_name){
  this.nickname = {nickname: nickname};
  this.storeName = {storeName: store_name};
  console.log("this nickname:" + this.nickname.nickname);
  console.log("this storename:" + this.storeName.storeName);
  return;
}

export const connect = async () => { //maybe need to change the signature and make it like the init function
  socket = socketio.connect(port, {transports: ["websocket"], }); // maybe props.socket
  setHandlers();
};


export const setHandlers = async () => {
  this.socket.on("message", (data) => {
    const {storeName, msg} = data;
    const msgs = JSON.parse(data).messages;
    alert(msg);
  //   this.gui.add_notification(msgs); // TODO - tell einat to add this func
  //   <OpenStore msg={msgs} />
  });
  socket.on("connect", () => {
  //   this.socket.emit("subscribe", { username: username, room: storename });
    socket.emit("subscribe", { username: nickname, room: storeName });
    //  maybe:         socket.emit("subscribe", { username: {username}, room: {storename} });

  });
};

export const disconnect = () => {
// disconnect (username, storename){
  // this.socket.emit("unsbscribe", { username: username, room: storename });
  this.socket.emit("unsbscribe", { username: nickname, room: storeName });
}

export const register_new_store = (storename) => {
  socket.emit("subscribe", { username: nickname, storeName });
}

