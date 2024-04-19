from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
import os
import Masuku

app = FastAPI()

model = Masuku.model(os.path.join("models", "newbest.onnx"))
UPLOAD_FOLDER = './static/uploads'

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.filename == '':
        raise HTTPException(status_code=400, detail="No selected file")
    else:
        filename = file.filename
        file_location = f"{UPLOAD_FOLDER}/{filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())
        json_data = model.infer(file_location)
        return json_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)