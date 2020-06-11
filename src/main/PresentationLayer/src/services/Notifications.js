
import {useState, useEffect} from 'react';
import port from '../App';
import 'bootstrap/dist/css/bootstrap.min.css';
import io from 'socket.io-client';
// const io = require("socket.io-client");
// var socketio = require('socket.io-client'); //('http://127.0.0.1:5000'); // TODO- maybe another port?

var socket = {socket: io.connect('http://127.0.0.1:5000', {
    transports: ["websocket"]
  })};
var nickname = {nickname:''};
var storeName = {storeName:''};

export async function init (nickname, store_name){
  this.nickname = {nickname: nickname};
  this.storeName = {storeName: store_name};
  console.log("this nickname:" + this.nickname.nickname);
  console.log("this storename:" + this.storeName.storeName);
  // connect();
  // this.socket = {};
  await setHandlers();
  console.log(this.nickname.nickname + " is connected to server by websocket");
  return;
}

export const connect = async () => { //maybe need to change the signature and make it like the init function
  // socket = socketio.connect(port, {transports: ["websocket"], }); // maybe props.socket

};


export const setHandlers = async () => {
  socket.socket.io.on("message", (data) => {
    const {storeName, msg} = data;
    const msgs = JSON.parse(data).messages;
    alert(msg);
  //   this.gui.add_notification(msgs); // TODO - tell einat to add this func
  //   <OpenStore msg={msgs} />
  });
  socket.socket.io.on("connect", () => {
  //   this.socket.emit("subscribe", { username: username, room: storename });
    socket.socket.io.emit("subscribe", { username: nickname, room: storeName });
    //  maybe:         socket.emit("subscribe", { username: {username}, room: {storename} });

  });
};

export const disconnect = () => {
// disconnect (username, storename){
  // this.socket.emit("unsbscribe", { username: username, room: storename });
  socket.socket.io.emit("unsbscribe", { username: nickname, room: storeName });
}

export const register_new_store = (storename) => {
  socket.socket.io.emit("subscribe", { username: nickname, storeName });
}

