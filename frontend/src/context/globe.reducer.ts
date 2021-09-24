import { Dispatch } from "react";
import { TransactionData } from "../types";
import { GlobeActionId, GlobeActionTypes } from "./types";

export type GlobeState = {
    isLoading: boolean;
    isError: boolean;
    isInitialized: boolean;
    transactions: TransactionData[];
}

export type GlobeStateDispatch = {
    state: GlobeState;
    dispatch: React.Dispatch<GlobeActionTypes>
}

export const defaultGlobeState: GlobeState = {
    isLoading: false,
    isError: false,
    isInitialized: false,
    transactions: [],
}

export const GlobeReducer = (
    state: GlobeState,
    action: GlobeActionTypes,
): GlobeState=>{
    switch(action.type){
        case GlobeActionId.FETCH_TRANSACTIONS_INIT: {
            return {
                ...state,
                isLoading: true,
                isError: false,
            }
        }
        case GlobeActionId.FETCH_TRANSACTIONS_SUCCESS: {
            return {
                ...state,
                isLoading: false,
                isError: false,
            }
        }
        case GlobeActionId.FETCH_TRANSACTIONS_FAILURE: {
            return {
                ...state,
                isLoading: false,
                isError: true,
            }
        }
        case GlobeActionId.SET_TRANSACTIONS: {
            return {
                ...state,
                transactions: action.payload
            }
        }
        default: {
            throw new Error("unsupported action type")
        }
    }
}