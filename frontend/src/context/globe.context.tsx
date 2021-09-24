import React from "react";
import { defaultGlobeState, GlobeReducer, GlobeStateDispatch } from "./globe.reducer";

const GlobeContext = React.createContext<GlobeStateDispatch>(null);

type GlobeProviderProps = {
    children: React.ReactNode;
}

export const GlobleProvider = (props: GlobeProviderProps) => {
    const [state, dispatch] = React.useReducer(GlobeReducer, defaultGlobeState);
    const value = React.useMemo(()=>({state, dispatch}), [state]);
    
}