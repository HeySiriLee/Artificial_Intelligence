import pymysql
import requests

from datetime import datetime

def MemDbAdd(mail, name, telno, addrs, sns):
    conn = pymysql.connect(
        host = "127.0.0.1",
        user = "mem",
        password = "@ai1234@",
        port = 3306,
        db = "memdb",
        charset = "utf8"
    )

    try:
        saveIp  = requests.get("http://ip.jsontest.com").json()["ip"]
        
        cursor = conn.cursor()
        
        sql = "INSERT INTO member (mail, name, telno, addrs, sns, ip) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (mail, name, telno, addrs, sns, saveIp)
        cursor.execute(sql, value)
        conn.commit()
        print("Registered the member:)")
    
    except:
        print("Input Error:(")
    
    conn.close()
