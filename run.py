from waitress import serve
from app import app  # Replace 'app' with the name of your Flask application module

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
