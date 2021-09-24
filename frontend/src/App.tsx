import React, { useEffect } from "react";
import Globe from "react-globe.gl";
import newImage from "./dotsGlobe.png";
import backgroundImage from "./background.png";
import "./App.css";
import { initializeWebsocket } from "./websockets";
import {GlobeProvider, useGlobe} from "./context";
import {camelizeKeys, convertTransactionsFromDjango} from "./helpers";
import {RawTransaction, TransactionData} from "./types";
import * as three from 'three';


function App() {
  return (
    <GlobeProvider>
      <GlobeContainer/>
    </GlobeProvider>
  )
}

const BATCHINTERVAL = 60000;

function convertTransactionToArcData(t: TransactionData): object {
  return {
      startLat: t.data.businessDetails.latitude,
      startLng: t.data.businessDetails.longitude,
      endLat: t.data.merchantDetails.latitude,
      endLng: t.data.merchantDetails.longitude,
      color: ["#222", "#333", '#444'],
  }
}

const GlobeContainer = () => {
  const { setTransactions, state } = useGlobe();
  const { transactions: currentBatch } = state;

  let newBatch: TransactionData[] = [];
  const addData = (data: TransactionData) => {
    console.log('adding to batch...')
    newBatch.push(data);
  }

  const flushBatch = () => {
    setInterval(() => {
      if (newBatch != []) {
        console.log("batch ", newBatch)
        setTransactions(newBatch)
        newBatch = [];
      }
    }, BATCHINTERVAL);
  }

  useEffect(() => {
    initializeWebsocket(addData)
    flushBatch()
  }, [])

  const arcsData = currentBatch.map(t => convertTransactionToArcData(t));

  return (
    <Globe
      globeImageUrl={newImage}
      bumpImageUrl="//unpkg.com/three-globe/example/img/earth-topology.png"
      arcsData={arcsData}
      arcColor={"color"}
      arcDashLength={1}
      arcDashGap={1}
      arcStroke={0.5}
      arcDashAnimateTime={() => Math.random() * 4000 + 500}
      backgroundImageUrl={backgroundImage}/>
  )

}

export default App;
