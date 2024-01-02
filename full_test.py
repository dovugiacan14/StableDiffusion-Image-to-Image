import requests
from PIL import Image,PngImagePlugin
import base64
import io
import json
import os 
import traceback
import logging 
from config import *
from pathlib import Path
from typing import Dict, List

def pil_to_base64(img):
    try: 
        im = Image.open(img)
        img_bytes = io.BytesIO()
        im.save(img_bytes, format='PNG')
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        return img_base64
    except Exception as e:
        logging.error(f"Error converting PIL image to base64: {e}")
        return None


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


def img2img(url, img_test: Path, payload: Dict):
    logging.info("Starting img2img")
    try: 
        headers = "Content-Type: application/json"
        payload["init_images"].append(pil_to_base64(img_test))
        response = requests.post(url= url, headers= headers, json= payload)
    
        if response.status_code == 200:
            r = response.json()
            if "images" not in r:
                return None
            return r["images"]
        return None 

    except Exception as e: 
        logging.error(f"Error when excuting img2img: {e}")
        return None


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
            image.save(output_file, pnginfo= pnginfo)
            
    except Exception as e: 
        logging.error(f"Error when saving image: {e}")
        return None
    finally: 
        logging.info("Finish saving image.!")


def main():
    domain   = DOMAIN + ":" + str(PORT) + IMG2IMG
    img_test = IMG
    folders  = ["2DCharacteristic", "3DCartoon","3DRealistic", "Halloween"]

    for folder in folders:
        file_list = os.listdir(folder)
        for i, file_name in enumerate(file_list, start= 1):
            output_path = file_name.replace('.json', "") 
            url = os.path.join(folder, file_name)
            with open(url) as f:
                payload = json.load(f)
                # payload['prompt'] = interrogate(pil_to_base64(img_test))
            
            images = img2img(domain, img_test, payload)
            output_file = f"result/{folder}/{output_path}_{i}.png"
            save_img(images, output_file)

                
if __name__ == "__main__":
    main()
