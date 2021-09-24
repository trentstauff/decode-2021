import React, { useEffect } from "react";
import Globe from "react-globe.gl";
import newImage from "./dotsGlobe.png";
import backgroundImage from "./background.png";
//import * as THREE from 'three';
import "./App.css";
import { initializeWebsocket } from "./websockets";

const BATCHINTERVAL = 120000;

function App() {
  let batch = [];
  const addData = (data) => {
    batch.push(data);
  };

  const flushBatch = () => {
    setInterval(() => {
      if (batch) {
        // call setTransactionData(batch)
        console.log("batch ", batch);
        batch = [];
      }
    }, BATCHINTERVAL);
  };

  useEffect(() => {
    initializeWebsocket(addData);
    flushBatch();
  }, []);

  const N = 20;
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
      showAtmosphere={false}
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
