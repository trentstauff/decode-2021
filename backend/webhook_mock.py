import time
import random
import json
import requests
from dotenv import load_dotenv, find_dotenv, dotenv_values

if __name__ == "__main__":
    
    while True:
        
        load_dotenv(find_dotenv())

        NGROK_LINK = dotenv_values(".env")['NGROK_LINK']
        
        event = random.choice(["capture.created", "refund.created"])

        event_key = event.split(".")[0]
        transaction_type = event_key.upper()
        currency = random.choice(["CAD", "USD"])
        amount = random.randint(1, 100000)

        locations = [("T7E 5G6", "Edson", "AB", "CAN"), ("L4G 3R3", "Aurora", "ON", "CAN"), ("J0J 8X1", "Montérégie-Est", "QC", "CAN"), ("N9Y 4X4", "Kingsville", "ON", "CAN"),
        ("N5H 5S1", "Alymer", "ON", "CAN"), ("T7S 0M2", "Whitecourt", "AB", "CAN"), ("J1S 5L8", "Windsor", "QC", "CAN"),("V3H 3K3", "Port Moody", "BC", "CAN"),
        ("94086", "Sunnyvale", "CA", "USA"), ("92069", "San Marcos", "CA", "USA"), ("02026", "Dedham", "MA", "USA"), ("11373", "Elmhurst", "NY", "USA"),
        ("30240", "Lagrange", "GA", "USA"), ("37660", "Kingsport", "TN", "USA"), ("25801", "Beckley", "WV", "USA"), ("01902", "Lynn", "MA", "USA")]
        
        cards = ["6f00ec41-5d6e-43ad-9b37-7f38b22f0791", "4a01cc62-4c6e-46ad-9b37-8f32a44a1234", "7a11ec41-5d6e-53cc-9b37-6a45c31f0782"]

        card = cards[random.randint(0, len(cards)-1)]

        source = locations[random.randint(0, len(locations)-1)]
        dest = locations[random.randint(0, len(locations)-1)]

        package = {
        "event_type": event,
        "data": {
            event_key: {
                "EventType": "",
                "id": "09f2d5a0-1ad1-4817-a5e9-e5c8581d12c6",
                "external_id": "09f2d5a0-1ad1-4817-a5e9-e5c8581d12c6",
                "transaction_type": transaction_type,
                "processor_type": "MARQETA",
                "currency": currency,
                "merchant_currency": currency,
                "card_id": card,
                "ledger_business_id": "62116bbc-d9c7-4d20-a61b-1b8af34d3976",
                "affected_authorization_id": "46f23479-1c56-45dc-ad4d-24651fe9e090",
                "created_at": 1632422976709,
                "updated_at": 1632422977059,
                "memo": "Approved or completed successfully",
                "memo_additional_info": "",
                "amount": amount,
                "merchant_amount": amount,
                "affected_capture_id": "",
                "refund_state": ""
            },
            "merchant_details": {
                "name": random.choice(["Best Buy", "Float", "Google", "Trent"]),
                "mcc": "5812",
                "mid": "211366",
                "postal_code": source[0],
                "state": source[2],
                "city": source[1],
                "country_code": source[3]
            },
            "business_details": {
                "name": random.choice(["Properly Homes", "Deloitte", "KOHO", "1Password"]),
                "postal_code": source[0],
                "state": source[2],
                "city": source[1],
                "country_code": source[3]
            }   
            }
        }

        package = json.dumps(package)

        res = requests.post(NGROK_LINK, package)

        time.sleep(0.1)
        
