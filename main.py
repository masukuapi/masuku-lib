import subprocess
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import json
import re

app = Flask(__name__)

UPLOAD_FOLDER = './static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def syntax_highlight(json_data):
    json_str = json.dumps(json_data, indent=2)
    json_str = json_str.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    def replacer(match):
        cls = "number"
        if match.group(0).startswith('"'):
            if match.group(0).endswith(':'):
                cls = "key"
            else:
                cls = "string"
        elif re.fullmatch("true|false", match.group(0)):
            cls = "boolean"
        elif re.fullmatch("null", match.group(0)):
            cls = "null"
        return '<span class="' + cls + '">' + match.group(0) + "</span>"

    pattern = r'"(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?'
    json_str = re.sub(pattern, replacer, json_str)
    return json_str

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #Send Req to Model
        json_data = {
            "status": "success",
            "message": "File uploaded successfully"
        }        
        return syntax_highlight(json_data)
if __name__ == "__main__":
    subprocess.Popen("npx tailwindcss -i ./static/base.css -o ./static/style.css --watch", shell=True)
    app.run(debug=True)
