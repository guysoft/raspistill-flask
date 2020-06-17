#!/usr/bin/python3
from flask import Flask, Response
import tempfile
import os
app = Flask(__name__)

def get_file(filename):  # pragma: no cover
    try:
        src = filename
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src,"rb").read()
    except IOError as exc:
        return str(exc)

@app.route("/")
def hello():
    temp_path = tempfile.mktemp(suffix=".jpg", prefix='/ram/')
    print(temp_path)
    os.system("sudo raspistill -drc high -o " + temp_path)
    content = get_file(temp_path)
    return Response(content, mimetype="image.jpg")
    #return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
