import cv2
import torch
import pathlib
import numpy as np
import onnxruntime as ort

#Passing the input to the model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# Load the ONNX model
ort_session = ort.InferenceSession('models\\best.onnx')

input_img = cv2.imread('man.jpg')
input_img = cv2.resize(input_img, (640, 640))
input_img = torch.from_numpy(input_img).permute(2, 0, 1).unsqueeze(0).float()
input_img = input_img.to(device)

# Convert to float32
input_img = input_img.float()

# Run the model with the input image
results = ort_session.run(None, {ort_session.get_inputs()[0].name: input_img.numpy()})
results = results[0][0]
#print(results)
covered_prob = results[:, 0].max() # Maximum probability of 'covered' class
not_covered_prob = results[:, 1].max() # Maximum probability of 'not-covered' class
#print(covered_prob, not_covered_prob)
if covered_prob > not_covered_prob:
    result = "not-covered"
else:
    result = "covered"
print(f"The face in the image is {result}.")
