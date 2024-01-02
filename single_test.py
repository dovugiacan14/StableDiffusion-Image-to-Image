import json
from config import * 
from modules.img2img import IMG2IMG
from modules.download import save_img

def main():
    url =  DOMAIN + ":" + str(PORT) + IMG2IMG
    img_test = IMG 
    payload_config = PAYLOAD
    output_file = f"save.png"
    
    with open(payload_config, "r") as f:
        payload = json.load(f)

    img2img = IMG2IMG(img_test)
    images = img2img.img2img(url, payload)
    save_img(images, output_file)


if __name__ == "__main__":
    main()



