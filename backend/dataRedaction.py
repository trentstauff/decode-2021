import json
from geocoding import findLatLng

captureObject = '''
{
	"event_type": "refund.created",
	"data": {
		"refund": {
			"EventType": "",
			"id": "eb6a1ae5-7871-44ed-86bc-33ed65b4b702",
			"external_id": "eb6a1ae5-7871-44ed-86bc-33ed65b4b702",
			"transaction_type": "REFUND",
			"processor_type": "MARQETA",
			"currency": "CAD",
			"merchant_currency": "CAD",
			"card_id": "83ee6a4d-2aa3-44df-acd4-f459e365c53e",
			"ledger_business_id": "edff2b42-dd97-46df-b33a-2a694ed7b4d3",
			"affected_authorization_id": "",
			"created_at": 1632404370600,
			"updated_at": 1632404370692,
			"memo": "Approved or completed successfully",
			"memo_additional_info": "",
			"amount": 10995,
			"merchant_amount": 10995,
			"affected_capture_id": "",
			"refund_state": ""
		},
		"merchant_details": {
			"name": "SP * MVR PLUS",
			"mcc": "5734",
			"mid": "KEDRFVOABOSI2VZ",
			"postal_code": "00918",
			"state": "ON",
			"city": "TORONTO",
			"country_code": "CA"
		},
		"business_details": {
			"name": "Properly Homes",
			"postal_code": "K6J 3P5",
			"state": "67",
			"city": "Cornwall",
			"country_code": "CAN"
		}
	}
}
'''

def ConvertWebhookToWebsocketEvent(jsonString: str, target: str):
	# To read json from a string
	data = json.loads(jsonString)

	newData = {}
	newData['target'] = target
	locationLookup = ""

	# dataKeys = ["capture", "merchant_details", "business_details"]
	dataKeys = list(data['data'].keys())
	print(dataKeys)
	outerDataKeys = list(data)

	# dataCaptureKeys = list(data['data']['capture'])
	captureDetailKeys = ["EventType", "transaction_type", "currency", "merchant_currency", "created_at", "updated_at", "amount", "merchant_amount"]

	# Merchant is the seller/corporation, business is the customer
	dataMerchantKeys = list(data['data']['merchant_details'])
	locationData = ["postal_code", "city", "country_code"]
	dataBusinessKeys = list(data['data']['business_details'])

	for outerDataKey in outerDataKeys:
		if outerDataKey == "event_type":
			newData['event_type'] = data['event_type']
		elif outerDataKey == "data":
			newData['data'] = {}
			for dataKey in dataKeys:
				locationLookup = ""
				if dataKey == "capture":
					newData['data']['capture'] = {}
					dataCaptureKeys = list(data['data']['capture'])
					for dataCaptureKey in dataCaptureKeys:
						if dataCaptureKey in captureDetailKeys:
							newData['data']['capture'][dataCaptureKey] = data['data']['capture'][dataCaptureKey]
				elif dataKey == "refund":
					newData['data']['refund'] = {}
					dataCaptureKeys = list(data['data']['refund'])
					for dataCaptureKey in dataCaptureKeys:
						if dataCaptureKey in captureDetailKeys:
							newData['data']['refund'][dataCaptureKey] = data['data']['refund'][dataCaptureKey]
				elif dataKey == "merchant_details":
					newData['data']['merchant_details'] = {}
					for dataMerchantKey in dataMerchantKeys:
						if dataMerchantKey in locationData:
							locationLookup += data['data']['merchant_details'][dataMerchantKey] + " "
					lat, lng = findLatLng(locationLookup)
					newData['data']['merchant_details']['latitude'] = lat
					newData['data']['merchant_details']['longitude'] = lng
				elif dataKey == "business_details":
					newData['data']['business_details'] = {}
					for dataBusinessKey in dataBusinessKeys:
						if dataBusinessKey in locationData:
							locationLookup += data['data']['business_details'][dataBusinessKey] + " "
					lat, lng = findLatLng(locationLookup)
					newData['data']['business_details']['latitude'] = lat
					newData['data']['business_details']['longitude'] = lng

	if target == "DASHBOARD":
		newData['data']['business_details']['name'] = data['data']['business_details']['name']
		newData['data']['merchant_details']['name'] = data['data']['merchant_details']['name']

	return newData

print(ConvertWebhookToWebsocketEvent(captureObject, "DASHBOARD"))