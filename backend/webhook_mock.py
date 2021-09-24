import datetime
import time
import random
import json
import requests
import typing
import uuid

from dotenv import load_dotenv, find_dotenv, dotenv_values
from faker import Faker

faker = Faker("en_CA")
Faker.seed(random.randint(0, 1000))


def datetime_to_unix_ms(dt: datetime.datetime) -> int:
    """Convert a Python datetime to a Unix timestamp (in milliseconds)

    Args:
        dt: datetime.datetime
            Date

    Returns: int
        Unix timestamp of the provided date, represented as milliseconds
        since 1970-01-01 00:00:00 GMT
    """
    return int(dt.timestamp() * 1000)


def get_random_address_details() -> typing.Tuple[str, str, str, str]:
    return random.choices(
        [_get_random_can_address_details, _get_random_usa_address_details, _get_random_nat_address_details],
        weights=[0.6, 0.2, 0.2],
        k=1,
    )[0]()


def _get_random_can_address_details():
    return random.choice(
        [
            ("T7E 5G6", "Edson", "AB", "CAN"),
            ("L4G 3R3", "Aurora", "ON", "CAN"),
            ("J0J 8X1", "Montérégie-Est", "QC", "CAN"),
            ("N9Y 4X4", "Kingsville", "ON", "CAN"),
            ("N5H 5S1", "Alymer", "ON", "CAN"),
            ("T7S 0M2", "Whitecourt", "AB", "CAN"),
            ("J1S 5L8", "Windsor", "QC", "CAN"),
            ("V3H 3K3", "Port Moody", "BC", "CAN"),
            ("V1G 4N9", "Dawson Creek", "BC", "CAN"),
        ]
    )


def _get_random_usa_address_details():
    return random.choice(
        [
            ("94086", "Sunnyvale", "CA", "USA"),
            ("92069", "San Marcos", "CA", "USA"),
            ("02026", "Dedham", "MA", "USA"),
            ("11373", "Elmhurst", "NY", "USA"),
            ("30240", "Lagrange", "GA", "USA"),
            ("37660", "Kingsport", "TN", "USA"),
            ("25801", "Beckley", "WV", "USA"),
            ("01902", "Lynn", "MA", "USA"),
        ]
    )

def _get_random_nat_address_details():
    return random.choice(
        [
			("CH46 1QT", "Wirral", " ", "UK"),
            ("SY2 5UT", "Shrewsbury", " ", "UK"),
            ("SM4 5RR", "Morden", " ", "UK"),
            (" ", "Capdepera", " ", "SPAIN"),
            (" ", "Bantayan", " ", "PHILIPPINES"),
            (" ", "Harda", " ", "INDIA"),
            (" ", "Kakau", " ", "GERMANY"),
            (" ", "Muheza", " ", "United Republic of Tanzania"),
            (" ", "Borgoforte", " ", "Italy"),
        ]
    )
	
if __name__ == "__main__":

    while True:

        load_dotenv(find_dotenv())

        NGROK_LINK = dotenv_values(".env")["NGROK_LINK"]

        event = random.choice(["capture.created", "refund.created"])

        event_key = event.split(".")[0]
        transaction_type = event_key.upper()
        currency = random.choice(["CAD", "USD"])
        amount = random.randint(1, 100000)

        cards = [
            "6f00ec41-5d6e-43ad-9b37-7f38b22f0791",
            "4a01cc62-4c6e-46ad-9b37-8f32a44a1234",
            "7a11ec41-5d6e-53cc-9b37-6a45c31f0782",
        ]

        card = cards[random.randint(0, len(cards) - 1)]

        source = get_random_address_details()
        dest = get_random_address_details()

        now_ms = datetime_to_unix_ms(datetime.datetime.now())

        package = {
            "event_type": event,
            "data": {
                event_key: {
                    "EventType": "",
                    "id": str(uuid.uuid4()),
                    "external_id": str(uuid.uuid4()),
                    "transaction_type": transaction_type,
                    "processor_type": "MARQETA",
                    "currency": currency,
                    "merchant_currency": currency,
                    "card_id": card,
                    "ledger_business_id": str(uuid.uuid4()),
                    "affected_authorization_id": str(uuid.uuid4()),
                    "created_at": now_ms,
                    "updated_at": now_ms,
                    "memo": "Approved or completed successfully",
                    "memo_additional_info": "",
                    "amount": amount,
                    "merchant_amount": amount,
                    "affected_capture_id": "",
                    "refund_state": "",
                },
                "merchant_details": {
                    "name": faker.company(),
                    "mcc": "5812",
                    "mid": "211366",
                    "postal_code": dest[0],
                    "state": dest[2],
                    "city": dest[1],
                    "country_code": dest[3],
                },
                "business_details": {
                    "name": faker.company(),
                    "postal_code": source[0],
                    "state": source[2],
                    "city": source[1],
                    "country_code": source[3],
                },
            },
        }

        package = json.dumps(package)

        res = requests.post(NGROK_LINK + "/webhook", package)
        time.sleep(0.3)

