import os
import numpy as np
import onnxruntime as ort
from PIL import Image

ort_session = ort.InferenceSession(os.path.join("models", "best.onnx"))

input_img = Image.open(os.path.join("images", "man.jpg"))
input_img = input_img.resize((640, 640))
input_img = np.expand_dims(np.transpose(input_img, (2, 0, 1)), axis=0).astype(float)

input_img = input_img.astype('float32')
results = ort_session.run(None, {ort_session.get_inputs()[0].name: input_img})
results = results[0][0]
covered_prob = results[:, 0].max()
not_covered_prob = results[:, 1].max()

if covered_prob > not_covered_prob:
    result = "not-covered"
    print(f"{result} | nc_prob: {not_covered_prob} | c_prob: {covered_prob} ")
else:
    result = "covered"
    print(f"{result} | nc_prob: {not_covered_prob} | c_prob: {covered_prob} ")


