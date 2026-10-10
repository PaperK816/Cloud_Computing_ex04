import socket
import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')
try:
    redis_client = redis.from_url(REDIS_URL)
    redis_client.ping()
    REDIS_AVAILABLE = True
except Exception:
    redis_client = None
    REDIS_AVAILABLE = False

local_count = 0

@app.route('/')
def counter():
    global local_count
    if REDIS_AVAILABLE and redis_client:
        try:
            count = redis_client.incr('visit_count')
        except Exception:
            local_count += 1
            count = local_count
    else:
        local_count += 1
        count = local_count

    hostname = socket.gethostname()
    return jsonify({
        'message': 'success',
        'count': count,
        'hostname': hostname
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
