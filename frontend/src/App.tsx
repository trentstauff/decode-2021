import React, { useEffect } from "react";
import GlobeRenderer from "react-globe.gl";
import newImage from "./163243843914973495.jpg";
import backgroundImage from "./Screen Shot 2021-09-23 at 7.35.47 PM.png";
//import * as THREE from 'three';
import "./App.css";
import { initializeWebsocket } from "./websockets";
import {GlobeProvider, useGlobe} from "./context";
import {camelizeKeys} from "./helpers";
import {RawTransaction, TransactionData} from "./types";


function App() {
  return (
    <GlobeProvider>
      <GlobeContainer/>
    </GlobeProvider>
  )
}

const BATCHINTERVAL = 120000;

const GlobeContainer = () => {
  const { setTransactions, state } = useGlobe();
  const { transactions: currentTransactionsBatch } = state;

  let newRawTransactionsBatch: RawTransaction[] = [];
  const addData = (data: RawTransaction) => {
    newRawTransactionsBatch.push(data);
  }

  const flushBatch = () => {
    setInterval(() => {
      if (newRawTransactionsBatch) {
        console.log("batch ", newRawTransactionsBatch)
        setTransactions(camelizeKeys(newRawTransactionsBatch))
        newRawTransactionsBatch = [];
      }
    }, BATCHINTERVAL);
  }

  useEffect(() => {
    initializeWebsocket(addData)
    flushBatch()
  }, [])

  // const N = 20;
  // const arcsData = [...Array(N).keys()].map(() => ({
  //   startLat: (Math.random() - 0.5) * 180,
  //   startLng: (Math.random() - 0.5) * 360,
  //   endLat: (Math.random() - 0.5) * 180,
  //   endLng: (Math.random() - 0.5) * 360,
  //   color: [
  //     ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
  //     ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
  //   ],
  // }));

  const arcsData = currentTransactionsBatch.map((t: TransactionData) => ({
    startLat: t.data.businessDetails.latitude,
    startLng: t.data.businessDetails.longitude,
    endLat: t.data.merchantDetails.latitude,
    endLng: t.data.merchantDetails.longitude,
  }));

  return (
    <GlobeRenderer
      globeImageUrl={newImage}
      bumpImageUrl="//unpkg.com/three-globe/example/img/earth-topology.png"
      arcsData={arcsData}
      arcColor={"color"}
      arcDashLength={() => Math.random()}
      arcDashGap={() => Math.random()}
      arcDashAnimateTime={() => Math.random() * 4000 + 500}
      backgroundImageUrl={backgroundImage}/>
  )

}

export default App;
