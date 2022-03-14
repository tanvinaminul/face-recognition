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
image_url = "https://lh3.googleusercontent.com/2Pc_5-H8tGbKMh3HdtP3PGSxAFOug-Q9WwhTpV_t_RQyFurrIZqW5cxHcUPwrEZ6FJ7TZohsYuc3ta5Yb7y6B40-e_lw59OZKLRATDbdhNf-6Ubsc3CfYgQMEYO9DNTVZC8K5Ba8yHH96GJ2pvlzPLh4uTQKPcFQttpZrfdFYHCNc2C3yqWsUInLg20dQKELubnIYX1UYBbL7vxjo-glkbBbKwF_Yq6giptlnydjJHuDJK2jj4UkDsCeHlYjm-uD8zw2Bcg9X7F5WKKN0JdB4Pgp1DeLhpRi8LFGgyPZjT6mdbtdDu1SzOw2086WijAaHYNHtN8M1wH3T5s_izhleHyxw2txsYe3cJF1Qah0xan9xYCIkUjYcAcxXtm1VIl3CHR7jMiel93WLkfMy3jqzCFubBfoAgjYkqphMtXz8FWk0AlDNCQ5hL_TDLXpkNZCGkBItyzEqjZZmqKHVB7dWJXmO_tm-wh1LT4A7N8w76YclyOp9yaMtoUPzDIUDdngwHhZKEXMeBCrJ7sb0BRNdk9lAHG-hXYePxKzPsQ4QLD21nG6Biuq3wEsu56lQ0eRHHY2QluTYa77lMshcO0ode2tN-MRNYiaxGzDmyY2wMLOFvZ6Aa3hbRj3UQS7anL2IjlUDXJLHgcD1k_vKQA5rbrmSvU8-pFOCzeK60DFixF0TXXTd_zT_NQXILQEI7CNYDCCEpLH0U2qhkmwzvf1r_bo=w1191-h893-no?authuser=0"
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