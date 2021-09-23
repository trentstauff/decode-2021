/*
Test websocket server
*/

const webSocketsServerPort = 8000;
const webSocketServer = require('websocket').server;
const http = require('http');
// Spinning the http server and the websocket server.
const server = http.createServer();
server.listen(webSocketsServerPort);
const wsServer = new webSocketServer({
  httpServer: server
});

wsServer.on('request', function(request) {
  var connection = request.accept(null, request.origin);
  console.log((new Date()) + ' Recieved a new connection from origin ' + request.origin + '.');
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            console.log('Received Message: ' + message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
            connection.sendUTF(message.utf8Data);
        }
        else if (message.type === 'binary') {
            console.log('Received Binary Message of ' + message.binaryData.length + ' bytes');
            connection.sendBytes(message.binaryData);
        }
    });
});