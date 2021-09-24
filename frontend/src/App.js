import React from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import World from './World.js'
import './App.css';



export class App extends React.Component {

  state = {
    arcsData:
      [{
        startLat: 120,
        startLng: 300,
        endLat: 0,
        endLng: 100,
        color: '#ffffff'
      },
      {
        startLat: 70,
        startLng: 100,
        endLat: 300,
        endLng: 360,
        color: '#ffff00'
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: '#7fab00'
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: '#38601e'
      },
    ]
  };

  changeArcs(arcs){
    this.setState({arcsData: arcs})
  }

  render(){
    return(
      <World
      arcsData={this.state.arcsData}
      changeArcs={this.changeArcs}
      />
    );
  }
};

export default App;
