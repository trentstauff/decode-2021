import json
from geocoding import findLatLng

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