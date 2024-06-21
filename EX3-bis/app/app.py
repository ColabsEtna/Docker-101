from flask import Flask, jsonify
import json
from sqlalchemy import create_engine, text

app = Flask(__name__)
database_uri = "mysql+pymysql://test:tutu@db/mydatabase"
engine = create_engine(database_uri)

@app.route('/')
def index():
    with engine.connect() as connection:
        query = "SELECT * FROM my_table"
        result = connection.execute(text(query))
        for row in result:
            return(jsonify({"name": row.name}))

    return jsonify(json.dumps(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
