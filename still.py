from flask import Flask,render_template,request,redirect,url_for
import os
app = Flask(__name__)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        files = request.files.get('file')
        f = request.files['file']
        upload_path = os.path.join(os.path.dirname(__file__), 'imgs', f.filename)
        f.save(upload_path)
        return redirect(url_for('upload_file'))
    return render_template('upload.html')