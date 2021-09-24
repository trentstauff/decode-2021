import React from "react";
import { useState, useEffect } from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import countries from './countries.geojson';
import earth from './earth-blue.png'

const World = (props) => {
    let [countries, setCountries] = useState({ features: []});

    useEffect(() => {
      // load data
      fetch(countries).then(res => res.json()).then(setCountries);
    }, []);

    console.log(countries);

    // const N = 1;
    // const arcsData = [...Array(N).keys()].map(() => ({
    //   startLat: (Math.random() - 0.5) * 180,
    //   startLng: (Math.random() - 0.5) * 360,
    //   endLat: (Math.random() - 0.5) * 180,
    //   endLng: (Math.random() - 0.5) * 360,
    //   color: [['#ffffff','#ffff00', '#7fab00', '#38601e'][Math.round(Math.random() * 3)], ['#ffffff', '#ffff00', '#7fab00', '#38601e'][Math.round(Math.random() * 3)]]
    // }));

    const arcsData = props.arcsData;

    return (<div>
        <Globe
      globeImageUrl={earth}

      showGraticules={false}
      atmosphereColor={'#049FDD'}
      backgroundColor={'#00222f'}

      arcsData={arcsData}
      arcColor={'color'}
      arcStroke={1}
      arcCircularResolution={10}
      arcDashLength={.7}
      arcDashGap={.3}
      arcDashAnimateTime={1000}

      hexPolygonsData={countries.features}
      hexPolygonResolution={3}
      hexPolygonMargin={0.3}
      hexPolygonColor={() => `#${Math.round(Math.random() * Math.pow(2, 24)).toString(16).padStart(6, '0')}`}
      hexPolygonLabel={({ properties: d }) => `
        <b>${d.ADMIN} (${d.ISO_A2})</b> <br />
        Population: <i>${d.POP_EST}</i>
      `}
    />
    {/* <input onChange={props.changeArcs}/> */}
    </div>
    );
  };

  export default World;