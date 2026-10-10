import socket
import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

REDIS_URL = os.environ.get("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL)

@app.route("/")
def counter():
    count = redis_client.incr("visit_count")
    hostname = socket.gethostname()
    return jsonify({
        "message": "访问成功",
        "count": count,
        "hostname": hostname
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)