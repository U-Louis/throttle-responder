from flask import Flask, request
import hashlib
import logging
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/throttle', methods=['POST'])
def throttle():
    data = request.get_json()
    throttle = data.get('throttle')
    id = data.get('id')
    app.logger.info(f'Received request: {data}')
    time.sleep(throttle/1000.0)
    response_data = {'id': id, 'throttle': throttle}
    return response_data

if __name__ == '__main__':
    run_simple('localhost', 5000, app, threaded=True)