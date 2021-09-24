import {camelCase} from "lodash";
import { useQuery } from "react-query";
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

  const useFetchData = (
    url: string,
    options = {},
    deps: any = [],
    isRefetchByUrl = true,
  ): any => {
    const { isLoading, error, data } = useQuery(
      [...(isRefetchByUrl ? [url] : []), ...deps],
      async () => {
        return fetch(url, {
          headers: {
            'Content-Type': 'application/json',
          },
          ...options,
        }).then((res) => res.json());
      },
      {
        enabled: true,
        staleTime: 30000,
        cacheTime: 0,
      },
    );
    return { isLoading, error, apiResponse: data };
  };
  export default useFetchData;