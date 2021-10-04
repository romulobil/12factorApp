import os
from flask import Flask
from redis import Redis

host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')
redis_host=os.environ.get('REDIS_HOST', 'redis')
redis_port=os.environ.get('REDIS_PORT', 6379)

app = Flask(__name__)
redis = Redis(host=redis_host, port=redis_port)

COUNTER = 0
@app.route('/')
def clicks():
    global COUNTER
    COUNTER = COUNTER + 1
    return {"clicks": COUNTER}

if __name__ == "__main__":
    app.run(host=host_run, debug=debug)