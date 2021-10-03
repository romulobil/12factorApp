import os
from flask import Flask

host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')
app = Flask(__name__)

COUNTER = 0;
@app.route('/')
def clicks():
    global COUNTER
    COUNTER = COUNTER + 1
    return {"clicks": COUNTER}

if __name__ == "__main__":
    app.run(host=host_run, debug=debug)