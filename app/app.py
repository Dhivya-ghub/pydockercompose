from typing import List, Dict
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def favorite_colors() -> List[Dict]:
    try:
        config = {
            'user': 'root',
            'password': 'root',
            'host': '52.39.232.196',
            'port': '3306',
            'database': 'knights'
        }
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT name, color FROM favorite_colors')
        results = [{'name': name, 'color': color} for (name, color) in cursor]
        cursor.close()
        connection.close()
        return results
    except mysql.connector.Error as error:
        print("Error connecting to MySQL:", error)
        return []

@app.route('/')
def index() -> str:
    colors = favorite_colors()
    return jsonify({'favorite_colors': colors})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

