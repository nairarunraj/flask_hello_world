#!/usr/bin/env python

from flask import Flask
# Flask takes one argument (__name__) to determine the location of the application, which in turn allows it to locate other files that are part of the application, such as images and templates
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

# Instead of using the decorator @app.route, we can also set the route using-
# app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
    app.run()
