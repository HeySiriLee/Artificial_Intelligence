# Look up the database

# Load the Library
import pymysql
import requests
from datetime import datetime

#########################
# Save the Database Function
#########################

def ChatGPTadd(human_chat,ai_chat):
    # Setting the database
    conn = pymysql.connect (
        host = "127.0.0.1",
        user = "chat",
        password = "Enter the password",
        port = 3306,
        db = "chatdb",
        charset = "utf8"
    )

    try:
        # Save the current date and time
        saveDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save the IP address
        saveIp = requests.get("http://ip.jsontest.com").json()["ip"]

        cursor = conn.cursor()
        
        # Processing a Insert 
        sql = "INSERT INTO chat (human_chat, ai_chat, date, ip) VALUES (%s, %s, %s, %s)"
        value = (human_chat, ai_chat, saveDate, saveIp)
        cursor.execute(sql, value)
        conn.commit()
        print("Recoded the data")

    except:
        print("Input Error:(")

    conn.close()