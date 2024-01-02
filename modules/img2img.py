import io 
import base64 
import logging 
import requests
from PIL import Image
from pathlib import Path 
from typing import Dict


class IMG2IMG: 
    def __init__(self, img:Path):
        self.img = img 

    def img2img(self, url, payload: Dict):
        logging.info("Starting img2img")
        try: 
            headers = "Content-Type: application/json"
            payload["init_images"].append(self.pil_to_base64())
            response = requests.post(url= url, headers= headers, json= payload)
        
            if response.status_code == 200:
                r = response.json()
                if "images" not in r:
                    return None
                return r["images"]
            return None 
    
        except Exception as e: 
            logging.error(f"Error when img2img: {e}")
            return None
    
    def pil_to_base64(self):
        try: 
            im = Image.open(self.img)
            img_bytes = io.BytesIO()
            im.save(img_bytes, format='PNG')
            img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
            return img_base64
        except Exception as e:
            logging.error(f"Error converting PIL image to base64: {e}")
            return None

