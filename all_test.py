import os
import json
from config import * 
from modules.img2img import IMG2IMG
from modules.download import save_img 

def main():
    domain =  DOMAIN + ":" + str(PORT) + IMG2IMG
    img_test = IMG
    folders = ["2DCharacteristic", "3DCartoon","3DRealistic", "Halloween", "Christmas", "Painting"]

    for folder in folders:
        file_list = os.listdir(folder)
        for i, file_name in enumerate(file_list, start= 1):
            output_path = file_name.replace('.json', "") 
            url = os.path.join(folder, file_name)
            with open(url) as f:
                payload = json.load(f)
                # payload['prompt'] = interrogate(pil_to_base64(img_test))
            
            img2img = IMG2IMG(img_test)
            images = img2img.img2img(domain, payload)
            output_file = f"result/{folder}/{output_path}_{i}.png"
            save_img(images, output_file)

if __name__ == "__main__":
    main()
