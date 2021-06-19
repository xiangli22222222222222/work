from flask import send_from_directory
@app.route('/download/<path:path>', methods=['GET', 'POST'])
def index(path):
    try:
        if os.path.isdr(filePath):
            return '<h1>文件夹无法下载</h1>'
        else:
            name=filePath.split('\\')[-1]#切割出文件名称
            filePath=filePath.replace(name,'')
            return send_from_directory(filePath,filename=name,as_attachment=True)
    except:
        return '<h1>该文件不存在或无法下载</h1>'