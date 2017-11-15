import os
import subprocess
#  import tarfile
from flask import Flask, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['pdf', 'tar', '.cpp', 'cc', '.h', '.hpp'])

app = Flask("compilO")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#  Use this to limit the upload size
#  app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


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


#  def unzip_tar_file(file_to_unzip):
    #  tar = tarfile.open(file_to_unzip)
    #  tar.extractall('./uploads/extracts')
    #  tar.close()
    
