import logging, json, base64, io

import boto3
import numpy as np
from PIL import Image, ImageOps, ImageFilter
import cv2

env = "DEV" 
if env == "DEV":
    logging.basicConfig(filename='images.log',level=logging.INFO)
else:
    logging.basicConfig(filename='images.log', level=logging.WARNING)

class PhotoManipulation():
    def __init__(self):
        self.session = boto3.Session(region_name='us-east-1')
        self.bedrock_client = self.session.client(
            service_name='bedrock-runtime',
        )
        self.photo_x: int = 512
        self.photo_y: int = 512
    
    def create_mask(self, photo, image_filename) -> Image:
        logging.info("Creating mask image for photo")
        cv_image = np.array('RGB')
        mask_image = np.zeros((self.photo_x, self.photo_y, 1), dtype = np.uint8)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        face_padding = 25
        for (x, y, w, h) in faces:
            cv2.rectangle(mask_image, (x-face_padding, y-face_padding), (x+w+face_padding, y+h+face_padding), (255, 255, 255), -1)
        
        mask_image = np.squeeze(mask_image, axis=2)

        image_mask = Image.fromarray(mask_image)
        
        if env == "DEV":
            image_mask.save(f"mask_{image_filename}")
        return image_mask
    
    def image_to_base64(self, photo) -> str:
        """Convert a PIL Image or local image file path to a base64 string for Amazon bedrock"""

        photo = photo.convert("RGB", colors=256)

        if isinstance(photo, str):
            if os.path.isfile(photo):
                print(f"Reading image from file: {photo}")
                with open(photo, "rb") as f:
                    return base64.b64encode(f.read()).decode("utf-8")
            else:
                raise FileNotFoundError(f"File not found: {photo}")
        
        elif isinstance(photo, Image.Image):
            print("Converting PIL image to base64 string")
            buffer = io.BytesIO()
            photo.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        eles:
            raise ValueError(f"Expected str (filename) or PIL Image. Got {type(photo)}")
    
    def update_photo(self, photo, mask, image_filename):
        