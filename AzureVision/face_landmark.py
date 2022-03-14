import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

"""
Example 2. Detect faces landmarks from an image (from a local file)
"""

API_KEY = "8eecbafb4729456498bf48a11238c58f"
ENDPOINT = "https://aminulface.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

img_file = open(r'.\Images\face1.jpg', 'rb')

response_detected_faces = face_client.face.detect_with_stream(
    image=img_file,
    detection_model='detection_03',
    recognition_model='recognition_04',
    return_face_landmarks=True
)

if not response_detected_faces:
    raise Exception('No face detected')

print('Number of people detected: {0}'.format(len(response_detected_faces)))

print(vars(response_detected_faces[0]))
print(vars(response_detected_faces[0].face_landmarks).keys())
print(response_detected_faces[0].face_landmarks.mouth_left)

img =Image.open(img_file)
draw = ImageDraw.Draw(img)

for face in response_detected_faces:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = rect.width + left
    bottom = rect.height + top
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=5)

    # mark the noise tip
    x = face.face_landmarks.nose_tip.x
    y = face.face_landmarks.nose_tip.y
    draw.rectangle(((x, y), (x, y)), outline='white', width=7)

    # draw the bounding box around the mouth
    mouth_left = face.face_landmarks.mouth_left.x, face.face_landmarks.mouth_left.y
    mouth_right = face.face_landmarks.mouth_right.x, face.face_landmarks.mouth_right.y
    lip_bottom = face.face_landmarks.under_lip_bottom.x, face.face_landmarks.under_lip_bottom.y
    draw.rectangle((mouth_left, (mouth_right[0], lip_bottom[1])), outline='yellow', width=2)

img.show()