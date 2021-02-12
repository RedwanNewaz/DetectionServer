import cv2
import requests
import base64



def send_image(address, image):
    """
    :param address: http (flask) server address
    :param image: cv image
    :return: text response from the server
    """
    _, img_encoded = cv2.imencode('.jpg', image)
    jpg_as_text = base64.b64encode(img_encoded)
    response = requests.post(address, data={"data":jpg_as_text})
    data = response.text
    return data

if __name__ == '__main__':
    OBJ_DETECTOR_SERVER = 'http://0.0.0.0:5000/'
    frame = cv2.imread("/home/redwan/Pictures/pedstrians/DV1842346-abbey-road-beatle.jpg")
    data = send_image(OBJ_DETECTOR_SERVER, frame)
    print(data)