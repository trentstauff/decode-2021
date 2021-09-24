import json
from geocoding import findLatLng

captureObject = '''
{
	"event_type": "capture.created",
	"data": {
		"capture": {
			"EventType": "",
			"id": "09f2d5a0-1ad1-4817-a5e9-e5c8581d12c6",
			"external_id": "09f2d5a0-1ad1-4817-a5e9-e5c8581d12c6",
			"transaction_type": "CAPTURE",
			"processor_type": "MARQETA",
			"currency": "CAD",
			"merchant_currency": "CAD",
			"card_id": "6f00ec41-5d6e-43ad-9b37-7f38b22f0791",
			"ledger_business_id": "62116bbc-d9c7-4d20-a61b-1b8af34d3976",
			"affected_authorization_id": "46f23479-1c56-45dc-ad4d-24651fe9e090",
			"created_at": 1632422976709,
			"updated_at": 1632422977059,
			"memo": "Approved or completed successfully",
			"memo_additional_info": "",
			"amount": 1384,
			"merchant_amount": 1384,
			"affected_capture_id": "",
			"refund_state": ""
		},
		"merchant_details": {
			"name": "SQ *TILLYS",
			"mcc": "5812",
			"mid": "211366",
			"postal_code": "K6J 3P5",
			"state": "67",
			"city": "Cornwall",
			"country_code": "CAN"
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

	dataKeys = ["capture", "merchant_details", "business_details"]
	outerDataKeys = list(data)

	dataCaptureKeys = list(data['data']['capture'])
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
					for dataCaptureKey in dataCaptureKeys:
						if dataCaptureKey in captureDetailKeys:
							newData['data']['capture'][dataCaptureKey] = data['data']['capture'][dataCaptureKey]
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