import React from "react";
import Globe from "react-globe.gl";
import newImage from "./163243843914973495.jpg";
import backgroundImage from "./Screen Shot 2021-09-23 at 7.35.47 PM.png";
//import * as THREE from 'three';
import "./App.css";

function App() {
  const N = 50;
  const arcsData = [...Array(N).keys()].map(() => ({
    startLat: (Math.random() - 0.5) * 180,
    startLng: (Math.random() - 0.5) * 360,
    endLat: (Math.random() - 0.5) * 180,
    endLng: (Math.random() - 0.5) * 360,
    color: [
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
      ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
    ],
  }));

  return (
    <Globe
      globeImageUrl={newImage}
      bumpImageUrl="//unpkg.com/three-globe/example/img/earth-topology.png"
      arcsData={arcsData}
      arcColor={"color"}
      arcDashLength={() => Math.random()}
      arcDashGap={() => Math.random()}
      arcDashAnimateTime={() => Math.random() * 4000 + 500}
      backgroundImageUrl={backgroundImage}
    />
  );
}

export default App;
