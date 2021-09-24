import React from "react";
import { useState, useEffect } from 'react';
import Globe from 'react-globe.gl';
import * as THREE from 'three';
import countries from './countries.geojson';
import earth from './earth-blue.png';
import background6 from './background6.png';
import background5 from './background5.png';
import background7 from './background7.png';

const World = (props) => {

    const arcsData = props.arcsData;

    return (<div>
        <Globe
      globeImageUrl={earth}

      showGraticules={false}
      //atmosphereColor={'#83c2db'}
      atmosphereColor={'white'}
      atmosphereAltitude={.25}
      //backgroundColor={'#222222'}
      backgroundImageUrl={background7}

      arcsData={arcsData}
      arcColor={'color'}
      arcStroke={'stroke'}
      arcCircularResolution={10}
      arcDashLength={.5}
      arcDashGap={.5}
      arcDashAnimateTime={3000}

      hexPolygonsData={countries.features}
      hexPolygonResolution={3}
      hexPolygonMargin={0.3}
      hexPolygonColor={() => `#${Math.round(Math.random() * Math.pow(2, 24)).toString(16).padStart(6, '0')}`}
      hexPolygonLabel={({ properties: d }) => `
        <b>${d.ADMIN} (${d.ISO_A2})</b> <br />
        Population: <i>${d.POP_EST}</i>
      `}
    />
    </div>
    );
  };

  export default World;