from typing import Dict
import requests as _requests

url = "https://www.edeka.de/api/offers"

def _generate_url(address: str) -> str:

    url = "https://www.edeka.de/api/marketsearch/markets"

    querystring = {"limit":"999","searchstring":address}

    payload = ""
    r = _requests.request("GET", url, data=payload, params=querystring)
    json = r.json()
    return json["markets"]

def get_offers(adress: str) -> Dict:
    markets = _generate_url(adress)
    complete = dict()
    i = 1
    for market in markets:
        query = dict()
        query["id"] = market["id"]
        query["market"] = market["name"]+" "+market["contact"]["address"]["street"]
        querystring = {"limit":"999","marketId":market["id"]}

        payload = ""
        headers = {
            "authority": "www.edeka.de",
            "accept": "*/*",
            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "cookie": "JSESSIONID=73B49B35BC12FD77636EFEC0A8AF2C96; EDEKA_LB=\u0021NxPec/7gSkW196xn454CmYg6L5gfcNqlG2mHOfi3qYcuvFyoB+GxZ1yp37uqqfFxrHNX9+jcX7MMxPibiJ0s1+QQJn2E7SkkGk8Hv1lV2yMsNfBA5ZgE/QQ0zNbFHCNbrBl71yU5WQA8oLwJvvdAxATmTEdt+aY=; TCPID=1227412445410774795247; EDEKA_PRIVACY=0@046@1%2C3%2C2%2C8%2C4%2C5%2C6%2C7@91@1657190696877@; EDEKA_PRIVACY_CENTER=1%2C3%2C2%2C8%2C4%2C5%2C6%2C7; atuserid=%7B%22name%22%3A%22atuserid%22%2C%22val%22%3A%22c22feada-301d-4657-85f2-ad5aae411427%22%2C%22options%22%3A%7B%22end%22%3A%222023-08-08T10%3A44%3A56.885Z%22%2C%22path%22%3A%22%2F%22%7D%7D; _gcl_au=1.1.513519246.1657190697; _pin_unauth=dWlkPU5EaGpNekF5TWpjdFl6azJNQzAwTjJNeExUaGtOMll0WTJVellXWXlaRFJoTXpReA",
            "referer": market["url"],
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36"
        }

        r = _requests.request("GET", url, data=payload, headers=headers, params=querystring)
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
                #"category": offer["category"]["name"],
                "validTill": offer["validTill"]
            }
            n += 1
    
        query["offers"] = offers
        complete[i] = query
        i += 1
    return complete

print(get_offers("Eppendorfer Baum"))