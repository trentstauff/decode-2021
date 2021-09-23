import React from 'react';
import { useEffect, useState } from 'react';
import { initializeWebsocket } from '../composables/websockets';

export default function WebSocket() {
  const [data, setData] = useState("");

  useEffect(() => {
    initializeWebsocket(setData);
  }, []);
  
  return (
    <div>
      Practical Intro To WebSockets. Last message: {data}
    </div>
  );
}
