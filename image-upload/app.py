from flask import Flask, redirect, request, send_file
import os, traceback

app = Flask(__name__)

@app.route('/')
def index():
    print("GET /")
    index_html = """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Upload Image</title>
                <style>
                fieldset { margin: 0; }  
                legend { font-size: 1.5em; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-weight: bold; }
                input { margin: 10px; }
                button { margin: 10px; }
                li { font-size: 1em; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 10px; }
                </style>
                
            </head>
            <body>
                <fieldset>
                    <form method="POST" enctype="multipart/form-data" action="/upload">
                    <legend>Upload Image</legend>
                    <input type="file" id="file" name="form_file" accept="image/jpeg"/>
                    <button>Upload</button>
                    </form>
                </fieldset>
                <br />
                
            
            """
            
    for file in list_of_files():
        index_html += "<li><a href=\"/files/" + file + "\">" + file + "</a></li>"
    
    return index_html

@app.route('/upload', methods=['POST'])
def upload():
    try:
        print("POST /upload")
        file = request.files['form_file'] 
        file.save(os.path.join("./files", file.filename))
    except:
        traceback.print_exc()
    return redirect('/')

@app.route('/files')
def list_of_files():
    print("GET /files")
    files = os.listdir("./files")
    jpgs = []
    print(files)
    for file in files:
        print(file)
        print(file.endswith('.jpg'))
        if file.endswith('.jpg'):
            jpgs.append(file)
    print(jpgs)
    return files

@app.route('/files/<filename>')
def get_file(filename):
    print("GET /files/+filename")
    return send_file('./files/' + filename)

app.run(host='0.0.0.0', port=8080)
