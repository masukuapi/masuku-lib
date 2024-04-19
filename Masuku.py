from numpy import expand_dims, transpose, sum, array
from onnxruntime import InferenceSession
from PIL import Image


class model:
    def __init__(self, model_path) -> None:
        self.ort_session = InferenceSession(model_path)

    def infer(self, image_path) -> dict:
        input_img = Image.open(image_path)
        input_img = input_img.resize((640, 640))
        input_img = expand_dims(transpose(input_img, (2, 0, 1)), axis=0).astype(float)
        input_img /= 255.0
        input_img = input_img.astype("float32")
        output = self.ort_session.run(
            None, {self.ort_session.get_inputs()[0].name: input_img}
        )

        o1 = array(output)

   
        outputs = output[0][0]
   
        # print(prob)
        class_probabilities = output[0][0][:, -2:]
   
        sumN = 0
        sumC = 0
        for i in range(len(class_probabilities)):
            confidence = o1[0, 0, i, 4]
            sumC += confidence * o1[0, 0, i, 5]
            sumN += confidence * o1[0, 0, i, 6]
        covered_probability = sumC
        not_covered_probability = sumN
        # print(covered_probability, not_covered_probability)
        if covered_probability > not_covered_probability:
            result = "covered"
   
        else:
            result = "not-covered"
   
            # break
        if covered_probability > not_covered_probability:
            result = "covered"
        else:
            result = "not-covered"

        return {"result": result, "covered_probability": covered_probability, "not_covered_probability": not_covered_probability}
