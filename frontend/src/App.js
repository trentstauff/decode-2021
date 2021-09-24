import React from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import World from './World.js'
import './App.css';



export class App extends React.Component {

  // state={
  //   arcsData:[
  //     {
  //       startLat: (Math.random() - 0.5) * 180,
  //       startLng: (Math.random() - 0.5) * 360,
  //       endLat: (Math.random() - 0.5) * 180,
  //       endLng: (Math.random() - 0.5) * 360,
  //       color: ['#faac6e', '#c3a156', '#8f924d', '#61804c', '#165556', '#0c2a2d'][Math.floor(Math.random()*5)],
  //       stroke: Math.random()*(1.5-0.2)
  //     },
  //     {
  //       startLat: (Math.random() - 0.5) * 180,
  //       startLng: (Math.random() - 0.5) * 360,
  //       endLat: (Math.random() - 0.5) * 180,
  //       endLng: (Math.random() - 0.5) * 360,
  //       color: ['#faac6e', '#c3a156', '#8f924d', '#61804c', '#165556', '#0c2a2d'][Math.floor(Math.random()*5)],
  //       stroke: Math.random()*(1.5-0.2)
  //     },
  //     {
  //       startLat: (Math.random() - 0.5) * 180,
  //       startLng: (Math.random() - 0.5) * 360,
  //       endLat: (Math.random() - 0.5) * 180,
  //       endLng: (Math.random() - 0.5) * 360,
  //       color: ['#faac6e', '#c3a156', '#8f924d', '#61804c', '#165556', '#0c2a2d'][Math.floor(Math.random()*5)],
  //       stroke: Math.random()*(1.5-0.2)
  //     }
  //   ]
  // }

  


  
  // Updating state with new data mostly works, but now the animation doesn't run
  // The arcs do update every few seconds because of setInterval inside generateArcs function in World.js
  // but the arcs themselves stops animating after they're initially drawn

  state = {arcsData: null};

  insertArcs = () => {
    let arcs = [];

    for(let i=0; i<6; i++){
      let colors = ['#faac6e', '#c3a156', '#8f924d', '#61804c', '#165556', '#0c2a2d']
      
      var arc = {
        startLat: (Math.random() - 0.5) * 180,
        startLng: (Math.random() - 0.5) * 360,
        endLat: (Math.random() - 0.5) * 180,
        endLng: (Math.random() - 0.5) * 360,
        color: colors[Math.floor(Math.random()*5)],
        stroke: Math.random()*(1.5-0.2)
      };

      arcs.push(arc);
    }

    return arcs;
  }

  changeArcs = () => {
    const arc = this.insertArcs();
    this.setState({ arcsData: arc });
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
