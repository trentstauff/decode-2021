import React from "react";
import { useFetchData } from "../helpers";
import { fetchTransactionsFailure, fetchTransactionsInit, fetchTransactionsSuccess, setTransactions } from "./globe.actions";
import { defaultGlobeState, GlobeReducer, GlobeStateDispatch } from "./globe.reducer";

const GlobeContext = React.createContext<GlobeStateDispatch>(null);

type GlobeProviderProps = {
    children: React.ReactNode;
}

export const GlobleProvider = (props: GlobeProviderProps) => {
    const [state, dispatch] = React.useReducer(GlobeReducer, defaultGlobeState);
    const value = React.useMemo(()=>({state, dispatch}), [state]);
    const {apiResponse, isLoading, error} = useFetchData();
    if(!state.isInitialized && !state.isLoading &&!state.isError){
        fetchTransactionsInit(dispatch)();
    }
    if(state.isLoading && apiResponse && !isLoading){
        fetchTransactionsSuccess(dispatch)();
    }
    if(error){
        fetchTransactionsFailure(dispatch)();
    }
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