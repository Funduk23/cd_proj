from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
import logging

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='endpoint')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info('Received request on home page')
    return 'Hello and bye, Monitoring!'
@app.route('/health')
def health():
    return "Healty", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
