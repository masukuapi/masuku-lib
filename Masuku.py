import numpy as np
import onnxruntime as ort
from PIL import Image

class model:
    def __init__(self, model_path) -> None:
        self.ort_session = ort.InferenceSession(model_path)

    def infer(self, image_path) -> dict:
        input_img = Image.open(image_path)
        input_img = input_img.resize((640, 640))
        input_img = np.expand_dims(np.transpose(input_img, (2, 0, 1)), axis=0).astype(float)

        input_img = input_img.astype('float32')
        results = self.ort_session.run(None, {self.ort_session.get_inputs()[0].name: input_img})
        results = results[0][0]
        covered_prob = results[:, 0].max()
        not_covered_prob = results[:, 1].max()

        if covered_prob > 0.7:
            result = "not-covered"
        else:
            result = "covered"

        return {
            "result": result,
            "not_covered_probability": int(not_covered_prob),
            "covered_probability": int(covered_prob)
        }