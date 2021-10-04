import os
import socket
import signal
from multiprocessing import Process

from flask import Flask
from redis import Redis

host_run=os.environ.get('HOST_RUN', '0.0.0.0')
debug=os.environ.get('DEBUG', 'True')
redis_host=os.environ.get('REDIS_HOST', 'redis')
redis_port=os.environ.get('REDIS_PORT', 6379)

app = Flask(__name__)
redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def clicks():
    redis.incr('hits')
    return {
            "clicks": str(redis.get('hits')),
            "hostname": str(socket.gethostname())
           }

if __name__ == "__main__":
    def server_handler(signum, frame):
        server.terminate();
        server.join();

    signal.signal(signal.SIGTERM, server_handler);

    def run_server():
        app.run(host=host_run, debug=debug);

    server = Process(target=run_server);
    server.start();