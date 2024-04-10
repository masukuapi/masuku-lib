import onnxruntime as ort

# Load the ONNX model
session = ort.InferenceSession('last.onnx')