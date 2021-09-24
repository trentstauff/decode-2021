import React, { useEffect } from "react";
import Globe from "react-globe.gl";
import newImage from "./163243843914973495.jpg";
import backgroundImage from "./Screen Shot 2021-09-23 at 7.35.47 PM.png";
import "./App.css";
import { initializeWebsocket } from "./websockets";
import {GlobeProvider, useGlobe} from "./context";
import {camelizeKeys, convertTransactionsFromDjango} from "./helpers";
import {RawTransaction, TransactionData} from "./types";


function App() {
  return (
    <GlobeProvider>
      <GlobeContainer/>
    </GlobeProvider>
  )
}

const BATCHINTERVAL = 20000;

function convertTransactionToArcData(t: TransactionData): object {
  return {
      startLat: t.data.businessDetails.latitude,
      startLng: t.data.businessDetails.longitude,
      endLat: t.data.merchantDetails.latitude,
      endLng: t.data.merchantDetails.longitude,
      color: [
        ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
        ["red", "white", "blue", "green"][Math.round(Math.random() * 3)],
      ],
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
      if (newBatch) {
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
  console.log({arcsData})

  return (
    <Globe
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
