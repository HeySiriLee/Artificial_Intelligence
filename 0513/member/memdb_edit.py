import pymysql


def MemDbEdit(idx, mail, name, telno, addrs, sns):
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

        sql = "UPDATE member SET mail = %s, name = %s, telno = %s, addrs = %s, sns = %s WHERE id = %s"
        value = [mail, name, telno, addrs, sns, idx]
        cursor.excute(sql, value)
        conn.commit()

    except:
        print("Error occurred")
        
    finally:        
        conn.close()