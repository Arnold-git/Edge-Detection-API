from flask import Flask, request, make_response, jsonify, send_file, Response
import numpy as np
import cv2
import requests
from PIL import Image
import io
from io import StringIO, BytesIO
import os
import json
from json import JSONEncoder




from utils import canny_edge


app = Flask(__name__)


app.config["ALLOWED_EXTENSIONS"] = ["png", "jpg", "jpeg"]

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024

@app.errorhandler(413)
def too_large(e):
    return "Max file size is 2MB, Please use image within 2MB.", 413

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route('/detect_edge', methods=['GET', 'POST'])
def upload_file():

    uploaded_file = request.files.get("file")


    try:


        if not uploaded_file or not allowed_file(uploaded_file.filename):


            return Response(
                json.dumps({"message" : "Please upload a Valid Image file (.jpg, .png, .jpeg)"}),
                status = 400
            )


        img = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)


 
        img = canny_edge(img)


        # imgs_final = detector.detect()


        result = np.array(img)

     

         #convert numpy array to PIL Image
        img = Image.fromarray(result.astype('uint8'))

        # create file-object in memory
        file_object = io.BytesIO()

        # write PNG in file-object
        img.save(file_object, 'PNG', quality=100)

        # move to beginning of file so `send_file()` it will read from start    
        file_object.seek(0)


        return send_file(file_object, mimetype='image/PNG')


    except:

        pass





if __name__ == "__main__":
    app.run(debug=True)
