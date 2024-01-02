import logging 
import requests
import io
import base64 
from pathlib import Path 
from typing import Dict, List 
from PIL import Image, PngImagePlugin
from config import DOMAIN, PORT, PNG_INFO


def save_img(images: List, output_file: Path):
    logging.info("Start saving image...") 
    url = DOMAIN + ":" + str(PORT) + PNG_INFO
    headers = "Content-Type: application/json"
    try:
        if images is None: 
            return None 
        for img in images: 
            image = Image.open(io.BytesIO(base64.b64decode(img.split(",",1)[0])))
            png_payload = {
                "image": "data:image/png;base64," + img
            }
            response2 = requests.post(url= url, headers= headers, json= png_payload)

            pnginfo = PngImagePlugin.PngInfo()
            if "info" not in response2.json():
                return None
            pnginfo.add_text("parameters", response2.json().get("info"))

            # saving image 
            image.save(output_file ,"PNG", pnginfo= pnginfo)
        
    except Exception as e: 
        logging.error(f"Error when saving image: {e}")
        return None
    finally: 
        logging.info("Finish saving image.!")