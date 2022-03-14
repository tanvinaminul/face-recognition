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

image_url = "https://lh3.googleusercontent.com/9gmUlDen_p2jgx1mJmQhmV2q7VCzyxGt0YmciixvXfX3J8-TfJCKmEhehZXqxrfbngXRIZdsKRPLry5DcDvRI5ZaHxAkewTOV6H7S0gmyrQvTXQrycjk3Xm-Odf-6U6K7nE6JvUL4_F-xhlT9ce3ONy6n7zhnd6vXuoJvdP01BfWQGt9uqSZpiCpuqctdAxrFQZh1i5wZG1SQVBmaW0aRHajdPruk2z0GknAQbHyb4ZLu_nIfWrh317-1WTRbu1Iv9xbzIV7h8LEFhV1NeG0QWsas3FIJvce3oAk0Pi-x6s8Ran57akvu_Tb68KXzvVhl6nh8yiuUDQ_e2bQ4v8yKV5vXTyo3D0TUqlPMczfJ7GWYD3Ix9WEj6COeutaipGeG5s21OI0XKHbN9AGJc4QF6Qz8KIMUrMWOKYXKbr2zcX8fay6LJCvn9TOheFP9fyD1kRj3DCnXEuZegUObt_cvW8vdTQRzCLMo6aIEjoI_t44FLZRZMBtv3wwLmmmpyakLIWpTWF7LOHz1MCAluesMcqlq5kdABLE7umMn2EZMpS9nV8q0VVjdFWXkyJPSGSJnJ11NuiH-R7ZD6LugDLeaO6Qwb2oYojxbH87sPoSu3f-YnMPQc7bCOd2YEkY6Y0ZjJbZfBUOFuHhJDDqWhO6d8nvxCZJl8zLp2N8yWg1Rl8wx8WBofFU-hKHqp_L5bsPfehfYueOjwD-BNaFKvv5xqt1=w1160-h893-no?authuser=0"
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