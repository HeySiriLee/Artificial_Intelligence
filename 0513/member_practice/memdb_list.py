import pymysql


def MemDbList(qry):
    # ver 2.
    result = ""

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

        if qry == "":
            sql = "SELECT id, mail, name, telno, addrs, sns FROM member"
        else:
            sql = "SELECT id, mail, name, telno, addrs, sns FROM member WHERE mail LIKE %s OR name LIKE %s OR telno LIKE %s OR addrs LIKE %s OR sns LIKE %s"
            cursor.execute(sql, ("%" + qry + "%", "%" + qry + "%", "%" + qry + "%", "%" + qry + "%", "%" + qry + "%"))
        
        result = cursor.fetchall()

        for data in result:
            print(data)

        # ver 1.
        # conn.close()
        # return result

    except:
        print("Error occurred")
        
    finally:        
        conn.close()

        return result