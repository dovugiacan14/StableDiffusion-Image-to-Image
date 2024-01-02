import requests
import logging
import traceback
from config import DOMAIN, PORT, INTERROGATE 


def interrogate(image):
    url = DOMAIN + ":" + str(PORT) + INTERROGATE
    payload = {
        "image": image,
        "model": "deepdanbooru"
        }
    
    try: 
        headers = "Content-Type: application/json"
        response = requests.post(url= url, headers= headers, json= payload)

        if response.status_code == 200:
            response_json = response.json()
            print("Interrogate Succesfuly.!")
        else:
            print("Error when captioning.!")
            traceback.print_exc()
            return
        
        if "caption" not in response_json:
            return None
        text = response_json.get("caption")
        return text 
    
    except Exception as e:
        logging.error(f"Error when captioning: {e}")
        return None