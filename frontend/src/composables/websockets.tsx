import { w3cwebsocket as W3CWebSocket } from "websocket";

const client = new W3CWebSocket('ws://127.0.0.1:8000');

export function initializeWebsocket(setData: (message: any) => void) {
  client.onopen = () => {
    console.log('WebSocket Client Connected');
  };
  client.onmessage = (message) => {
    console.log(message);
    setData(message);
  };
}