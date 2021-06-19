from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__)

root_dir = r'E:\Documents\test'

@app.route('/')
def index():
    files = os.listdir(root_dir)
    return render_template('files_list.html', files=files)


@app.route('/<filename>')
def download(filename):
    return send_from_directory(root_dir, filename)


app.run(debug=True)
