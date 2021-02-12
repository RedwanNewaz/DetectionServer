from flask import Flask, request
from flask_restful import Resource, Api
from functools import wraps
import base64
import numpy as np
import cv2
from queue import Queue

image_transport = Queue()
runnable = None

def image_decode(func):
    """
    :param func: post function from ImageServer class
    :return: decode base64 data to cv2 image and transfer via global variable image_transport
    """
    @wraps(func)
    def with_decoding(*args, **kwargs):
        data = request.form['data']
        print(func.__name__ + " was called")
        imageString = base64.b64decode(data)
        nparr = np.fromstring(imageString, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image_transport.put(img)
        return func(*args, **kwargs)
    return with_decoding

class ImageServer(Resource):
    """
    flask restful api is used so that image can be sent via curl as well
    """
    def get(self):
        return {'ImageServer': 'accept images that are sent via curl or python requests library'}

    @image_decode
    def post(self):
        """
        :param: runnable could be an object detection module, initialized during DetectionServer class
        :return: the output of runnable needs to be a dictionary or json string
        """
        result = image_transport.get()
        return runnable(result)



class DetectionServer(object):
    """
    This class provide a high-level interface to start an image processing server for computer vision application.
    User need to specify a custom function called module that can be generated from other libraries.
    One can also specify functor as a module
    """
    app = Flask(__name__)
    api = Api(app)
    def __init__(self,module, addr="0.0.0.0"):
        global runnable
        runnable = module
        self.address = addr
        self.api.add_resource(ImageServer, '/')

    def start(self, debug=True):
        "This function will start the flask server"
        self.app.run(host=self.address, debug=debug)



if __name__ == '__main__':
    def my_module(image):
        return {'img': 'received {}'.format(image.shape)}
    detector = DetectionServer(my_module)
    detector.start()