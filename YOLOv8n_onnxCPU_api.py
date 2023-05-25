from flask import Flask
import run_onnx_cpu
import onnxruntime

app = Flask(__name__)

session = onnxruntime.InferenceSession("yolov8n.onnx")

@app.route('/')
def index():
    return "hello world"

@qpp.route('/detector', methods=['POST'])
def detector():
    return "1"