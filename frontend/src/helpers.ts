import {camelCase} from "lodash";
import { DjangoTransaction, TransactionData } from "./types";

export const camelizeKeys = (obj: any): any => {
    if (Array.isArray(obj)) {
      return obj.map((v) => camelizeKeys(v));
    }
    if (obj != null && obj.constructor === Object) {
      return Object.keys(obj).reduce(
        (result, key) => ({
          ...result,
          [camelCase(key)]: camelizeKeys(obj[key]),
        }),
        {},
      );
    }
    return obj;
  };

  export const convertTransactionsFromDjango = (djangoData: DjangoTransaction): TransactionData=> camelizeKeys(djangoData)