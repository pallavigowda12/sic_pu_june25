import pymysql
def connectDb():
    try:
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',user="root", password="tree123",db='employee',charset='utf8mb4',port=3306)
        print("Connected to the database successfully!")
    except:
        print("Failed to connect to the database.")
    return connection