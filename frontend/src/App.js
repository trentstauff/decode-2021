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
        color: '#ffffff',
        stroke: 5
      },
      {
        startLat: 70,
        startLng: 100,
        endLat: 300,
        endLng: 360,
        color: '#ffff00',
        stroke: .2
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: '#7fab00',
        stroke: 2
      },
      {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: '#38601e',
        stroke: 1
      },
    ],
    // arcsColor:['#ffffff', '#ffff00', '#7fab00', '#38601e'],
    // arcsStroke: [5, 1, 1, 1]
  };

  changeArcs(arcs){
    this.setState({arcsData: arcs})
  }

  render(){
    return(
      <World
      arcsData={this.state.arcsData}
      // arcsColor={this.state.arcsColor}
      // arcsStroke={this.state.arcsStroke}
      changeArcs={this.changeArcs}
      />
    );
  }
};

export default App;
