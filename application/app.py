from flask import Flask
import redis
import mysql.connector

app = Flask(__name__)

# Connect to Redis database
redis_db = redis.Redis(host="localhost", port=6379)

# Connect to MySQL database
mysql_db = mysql.connector.connect(
    host="localhost",
    user="app",
    password="",
    database="test"
)

@app.route("/")
def index():
    # Increment the number of visits in Redis
    visits = redis_db.incr("visits")

    # Retrieve the latest message from MySQL
    cursor = mysql_db.cursor()
    cursor.execute("SELECT message FROM messages ORDER BY id DESC LIMIT 1")
    message = cursor.fetchone()

    return f"You are visitor number {visits}. Latest message: {message}"

if __name__ == "__main__":
    app.run()
