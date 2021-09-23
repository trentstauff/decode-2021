import { w3cwebsocket as W3CWebSocket } from "websocket";

const WEBSOCKETHOST = '127.0.0.1';
const WEBSOCKETPORT = '8000'

export function initializeWebsocket(setData: (message: any) => void) {
  const client = new W3CWebSocket('ws://'+WEBSOCKETHOST+':'+WEBSOCKETPORT);
  client.onopen = () => {
    console.log('WebSocket Client Connected');
    client.send("Initialized")
  };
  client.onmessage = (message) => {
    console.log(message);
    setData(message.data);
  };
}