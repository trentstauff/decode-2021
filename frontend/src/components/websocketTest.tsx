import React from 'react';
import { useEffect, useState } from 'react';
import { initializeWebsocket } from '../composables/websockets';

type MyProps = {}

type MyState = {
  data: any; // like this
};

export default class WebSocket extends React.Component<MyProps, MyState> {
  addData = (newData: any) => {
    this.setState((state) => ({
      data: newData.startLat,
    }));
  }

  componentDidMount() {
    initializeWebsocket(this.addData);
  }
  
  state: MyState = {
    // optional second annotation for better type inference
    data: 0,
  };

  render() {
    return (
      <div>
        Practical Intro To WebSockets. Last message: {this.state.data}
      </div>
    );
  }
}

export  function WebSocket2() {
  const [data, setData] = useState("Nothing yet");

  useEffect(() => {
    initializeWebsocket(setData);
  }, []);
  
  return (
    <div>
      Practical Intro To WebSockets. Last message: {data}
    </div>
  );
}
