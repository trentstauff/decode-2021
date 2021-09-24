import { TransactionData } from "../types";

export enum GlobeActionId {
    FETCH_TRANSACTIONS_INIT,
    FETCH_TRANSACTIONS_SUCCESS,
    FETCH_TRANSACTIONS_FAILURE,
    SET_TRANSACTIONS,
}

type fetchTransactionsInit = {
    type: GlobeActionId.FETCH_TRANSACTIONS_INIT
}

type fetchTransactionsSuccess = {
    type: GlobeActionId.FETCH_TRANSACTIONS_SUCCESS
}

type fetchTransactionsFailure = {
    type: GlobeActionId.FETCH_TRANSACTIONS_FAILURE
}

type setTransactions = {
    type: GlobeActionId.SET_TRANSACTIONS;
    payload: TransactionData[];
}

export type GlobeActionTypes = fetchTransactionsInit | fetchTransactionsSuccess | fetchTransactionsFailure | setTransactions;