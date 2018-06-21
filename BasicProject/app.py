"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# you can use as many decorators as you want if the same function serves multiple routes
# The variable can be part of the URL path or in a query parameter. For example, a route 
# in the form of '/hello/<name> generates a string argument called name to the function, 
# and using ?message=<msg> in the route parses the value given for the "message=" query 
# parameter and passes it to the function as msg

#@app.route('/hello/<name>?message=<msg>')
#def hello(name, msg):
#    return "Hello " + name + "! Message is " + msg + "."

@app.route('/')
@app.route('/hello')
def hello():
    """Renders a sample page."""
    return "Hello World!"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
