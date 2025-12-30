# python-web
Minimal python web app

## Features

- Simple Flask web application
- Clean and responsive design
- Two pages: Home and About
- Request logging with timing and status tracking
- Easy to extend and customize

## Requirements

- Python 3.x
- Flask 3.0.0
- Werkzeug 3.0.1

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Pages

- `/` - Home page
- `/about` - About page

## Request Logging

The application includes automatic request logging that tracks:
- HTTP method and path
- Source IP address
- Response status code
- Request duration (in seconds)

Logs are output to the console in the following format:
```
2025-12-30 15:11:44,316 - __main__ - INFO - Request: GET / from 127.0.0.1
2025-12-30 15:11:44,319 - __main__ - INFO - Response: 200 for GET / - Duration: 0.002s
```
