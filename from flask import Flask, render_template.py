from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(_name_)

@app.post("/uploadfile/")
def upload_file():
  if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
 
  content = """<!document HTML5>
<html>
  <head>
    <title>Resume Parser</title>
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
    />
  </head>
  <body>
    <div class="row">
      <div class="col-md-12">
        <a href="/"><button class="btn btn-primary">
          Home <span class="fa-fa-home"></span>
        </button> </a>
      </div>
    </div>
    <div class="row" style="display: flex;margin:5px;">
      <div class="col-md-12" style="border: 2px solid black">
        file uploaded successfully
      </div>
    </div>
  </body>
</html>"""
    
  return (content)
    # return {"File saved to disk at": fullpath}

@app.get("/")
async def home():
    content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Resume Parser</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"/>
  </head>
  <body>
  <header>
  <!-- Jumbotron -->
  <div class="jumbotron p-5 text-center bg-light">
    <h1 class="mb-3">Resume Parser</h1>
    <h4 class="mb-3">Parse your resume</h4>
  </div>
  <!-- Jumbotron -->
</header>
  <center class="jumbotron">
    <form action="/uploadfile/" enctype="multipart/form-data" method="post">
        <div class="form-group">
    <label for="exampleInputEmail1"> Pdf File  </label>
    <input required name="file" type="file" accept=".pdf" multiple>
    </div>
    <div class="form-group">
        <input class="btn btn-warning" type="submit">
        </div>
        </form>
        <center>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  </body>
</html>
    """
    return content
		
if _name_ == '_main_':
   app.run(debug = True)