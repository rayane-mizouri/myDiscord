import mysql.connector

class Database:
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost",user="root",password="password")
        self.cursor = self.mydb.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS myDiscord")
        self.cursor.execute("USE myDiscord;")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")
        self.cursor.execute("INSERT INTO users(first_name, last_name, email, password) SELECT 'Rayane', 'Mizouri', 'rayane.mizouri@laplateforme.io', 'password' WHERE NOT EXISTS(SELECT * FROM users WHERE first_name = 'Rayane' AND last_name = 'Mizouri')")
        self.cursor.execute("INSERT INTO users(first_name, last_name, email, password) SELECT 'Alyssa', 'Plot', 'alyssa.plot@laplateforme.io', 'password' WHERE NOT EXISTS(SELECT * FROM users WHERE first_name = 'Alyssa' AND last_name = 'Plot')")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS channels (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), is_public BOOL)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY, content TEXT, timestamp DATETIME, user_id INT, channel_id INT, FOREIGN KEY(user_id) REFERENCES users(id), FOREIGN KEY(channel_id) REFERENCES channels(id))")