# Detection Server

A simple flask server to communicate with deep learning module.
Suppose that you have an object detection model where you want to send some input images via http network.
You can have multiple networks and you want them as a service to your client node. 
This package will allow you to do that with couple of line of codes. 

## How to install 
To install this library using pip 
```bash 
pip3 install git+https://github.com/RedwanNewaz/DetectionServer.git
```

## Quick Start 
To start an object detection server, you can replace my_module function with your object detection model. 

```python 
from detection_server import DetectionServer

def my_module(image):
    return {'img': 'received {}'.format(image.shape)}
detector = DetectionServer(my_module, addr="0.0.0.0", port=5000)
detector.start()
```
Note that the if you want to use the default __ip address__ and __port__, you can skip those arguments.

On the client side, you have two options: either you can use curl to send an image or 
you can use python library requests to send an image.

### Sending image via CURL 
```bash 
  echo "posting image to $OBJ_DETECTOR_SERVER"
  DATA=`cat <my_image.jpg>|base64 -w0`
  curl $OBJ_DETECTOR_SERVER -F "data=$DATA" -X POST
```


### Sending image via requests
```python
from detection_server import send_image

OBJ_DETECTOR_SERVER = 'http://0.0.0.0:5000/'
frame = cv2.imread("<my_image.jpg>")
data = send_image(OBJ_DETECTOR_SERVER, frame)
```