from flask import Flask

app = Flask(__name__)

COUNTER = 0;
@app.route('/')
def clicks():
    global COUNTER
    COUNTER = COUNTER + 1
    return {"clicks": COUNTER}

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)