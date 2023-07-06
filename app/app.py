from flask import Flask
import mysql.connector

app = Flask(__name__)

def favorite_colors():
    
        config = {
            'user': 'root',
            'password': 'root',
            'host': '52.39.232.196',
            'port': '3306',
            'database': 'knights'
        
        connection = mysql.connector.connect(**config)
        return connection
   

@app.route('/')
def index():
    connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        cursor.execute('SELECT name, color FROM favorite_colors')
        results = [{'name': name, 'color': color} for (name, color) in cursor]
        cursor.close()
        connection.close()
        return results
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')

