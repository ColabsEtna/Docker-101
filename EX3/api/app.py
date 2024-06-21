from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Docker Compose!"

@app.route('/db')
def db():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'))
        return "Connected to the database!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
