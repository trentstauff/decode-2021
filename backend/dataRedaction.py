import json
from geocoding import findLatLng

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
	# merchantDetailKeys = ["postal_code", "state", "city", "country_code"]
	dataMerchantKeys = list(data['data']['merchant_details'])
	# businessDetailKeys = ["postal_code", "state", "city", "country_code"]
	locationData = ["postal_code", "city", "country_code"]
	dataBusinessKeys = list(data['data']['business_details'])

	for outerDataKey in outerDataKeys:
		# print(outerDataKey)
		if outerDataKey == "event_type":
			# print(" ", data['event_type'])
			newData['event_type'] = data['event_type']
		elif outerDataKey == "data":
			newData['data'] = {}
			for dataKey in dataKeys:
				locationLookup = ""
				# print(" ", dataKey)
				if dataKey == "capture":
					newData['data']['capture'] = {}
					for dataCaptureKey in dataCaptureKeys:
						# print("     ", dataCaptureKey)
						if dataCaptureKey in captureDetailKeys:
							newData['data']['capture'][dataCaptureKey] = data['data']['capture'][dataCaptureKey]
				elif dataKey == "merchant_details":
					newData['data']['merchant_details'] = {}
					for dataMerchantKey in dataMerchantKeys:
						# print("     ", dataMerchantKey)
						if dataMerchantKey in locationData:
							# newData['data']['merchant_details'][dataMerchantKey] = data['data']['merchant_details'][dataMerchantKey]
							locationLookup += data['data']['merchant_details'][dataMerchantKey] + " "
					lat, lng = findLatLng(locationLookup)
					# print(locationLookup)
					# print(lat, lng)
					newData['data']['merchant_details']['latitude'] = lat
					newData['data']['merchant_details']['longitude'] = lng
				elif dataKey == "business_details":
					# print(newData)
					# print(data)
					newData['data']['business_details'] = {}
					for dataBusinessKey in dataBusinessKeys:
						if dataBusinessKey in locationData:
							# print("     ", dataBusinessKey)
							# newData['data']['business_details'][dataBusinessKey] = data['data']['business_details'][dataBusinessKey]
							locationLookup += data['data']['business_details'][dataBusinessKey] + " "
					lat, lng = findLatLng(locationLookup)
					# print(locationLookup)
					# print(lat, lng)
					newData['data']['business_details']['latitude'] = lat
					newData['data']['business_details']['longitude'] = lng

	if target == "DASHBOARD":
		newData['data']['business_details']['name'] = data['data']['business_details']['name']
		newData['data']['merchant_details']['name'] = data['data']['merchant_details']['name']

	return newData