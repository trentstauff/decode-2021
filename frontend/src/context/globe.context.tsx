import React from "react";
import { useFetchData } from "../helpers";
import { fetchTransactionsFailure, fetchTransactionsInit, fetchTransactionsSuccess, setTransactions } from "./globe.actions";
import { defaultGlobeState, GlobeReducer, GlobeStateDispatch } from "./globe.reducer";

const GlobeContext = React.createContext<GlobeStateDispatch | null>(null);

type GlobeProviderProps = {
    children: React.ReactNode;
}

export const GlobeProvider = (props: GlobeProviderProps) => {
    const [state, dispatch] = React.useReducer(GlobeReducer, defaultGlobeState);
    const value = React.useMemo(()=>({state, dispatch}), [state]);
    return <GlobeContext.Provider value={value} {...props} />
}

export const useGlobe = ()=>{
    const context = React.useContext(GlobeContext);
    if(!context){
        throw new Error("please put useGlobe within the GloveProvider");
    }
    const {state, dispatch} = context;
    return{
        state,
        dispatch,
        setTransactions: setTransactions(dispatch),
    }
}