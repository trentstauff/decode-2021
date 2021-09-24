export type Detail = {
    longitude: number;
    latitude: number;
    name: string;
}

export enum Currency {
    CAD,
    USD,
    NONE,
}

export type Capture = {
    eventType: string;
    transactionType: "CAPTURE";
    currency: Currency;
    merchantCurrency: Currency;
    createdAt: number;
    updatedAt: number;
    amount: number;
    merchantAmount: number;
}
