# Image to Image - Test 

## OVERVIEW 
    In this repository, we provide a source code to test Stable Diffusion's image to image functionality via API. We include testing capabilities for both single payload and all payloads. 

## PRE-REQUISITS 
First, you have to start Stable Diffusion Web UI. 

If any of these packages are not installed on your computer, you can install them using the supplied requirements.txt file: 
>        pip install -r requirements.txt

## INSTALL 
1. Here, how to test one payload: 
    * In `config.py`, locate the IMG variable.
    * Enter the relative path of your image into the `IMG` variable.
    * Customize your payload configuration within the `PAYLOAD` variable.
Run: 
>       python single_test.py 

**NOTE:** Payload can be found in Payload folder. 

2. To test all payloads: 
    * In `config.py`, locate the IMG variable.
    * Enter the relative path of your image into the `IMG` variable.
    * Prepare a folder named `result` that have the similar structure with folder `Payload`. 

Run: 
>       pythonn all_test.py 








