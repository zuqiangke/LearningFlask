from datetime import datetime
#from flask import Flask
from flask import render_template
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
   # html_content = "<html><head><title>Hello Flask</title></head><body>"
   # html_content += "<strong>Hello Flask</strong> on " + formatted_now
   # html_content += "</body></html>"
   # return html_content
   # return render_template("index.html", content = "<strong>Hello Flask</strong> on " + formatted_now) # render_template to load the template and supply a value for "content", which is done using a named argument matching the name of the placeholder. Flask automatically looks for templates in the templates folder
    return render_template("index.html", title="Hello Flask", message="Hello, Flask !", content = "on" + formatted_now)
