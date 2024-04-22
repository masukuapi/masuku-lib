from numpy import expand_dims, transpose, sum, array
from onnxruntime import InferenceSession
from PIL import Image
from functools import lru_cache

@lru_cache(maxsize=None)
def weighted_prob_calc(o1_i_4, o1_i_x):
    return o1_i_4 * o1_i_x


class model:
    def __init__(self, model_path) -> None:
        self.ort_session = InferenceSession(model_path)

    def infer(self, image_path) -> dict:
        
        input_img = Image.open(image_path)
        input_img = input_img.resize((640, 640))
        input_img = expand_dims(transpose(input_img, (2, 0, 1)), axis=0).astype(float)
        input_img /= 255.0
        input_img = input_img.astype("float32")
        try:
            output = self.ort_session.run(None, {self.ort_session.get_inputs()[0].name: input_img})   
        except:
            return {"result": "failed to get a result"}
           
        

        output = array(output)
        sum_cov, sum_ncov= 0, 0
        for i in range(25200):
            sum_cov += weighted_prob_calc(output[0, 0, i, 4], output[0, 0, i, 5])
            sum_ncov += weighted_prob_calc(output[0, 0, i, 4], output[0, 0, i, 6])
        
        covered_probability, not_covered_probability  = sum_cov/25020 , sum_ncov/25020
 
        if covered_probability > not_covered_probability:
            result = "covered"
   
        else:
            result = "not-covered"
   
            # break
        if covered_probability > not_covered_probability:
            result = "covered"
        else:
            result = "not-covered"

        return {"result": result, "covered_score": round(covered_probability,6) , "not_covered_score": round(not_covered_probability,6)}
