
import {useState, useEffect} from 'react';
import port from '../App';
import 'bootstrap/dist/css/bootstrap.min.css';
import io from 'socket.io-client';
import * as Notifications from '../components/OwnerOrManagerRole/NotificationsActions'

// const io = require("socket.io-client");
// var socketio = require('socket.io-client'); //('http://127.0.0.1:5000'); // TODO- maybe another port?

// var socket = {socket: io.connect('http://127.0.0.1:5000', {transports: ["polling"], autoConnect: true, forceNew: true})};
var socket = {socket: io.connect('http://127.0.0.1:5000', {transports: ["websocket"], autoConnect: true, forceNew: true})};
var nickname = {nickname:''};
var storeName = {storeName:''};
var counter = {counter:0};

export async function init (nick_name, store_name){
  if (!this.counter){
    nickname = {nickName: nick_name};
    // this.nickname = {nickName: nickname};
    storeName = {storeName: store_name};
    console.log("this nickname:" + nickname.nickName);
    // console.log("this nickname:" + this.nickname.nickName);
    console.log("this storename:" + storeName.storeName);
    // connect();
    // this.socket = {};
    // io.handshake.query.token;
    // socket.socket.io.emit("join", {username: nickname, store: store_name});
    this.counter = {counter: 1};
    console.log("counter = " + this.counter)
    console.log(nickname.nickName + " is connected to server by websocket");
    // console.log(this.nickname.nickName + " is connected to server by websocket");
    await connect();
    // await setHandlers(); // maybe while loop?
  }
  return;
}

// export const connect = async () => { //maybe need to change the signature and make it like the init function
//   // socket = socketio.connect(port, {transports: ["websocket"], }); // maybe props.socket

// };
// export const connect = async () => {
export const connect = async (host, username) => {
  // socket.socket.io.emit("join", {username: nickname, store: storeName});
  console.log("nickname= " + nickname.nickName + ", storename= " + storeName.storeName);
  socket.socket.emit("join", {username: nickname.nickName, store: storeName.storeName});
  // socket.socket.emit("join", {username: this.nickname.nickName, store: this.storeName.storeName});
  await setHandlers();
}

export const setHandlers = async () => {
  socket.socket.on("message", (data) => {
    // const {storeName, msg} = data;
    // console.log("got msg!")
    // list of msgs

    // const msgs = JSON.parse(data).messages;
     const msg = data['messages'];
    // alert(msg)
    Notifications.addNotification(msg, "regular", "", "")
    
    console.log(msg);
  //   this.gui.add_notification(msgs); // TODO - tell einat to add this func
  //   <OpenStore msg={msgs} />
  });
  socket.socket.on("agreement", (data) => {
    const msg = data['messages'];
    // alert(msg)
    Notifications.addNotification(msg, "agreement", data['username'], data['store'])

    // socket.socket.io.emit("subscribe", { username: username, room: storename });
    //  maybe:         socket.emit("subscribe", { username: {username}, room: {storename} });
  });
};

export const disconnect = () => {
// disconnect (username, storename){
  // this.socket.emit("unsbscribe", { username: username, room: storename });
  socket.socket.emit("unsubscribe", { username: this.nickname.nickname });
  // socket.socket.emit("unsubscribe", JSON.parse({ username: this.nickname.nickname }));
}

export const register_new_store = (username, storename) => {
// export const register_new_store = (storename) => {
  console.log("on register store");
  if (counter.counter === 1)
    console.log("call set handlers");
    setHandlers();
  socket.socket.emit("join", { username: username, store:storename });
  // else
  //   alert("there were'nt init!!")
}

