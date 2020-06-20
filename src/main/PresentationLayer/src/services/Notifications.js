
import {useState, useEffect} from 'react';
import port from '../App';
import 'bootstrap/dist/css/bootstrap.min.css';
import io from 'socket.io-client';
// const io = require("socket.io-client");
// var socketio = require('socket.io-client'); //('http://127.0.0.1:5000'); // TODO- maybe another port?

var socket = {socket: io.connect('http://127.0.0.1:5000', {transports: ["polling"], autoConnect: true, forceNew: true})};
var nickname = {nickname:''};
var storeName = {storeName:''};
var counter = {counter:0};

export async function init (nickname, store_name){
  if (!this.counter){
    this.nickname = {nickname: nickname};
    this.storeName = {storeName: store_name};
    console.log("this nickname:" + this.nickname.nickname);
    console.log("this storename:" + this.storeName.storeName);
    connect();
    // this.socket = {};
    // io.handshake.query.token;
    // socket.socket.io.emit("join", {username: nickname, store: store_name});
    // this.counter = {counter: 1};
    console.log("counter = " + this.counter)

    await setHandlers(); // maybe while loop?
    console.log(this.nickname.nickname + " is connected to server by websocket");
  }
  return;
}

// export const connect = async () => { //maybe need to change the signature and make it like the init function
//   // socket = socketio.connect(port, {transports: ["websocket"], }); // maybe props.socket

// };
export const connect = async (host, username) => {
  socket.socket.io.emit("join", {username: nickname, store: storeName});
  await setHandlers(); 
}


export const setHandlers = async () => {
  socket.socket.io.on("message", (data) => {
    // const {storeName, msg} = data;
    console.log("got msg!")
    // list of msgs
    // const msgs = data["messages"];
    const msgs = JSON.parse(data).messages;
    alert("hiiiii")
    alert(msgs)
    // eden: display the notification without button
    
    console.log(msgs);
  //   this.gui.add_notification(msgs); // TODO - tell einat to add this func
  //   <OpenStore msg={msgs} />
  });
  socket.socket.io.on("agreement", () => {
    // eden: display the notification with button (create a function)
    // socket.socket.io.emit("subscribe", { username: username, room: storename });
    //  maybe:         socket.emit("subscribe", { username: {username}, room: {storename} });
  });
};

export const disconnect = () => {
// disconnect (username, storename){
  // this.socket.emit("unsbscribe", { username: username, room: storename });
  socket.socket.io.emit("unsbscribe", JSON.parse({ username: nickname, store: storeName }));
}

export const register_new_store = (storename) => {
  socket.socket.io.emit("join", { username: nickname, store:storename });
}

