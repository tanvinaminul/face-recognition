# face-recognition
Face recognition using Azure Cognitive Service's Face API

It can detect face and the emotions in the face.

Also using face ID we can compare one face with another.
## Requirements
* Python
* Azure Subscription
* pip

## Installation
Crearte python virtual environment and install some ppip package
```python
python -m venv AzureVision
cd AzureVision
Scripts\activate
pip install azure.cognitiveservices.vision.face pillow pandas
```
Replace API_KEY and ENDPOINT with your azure faceapp's API_KEY and ENDPOINT

Place your image in the '/Images' folder

Run the code in terminal

You will get output in the popup window

## Output

* Output in face detection:
![Output in face detection:](Images/output1.png?raw=true "Face")

* Output in face landmark:
![Output in face landmark:](Images/output2.png?raw=true "Face2")

* Output in face emotions:
![Output in face emotions:](Images/output3.png?raw=true "Face2")

* Output in face match:
![Output in face match:](Images/output4.png?raw=true "Face2")

* Output in Terminal:
![Output in Terminal:](Images/output5.png?raw=true "Face2")

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
