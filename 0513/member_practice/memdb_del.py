import pymysql

def MemDbDel(idx):
    if idx == "":
        return False
     
    conn = pymysql.connect(
            host = "127.0.0.1",
            user = "mem",
            password = "@ai1234@",
            port = 3306,
            db = "memdb",
            charset = "utf8"
    )

    try:
        cursor = conn.cursor()

        sql = "DELETE * FROM member WHERE id = %s"
        value = idx
        cursor.execute(sql, value)
        conn.commit()

    except:
        conn.close()
        print("Error occurred")
        return False

    finally:
        conn.close()
        return True