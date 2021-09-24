// import { w3cwebsocket as W3CWebSocket } from "websocket";
import io from 'socket.io-client';

const WEBSOCKETHOST = '127.0.0.1';
const WEBSOCKETPORT = '5001'

export function initializeWebsocket(setData: (message: any) => void) {
  const newSocket = io(`http://${WEBSOCKETHOST}:${WEBSOCKETPORT}`);
  newSocket.on('connect', () => {
    console.log("connected")
    // newSocket.send("message")
  });
  newSocket.on('message', (data: any) => {
    console.log(data)
    setData(data)
  });
  // const client = new W3CWebSocket('ws://'+WEBSOCKETHOST+':'+WEBSOCKETPORT);
  // client.onopen = () => {
  //   console.log('WebSocket Client Connected');
  //   client.send("Initialized")
  // };
  // client.onmessage = (message) => {
  //   console.log(message);
  //   setData(message.data);
  // };
}