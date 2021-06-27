import psycopg2

def db_connect():
    conn = psycopg2.connect(
        host="tuffi.db.elephantsql.com",
        database="jahysiey",
        user="jahysiey",
        password="7AldQZRicIRwRQALq-a-qgjPQPQcfHod")

def get_actors():
    conn = None
    try:
        conn = psycopg2.connect(
            host="tuffi.db.elephantsql.com",
            database="vifhcirc",
            user="vifhcirc",
            password="YuZvv4GZJx9OF2RjS8oKHxDQ2dreul4_")
        cur = conn.cursor()
        cur.execute("SELECT first_name, last_name FROM public.actor;")
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_actors()