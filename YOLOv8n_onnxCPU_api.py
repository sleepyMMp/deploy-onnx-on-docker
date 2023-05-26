import os
from flask import Flask, request
import run_onnx_cpu
import onnxruntime

app = Flask(__name__)

session = onnxruntime.InferenceSession("yolov8n.onnx")

@app.route('/')
def index():
    return "hello world"

@app.route('/detector', methods=['POST'])
def detector():
    f = request.files.get('image')
    filename = f.filename# save file 
    filepath = os.path.join( "./", filename)
    f.save(filepath)
    detected_image = run_onnx_cpu.onnxruntimeFunc(filepath,session)
    return detected_image


app.run()