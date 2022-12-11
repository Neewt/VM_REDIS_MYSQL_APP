from datetime import datetime
import redis
import pymysql

# Connect to the Redis database
r = redis.Redis(host='localhost', port=6379, db=0)

# Connect to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='app',
                             password='',
                             db='test')

try:
    with connection.cursor() as cursor:
        # Insert a new record into the "visits" table
        sql = "INSERT INTO visits (time) VALUES (%s)"
        cursor.execute(sql, (datetime.now(),))
        
        # Increment the "visits" key in the Redis database
        r.incr('visits')
        
        # Save the changes to the database
        connection.commit()
        
finally:
    connection.close()

# Print the number of visits from the Redis database
visits = r.get('visits')
print(f'This page has been visited {visits} times!')
