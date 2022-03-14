import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

"""
Example 1. Detect faces from an image (from the web)
"""

API_KEY = "8eecbafb4729456498bf48a11238c58f"
ENDPOINT = "https://aminulface.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))
image_url = "https://lh3.googleusercontent.com/pw/AM-JKLWihuQfkjmAu7AG5xRaoCnB9PI5VI6dZGcXhqVtIMk6L9swLa0M8WziWt0uVOTjTEY03WKKzAppzFt62mbpYT9C5x5n-gI0S8TmfOzUOg2X6CceLspAVqWSKyXN96r7C6YNHSGXUw7xm1wK2utNAAjNXg=w2249-h1686-no?authuser=0"
image_name = os.path.basename(image_url)

response_detected_faces = face_client.face.detect_with_url(
    image_url,
    detection_model='detection_03',
    recognition_model='recognition_04'
)
print(response_detected_faces)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

response_image = requests.get(image_url)
img = Image.open(io.BytesIO(response_image.content))
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)
img.show()
img.save('test.jpg')