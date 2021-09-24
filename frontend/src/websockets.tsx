import io from 'socket.io-client';
import {camelizeKeys} from "./helpers";

const WEBSOCKETHOST = '127.0.0.1';
const WEBSOCKETPORT = '5001'

export function initializeWebsocket(addData: (message: any) => void) {
  const newSocket = io(`http://${WEBSOCKETHOST}:${WEBSOCKETPORT}`);
  newSocket.on('connect', () => {
    console.log("connected")
  });
  newSocket.on('message', (data: string) => {
    const rawTransaction = JSON.parse(data)
    const transaction = camelizeKeys(rawTransaction)
    console.log(transaction)
    addData(transaction)
  });
}
