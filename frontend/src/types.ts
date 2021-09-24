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

export type DjangoCapture = {
    EventType: string;
    transaction_type: "CAPTURE";
    currency: Currency;
    merchant_currency: Currency;
    created_at: number;
    updated_at: number;
    amount: number;
    merchant_amount: number;
}

export type DjangoDetails = {
    longitude: number;
    latitude: number;
    name: string;
}


export type TransactionData = {
    target: string;
    eventType: string;
    data: {
        capture: Capture;
        merchantDetails: Detail;
        businessDetails: Detail;
    }
}

export type RawTransaction = {
    target: string;
    event_type: string;
    data: {
        capture: DjangoCapture;
        merchant_details: DjangoDetails;
        business_details: DjangoCapture;
    }
}