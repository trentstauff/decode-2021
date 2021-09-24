import React from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import World from './World.js'
import './App.css';



export class App extends React.Component {

  state = {
    arcsData:
      [{
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#a89a50', '#61804c', '#2a604b', '#0c3e3e','#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#a89a50', '#61804c', '#2a604b', '#0c3e3e','#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#a89a50', '#61804c', '#2a604b', '#0c3e3e','#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#a89a50', '#61804c', '#2a604b', '#0c3e3e','#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#a89a50', '#61804c', '#2a604b', '#0c3e3e','#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: ['#faac6e', '#c3a156', '#8f924d', '#61804c', '#165556', '#0c2a2d'][Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      },
    ],
  };

  // changeArcs(arcs){
  //   this.setState({arcsData: arcs})
  // }

  render(){
    return(
      <World
      arcsData={this.state.arcsData}
      // changeArcs={this.changeArcs}
      />
    );
  }
};

export default App;
