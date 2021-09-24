import React from "react";
import { TransactionData } from "../types";
import {GlobeActionId, GlobeActionTypes} from "./types";

type DispatchType = React.Dispatch<GlobeActionTypes>;

export const fetchTransactionsInit = (dispatch: DispatchType)  => () => {
    dispatch({type: GlobeActionId.FETCH_TRANSACTIONS_INIT})
}

export const fetchTransactionsSuccess = (dispatch: DispatchType) => ()=>{
    dispatch({type: GlobeActionId.FETCH_TRANSACTIONS_SUCCESS})
}

export const fetchTransactionsFailure = (dispatch: DispatchType) => () => {
    dispatch({type: GlobeActionId.FETCH_TRANSACTIONS_FAILURE})
}

export const setTransactions = (dispatch: DispatchType) => (transactions: TransactionData[]) =>{
    dispatch({
        type: GlobeActionId.SET_TRANSACTIONS,
        payload: transactions,
    })
}