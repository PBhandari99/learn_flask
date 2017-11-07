import os
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf'])

app = Flask("compilO")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def main_page():
    return 'hello world'

@app.route("/assign", methods=["POST"])
def hello():
    if request.method == "POST":
        return request.form['name']


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# This is the post method to upload the file.
@app.route('/submit', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename + ' upload successful'
