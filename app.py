import logging
import time
from flask import Flask, render_template, request, g

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.before_request
def before_request():
    """Log incoming requests and start timer"""
    g.start_time = time.time()
    logger.info(f"Request: {request.method} {request.path} from {request.remote_addr}")

@app.after_request
def after_request(response):
    """Log response details and calculate request duration"""
    if hasattr(g, 'start_time'):
        duration = time.time() - g.start_time
        logger.info(f"Response: {response.status_code} for {request.method} {request.path} - Duration: {duration:.3f}s")
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
