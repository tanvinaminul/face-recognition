import os
import io
import json
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw, ImageFont

"""
Example 5. Check if a perosn in differnet images are the same perosn
"""

credential = json.load(open('AzureCloudKeys.json'))
API_KEY = credential['API_KEY']
ENDPOINT = credential['ENDPOINT']
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

face_verified = face_client.face.verify_face_to_face(
    face_id1=matched_faces[0].face_id,
    face_id2='371e00f4-b5a5-4030-8473-3388d7016423'
)
print(face_verified.is_identical)