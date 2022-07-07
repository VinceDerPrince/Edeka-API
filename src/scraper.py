from typing import Dict
import requests

url = "https://www.edeka.de/api/offers"

def get_offers() -> Dict:
    querystring = {"limit":"999","marketId":"8000224"}

    payload = ""
    headers = {
        "authority": "www.edeka.de",
        "accept": "*/*",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "JSESSIONID=73B49B35BC12FD77636EFEC0A8AF2C96; EDEKA_LB=\u0021NxPec/7gSkW196xn454CmYg6L5gfcNqlG2mHOfi3qYcuvFyoB+GxZ1yp37uqqfFxrHNX9+jcX7MMxPibiJ0s1+QQJn2E7SkkGk8Hv1lV2yMsNfBA5ZgE/QQ0zNbFHCNbrBl71yU5WQA8oLwJvvdAxATmTEdt+aY=; TCPID=1227412445410774795247; EDEKA_PRIVACY=0@046@1%2C3%2C2%2C8%2C4%2C5%2C6%2C7@91@1657190696877@; EDEKA_PRIVACY_CENTER=1%2C3%2C2%2C8%2C4%2C5%2C6%2C7; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22c22feada-301d-4657-85f2-ad5aae411427%22%2C%22options%22%3A%7B%22end%22%3A%222023-08-08T10%3A44%3A56.885Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _gcl_au=1.1.513519246.1657190697; _pin_unauth=dWlkPU5EaGpNekF5TWpjdFl6azJNQzAwTjJNeExUaGtOMll0WTJVellXWXlaRFJoTXpReA",
        "referer": "https://www.edeka.de/eh/nord/edeka-boldt-kaiser-friedrich-ufer-30/angebote.jsp",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
    }

    r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = r.json()
    
    offers = dict()
    n = 1
    for offer in data["offers"]:
        offers[n] = {
            "name": offer["title"],
            "id": offer["id"],
            "price": offer["price"]["value"],
            "discount": offer["discountInPercentage"],
            "description": offer["descriptionApp"],
            "category": offer["category"]["name"],
            "validTill": offer["validTill"]
        }
        n += 1
    
    return offers

print(get_offers())