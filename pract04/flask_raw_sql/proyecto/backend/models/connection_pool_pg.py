from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

dbConnection = "dbname='flaskpsql' user='postgres' host='localhost' password='Pass.123$'"

# pool define with 10 live connections
connectionpool = SimpleConnectionPool(1,10,dsn=dbConnection)

@contextmanager
def getcursor():
    con = connectionpool.getconn()
    try:
        yield con.cursor()
    finally:
        connectionpool.putconn(con)

if __name__ == "__main__":
    try:
        # with here will take care of put connection when its done
        with getcursor() as cur:
            cur.execute("select * from task")
            result_set = cur.fetchall()

        for result in result_set:
            print(result)

    except Exception as e:
        print("error in executing with exception: ", e)