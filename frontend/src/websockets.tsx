import io from 'socket.io-client';

const WEBSOCKETHOST = '127.0.0.1';
const WEBSOCKETPORT = '5001'

export function initializeWebsocket(addData: (message: any) => void) {
  const newSocket = io(`http://${WEBSOCKETHOST}:${WEBSOCKETPORT}`);
  newSocket.on('connect', () => {
    console.log("connected")
  });
  newSocket.on('message', (data: any) => {
    console.log(data)
    addData(data)
  });
}
